---
title: A New Solution for Visual Object Tracking in Robotics
date: 2021-11-28
source: KUCARS
source_url: "https://www.ku.ac.ae/research-center-news-single?single-news=a-new-solution-for-visual-object-tracking-in-robotics&research-center=MzQ1MzQ="
image: /assets/images/news/a-new-solution-for-visual-object-tracking-in-robotics.jpg
summary: "Teaching robots to follow a moving object is more difficult than you think, requiring complex algorithms and a different way of thinking.   Take a look around. What do you see? Most of us have two eyes and we use those eyes to collect light that reflects off the objects around us. The eyes convert that light into el..."
---

***Teaching robots to follow a moving object is more difficult than you think, requiring complex algorithms and a different way of thinking.***

Take a look around. What do you see? Most of us have two eyes and we use those eyes to collect light that reflects off the objects around us. The eyes convert that light into electrical signals that are processed by our brain. This builds a representation of the world and we use that to navigate during our everyday lives. Even robots that are the most like humans in appearance, however, don’t see the world the way we do.

Instead, algorithms recognize features in images collected by a robot’s sensors and cameras. The software may create a very basic map of the environment and learn to recognize patterns to help the robot understand its surroundings. This means that robots are being programmed by humans to see things the human thinks the robot will need to see. While this has many very successful examples, no robot is capable of navigating the world using just vision for static recognition.

If you spot a bird outside, you can watch that bird fly through the sky until it lands or disappears from view. This is visual object tracking, and it’s a simple task for humans: spot the object and follow it. For robots, it’s much more difficult.

To improve visual object tracking in robotic applications, Dr. Sajid Javed, Assistant Professor, Dr. Jorge Dias, Professor, Dr. Lakmal Seneviratne, Professor, and Dr. Naoufel Werghi, Professor, all from the Department of Electrical Engineering and Computer Science at Khalifa University, collaborated with Dr. Arif Mahmood from Information Technology University, Pakistan, to develop an AI algorithm that is both highly accurate and quick when detecting and tracking a generic object. Their proposed solution was published in[ IEEE Transactions on Cybernetics](https://ieeexplore.ieee.org/document/9475879).

“Visual object tracking is a fundamental and challenging task in many high-level vision and robotics applications,” Dr. Javed explains. “Typically, the difficulties lie in developing detection algorithms that can handle blurred images from fast motion, ignore background clutter and deal with significant scale and light variations.”

Object tracking is an application of deep learning where a program takes an initial set of object detections and follows them as they move around frames in a video. The algorithms allow the robot to automatically identify an object in a video and interpret it as a set of trajectories to predict where it will end up.

The first step in tracking an object is to detect it. The research team’s solution narrows a search area down and instructs the robot to find all object instances of one or more pre-determined object classes. The algorithm is trained on a series of examples of these object classes to learn what it is looking for, regardless of the object’s scale, location or pose and despite any partial occlusions or poor lighting conditions.

Once the object has been identified, it needs to be followed. Robots can do this by continuously re-identifying the object in subsequent images, but for visual object tracking to be useful in robotic applications, interpreting the object as a set of trajectories with high accuracy is required.

Algorithms for tracking objects need to accurately perform detections and localize objects of interest in the least amount of time possible. This is especially imperative for real-time object tracking models.

“Discriminative correlation filters (DCF) are well suited to object tracking because of their impressive performance in terms of speed and accuracy,” Dr. Javed says. “In most DCF methods, an online correlation filter is trained from the region of interest in the current frame and then employed to track the target object in subsequent frames.”

High detection accuracy and fast processing speed are difficult to combine: More accurate tracking tasks often require longer processing times, while quicker responses are more prone to errors. In the research team’s solution, accuracy and speed are achieved by constructing a spatiotemporal graph that models and predicts where an object is likely to appear based on its previous identified location. Out of a series of possible trajectories, the most probable is selected by the DCF, which filters the background noise and any other distractions.

To evaluate their algorithm, the team tested it on six challenging benchmark datasets and compared it with 33 existing state-of-the-art trackers. Their results were excellent, achieving higher accuracy than existing trackers on many tests and ranking among the top three for the remaining tests.

As mobile robots and autonomous machines are increasingly deployed, object detection systems are becoming more important. Although great progress is being made, we are still far from achieving human-level performance, but solutions like this are a vital step towards that level of performance.

**Jade Sterling**

**Science Writer**

**28 November 2021**
