---
title: Autonomous Vehicles Lab
layout: research-theme
theme_slug: autonomous-vehicles
permalink: /research/autonomous-vehicles/
---

Explore publications, software, datasets, and platforms on the dedicated lab site: **[avlab.io](https://avlab.io/)**.

## Software & DevOps

The lab develops three core autonomy stacks for perception, planning, validation, and fleet coordination. Full details are on the [DevOps page](https://avlab.io/2-devops.html).

<div class="devops-stack">
  <article class="devops-item">
    <img src="/assets/images/research/autonomous-vehicles/avlite.png" alt="AVLite logo" width="80" height="80" loading="lazy">
    <div>
      <h3><a href="https://github.com/AV-Lab/avlite" target="_blank" rel="noopener noreferrer">AVLite</a></h3>
      <p>High-level autonomy stack for advanced decision-making, perception, and planning — enabling robust navigation and complex task execution. <a href="https://avlab.io/avlite/" target="_blank" rel="noopener noreferrer">AVLite documentation</a>.</p>
    </div>
  </article>
  <article class="devops-item">
    <img src="/assets/images/research/autonomous-vehicles/orbit.png" alt="ORBit logo" width="80" height="80" loading="lazy">
    <div>
      <h3>ORBit</h3>
      <p>Mid-level autonomy stack focused on real-time risk assessment and high-level plan validation through independent evaluation and agentic verification.</p>
    </div>
  </article>
  <article class="devops-item">
    <img src="/assets/images/research/autonomous-vehicles/pigeon.png" alt="Pigeon logo" width="80" height="80" loading="lazy">
    <div>
      <h3>Pigeon</h3>
      <p>Cloud-based backend for coordination, data management, and multi-agent collaboration — supporting remote monitoring and digital twin integration.</p>
    </div>
  </article>
</div>

<p>Source code and releases are on <a href="https://github.com/AV-Lab" target="_blank" rel="noopener noreferrer">GitHub</a>. The lab fleet includes passenger shuttles and a retrofitted Nissan Leaf equipped with LiDAR and cameras for last-mile mobility and data collection.</p>

## Datasets

Open datasets support autonomous driving research in Gulf urban traffic, high-speed racing, desert off-road navigation, and campus shuttle operation. All datasets are licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC-SA 4.0</a>. Browse and download from the [datasets page](https://avlab.io/1-datasets.html).

<div class="dataset-grid">
  <article class="dataset-card">
    <h3><a href="https://avlab.io/emt-dataset/" target="_blank" rel="noopener noreferrer">Emirates Multi-Task (EMT)</a></h3>
    <p>57 minutes of annotated urban traffic footage from the Gulf Region — pedestrians, cyclists, and seven vehicle classes across dense traffic, rain, and night-time reflections.</p>
  </article>
  <article class="dataset-card">
    <h3><a href="https://avlab.io/EagleVision/" target="_blank" rel="noopener noreferrer">EagleVision</a></h3>
    <p>LiDAR perception benchmark spanning A2RL and Indy Autonomous Challenge data — 28,056 labeled frames for 3D detection and trajectory prediction across three domains.</p>
  </article>
  <article class="dataset-card dataset-card--has-image">
    <figure>
      <img src="/assets/images/research/autonomous-vehicles/O2DTD_Dataset_Demo_cropped.gif" alt="O2DTD desert trail detection samples across lighting conditions" loading="lazy">
    </figure>
    <h3><a href="https://avlab.io/datasets/offroad" target="_blank" rel="noopener noreferrer">Off-Road Open Desert Trail Detection (O2DTD)</a></h3>
    <p>5,045 RGB images for desert freespace detection across six lighting conditions from dawn through night.</p>
  </article>
  <article class="dataset-card dataset-card--has-image">
    <figure>
      <img src="/assets/images/research/autonomous-vehicles/KUAS_Dataset_cropped.png" alt="Khalifa University autonomous shuttle sensor layout" loading="lazy">
    </figure>
    <h3><a href="https://avlab.io/datasets/shuttle" target="_blank" rel="noopener noreferrer">KU Autonomous Shuttle (KUAS)</a></h3>
    <p>~20 minutes of unlabeled multi-sensor data from the SAN Campus shuttle — eight LiDARs, monochrome cameras, IMU, and GPS.</p>
  </article>
</div>
