(function (window) {
  var THRESHOLD = 1.02;
  var BLUR_FACTOR = 6;
  var MAX_BLUR = 12;
  var SCALE_FACTOR = 0.022;
  var SOFT_CLASS = "image--soft";
  var boundImages = [];

  function getCoverScale(img) {
    return Math.max(
      img.clientWidth / img.naturalWidth,
      img.clientHeight / img.naturalHeight
    );
  }

  function getOptions(img) {
    return {
      blurFactor: parseFloat(img.dataset.blurFactor) || BLUR_FACTOR,
      maxBlur: parseFloat(img.dataset.blurMax) || MAX_BLUR,
      scaleFactor: parseFloat(img.dataset.scaleFactor) || SCALE_FACTOR
    };
  }

  function applyUpscaleBlur(img) {
    if (!img || !img.naturalWidth || !img.naturalHeight) return;

    var scale = getCoverScale(img);
    var options = getOptions(img);

    if (scale > THRESHOLD) {
      var excess = scale - 1;
      var blur = Math.min(options.maxBlur, excess * options.blurFactor);
      var scaleUp = 1 + excess * options.scaleFactor;
      img.style.setProperty("--image-blur", blur.toFixed(2) + "px");
      img.style.setProperty("--image-scale", scaleUp.toFixed(4));
      img.classList.add(SOFT_CLASS);
      return;
    }

    img.style.removeProperty("--image-blur");
    img.style.removeProperty("--image-scale");
    img.classList.remove(SOFT_CLASS);
  }

  function bind(img) {
    if (!img || boundImages.indexOf(img) !== -1) return;

    boundImages.push(img);

    img.addEventListener("load", function () {
      applyUpscaleBlur(img);
    });

    if (img.complete) {
      applyUpscaleBlur(img);
    }
  }

  function observe(selector) {
    document.querySelectorAll(selector).forEach(bind);
  }

  function refreshAll() {
    boundImages.forEach(applyUpscaleBlur);
  }

  var resizeTimer;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(refreshAll, 120);
  });

  document.addEventListener("DOMContentLoaded", function () {
    observe("[data-upscale-blur]");
    observe(".page-hero__bg");
  });

  window.KucarsUpscaleBlur = {
    apply: applyUpscaleBlur,
    bind: bind,
    observe: observe,
    refreshAll: refreshAll
  };
})(window);
