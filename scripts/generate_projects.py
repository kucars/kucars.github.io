#!/usr/bin/env python3
"""Generate curated _projects/*.md files from structured research data."""

from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "_projects"

PROJECTS = [
    {
        "slug": "msap",
        "title": "MSAP",
        "theme": "autonomous-vehicles",
        "order": 1,
        "subtitle": "Multi-robot Symbiotic Autonomy Platform for Next-generation Cities and Smart Communities",
        "summary": "A proof-of-concept multi-robot platform for risk-aware navigation, autonomous package delivery, preference-aware mobility, integrated perception, smart patrolling, and an API for future campus applications.",
        "team": {
            "pi": {"name": "Khaled ElBassioni", "role": "Full Professor", "dept": "EECS"},
            "co_investigators": [
                {"name": "Majid Khonji", "role": "Assistant Professor", "dept": "EECS", "email": "majid.khonji@ku.ac.ae"},
            ],
        },
        "video": "https://www.youtube.com/embed/leuWJc1BwDA",
        "images": [
            "/assets/images/research/autonomous-vehicles/avlab-msap-hero.png",
        ],
        "body": """In this project, reasoning under both aleatoric and epistemic uncertainty, we seek to design a proof-of-concept Multi-robot Symbiotic Autonomy Platform (MSAP) and synthesize provably efficient controllers and algorithms for safety-critical applications in transportation and last-mile logistics.

Capitalizing on the infrastructure and equipment already in place at KU's Autonomous Vehicle Lab — including an autonomous shuttle service at the SAN campus, contactless robotic delivery vehicle, retrofitted autonomous Nissan Leaf car, legged robot, robotic arm, and four drones — we develop an MSAP operating system that enables:

1. Risk-aware multi-agent navigation through collective autonomous intelligence and collective risk assessment
2. Autonomous small-package delivery under epistemic and aleatoric uncertainty
3. User-centered passenger mobility service via preference elicitation integrated into the vehicle navigation stack
4. Integrated multi-agent perception that captures objects beyond line-of-sight of a single agent
5. Smart monitoring and patrolling for outdoor facilities such as parking areas, outdoor storage areas, and construction sites
6. An application programming interface (API) hosted on AV Lab servers for future app development on the integrated platform""",
    },
    {
        "slug": "harbot",
        "title": "HARBOT",
        "theme": "autonomous-vehicles",
        "order": 2,
        "subtitle": "Hierarchical Reasoning for Enhanced Integrated Autonomy",
        "summary": "Hierarchical reasoning, uncertainty-aware planning, compliant manipulation, and legged robot integration for logistics and agriculture applications.",
        "team": {
            "pi": {"name": "Majid Khonji", "role": "Assistant Professor", "email": "majid.khonji@ku.ac.ae"},
            "co_investigators": [
                {"name": "Jorge Dias", "role": "Professor", "email": "jorge.dias@ku.ac.ae"},
                {"name": "Lakmal Seneviratne", "role": "Professor", "email": "lakmal.seneviratne@ku.ac.ae"},
            ],
        },
        "collaborators": ["University of Belgrade"],
        "keywords": ["Autonomous Legged Robots", "Agriculture", "Logistics", "Compliant Manipulation", "Uncertainty-aware Reasoning"],
        "images": ["/assets/images/research/autonomous-vehicles/avlab-fig3.jpg", "/assets/images/research/autonomous-vehicles/avlab-fig4.jpg"],
        "objectives": [
            "Develop a hierarchical reasoning framework for integrated autonomy in autonomous legged robots and vehicle platforms",
            "Investigate techniques for distilling uncertainty from sensing, prediction, and perception modalities",
            "Design an uncertainty-aware reasoning mechanism that respects risk thresholds and quality of service constraints",
            "Explore benefits of integrating legged robots with autonomous vehicles for charging, logistics depot, and agricultural storage",
            "Develop dynamic manipulation strategies for compliant, time- and energy-efficient object handling",
        ],
        "body": """The successful integration of autonomous systems in real-world environments, such as last-mile logistics and agriculture, requires effectively handling uncertainties and risks. This research emphasizes hierarchical reasoning, uncertainty-aware planning, and compliant manipulation in autonomous legged robots integrated with autonomous vehicle platforms.

Legged robots overcome limitations of wheeled platforms on rough terrain and in delicate agricultural environments. A key aspect is leveraging prediction and perception subsystems that explicitly represent uncertainty, enabling the reasoning module to make well-informed decisions.""",
    },
    {
        "slug": "infrastructure-inspection",
        "title": "Infrastructure Inspection",
        "theme": "aerial-robotics",
        "order": 1,
        "subtitle": "Heterogeneous UGV-UAV Vision-based Control for Collaborative Inspection and 3D Reconstruction",
        "summary": "Collaborative robotic inspection with computer vision, autonomy, and field validation for infrastructure monitoring.",
        "team": {
            "pi": {"name": "Yahya Zweiri"},
            "co_investigators": [
                {"name": "Naoufel Werghi"},
                {"name": "Lakmal Seneviratne"},
                {"name": "Igor Boiko"},
                {"name": "Rafic Ajaj"},
            ],
        },
        "collaborators": ["Emirates Nuclear Energy Corporation"],
        "images": ["/assets/images/research/aerial-robotics/infrastructure-inspection-hero.png"],
        "body": """This project investigates autonomous aerial drone-based inspection of critical infrastructure and indoor farms, such as concrete containment at nuclear power plants, railway tracks, oil and gas pipelines, and greenhouses. Regular inspection and early problem detection of critical facilities allow for greater safety and efficiency.""",
    },
    {
        "slug": "cloud-seeding",
        "title": "Cloud Seeding and Monitoring",
        "theme": "aerial-robotics",
        "order": 2,
        "subtitle": "Aerial Drones for Precipitation Enhancement Through Cloud Measurements and Seeding",
        "summary": "Drone platforms and autonomy methods for weather and environmental applications.",
        "team": {
            "pi": {"name": "Yahya Zweiri"},
            "co_investigators": [
                {"name": "Naoufel Werghi"},
                {"name": "Lakmal Seneviratne"},
                {"name": "Igor Boiko"},
                {"name": "Rafic Ajaj"},
            ],
        },
        "collaborators": ["National Centre of Meteorology"],
        "images": ["/assets/images/research/aerial-robotics/ariel-fig2.jpg"],
        "body": """Unmanned Aerial Vehicles can play a crucial role in precipitation enhancement by helping identify cloud regions suitable for seeding and performing cloud seeding. This framework establishes testing, validation, and enhancement frameworks for assessing UAV performance for cloud seeding in the UAE context, in collaboration with the National Center of Meteorology.""",
    },
    {
        "slug": "surveillance-inspection",
        "title": "Surveillance and Inspection",
        "theme": "aerial-robotics",
        "order": 3,
        "subtitle": "Surveillance and Inspection in Uniform Appearance Scenes Using Aerial Vehicles",
        "summary": "Aerial drone-based solutions for surveillance and inspection in security and agriculture applications.",
        "team": {
            "pi": {"name": "Naoufel Werghi"},
            "co_investigators": [
                {"name": "Yahya Zweiri"},
                {"name": "Lakmal Seneviratne"},
                {"name": "Igor Boiko"},
                {"name": "Rafic Ajaj"},
            ],
        },
        "collaborators": ["Silal", "Abu Dhabi Police"],
        "images": ["/assets/images/research/aerial-robotics/surveillance-inspection-hero.png"],
        "body": """This project provides aerial drone-based solutions for surveillance and inspection in security and agriculture. Research efforts focus on monitoring uniform-appearance crowds and scenes, and regular inspection with early detection of plant disease.""",
    },
    {
        "slug": "marvel",
        "title": "MARVEL",
        "theme": "marine-robotics",
        "order": 1,
        "subtitle": "Maritime Advanced Robotics, Vision, Efficiency, and Learning",
        "summary": "Underwater multi-robot autonomy with visual language models, multimodal AI, 3D mapping, coral and infrastructure monitoring, and adaptive power-aware operation.",
        "team": {
            "pi": {"name": "Jorge Dias", "role": "Professor", "dept": "Electrical Engineering"},
            "co_investigators": [
                {"name": "Federico Renda", "role": "Associate Professor", "dept": "Mechanical & Nuclear Engineering"},
                {"name": "Sajid Javed", "role": "Assistant Professor", "dept": "Computer Science"},
                {"name": "Naoufel Werghi", "role": "Professor", "dept": "Computer Science"},
            ],
        },
        "sponsors": ["DSUF"],
        "images": ["/assets/images/research/marine-robotics/marine-fig1.jpg"],
        "body": """MARVEL integrates underwater multi-robot autonomous systems with visual language models and multimodal AI to enable wide-area monitoring in underwater environments. Collaboration among autonomous underwater vehicles enables assessment of water quality and environmental health, producing 3D mapping of physical and chemical environmental parameters.

Advanced computer vision models allow online and offline observation of marine life, particularly coral reefs, and man-made structures like aquaculture farms, oil and gas facilities, and ports. MARVEL develops unified multi-modal 3D mappings for intelligent vision-language tasks such as Visual Question Answering, image captioning, and Text-to-Image search.""",
    },
    {
        "slug": "embodied-neuromorphic-ai",
        "title": "Embodied Neuromorphic AI",
        "theme": "marine-robotics",
        "order": 2,
        "subtitle": "Intel Neuromorphic Research for Robotic Perception",
        "summary": "Neuromorphic technologies from perception to motor control for compact, low-power robots that interact autonomously with their environment.",
        "team": {
            "pi": {"name": "Jorge Dias"},
            "co_investigators": [{"name": "VSAP Lab members"}],
        },
        "collaborators": ["Intel"],
        "images": ["/assets/images/research/marine-robotics/marine-fig2.jpg"],
        "body": """The design of robots that interact autonomously with the environment and exhibit complex behaviors can benefit from understanding what makes living beings fit to act in the world. Neuromorphic engineering studies neural computational principles to develop compact, low-power processing systems. This project demonstrates why endowing robots with neuromorphic technologies — from perception to motor control — is a promising approach for creating robots that can seamlessly integrate in society.""",
    },
    {
        "slug": "neuromorphic-hardware",
        "title": "Neuromorphic Hardware",
        "theme": "marine-robotics",
        "order": 3,
        "subtitle": "KU and NYU Collaboration on Neuromorphic Computing",
        "summary": "Neuromorphic chips, algorithms, and hardware architectures for efficient AI and robotics.",
        "team": {
            "pi": {"name": "Jorge Dias"},
            "co_investigators": [
                {"name": "Muhammed Shafique", "affiliation": "NYU"},
                {"name": "Fakhreddine Zayer"},
            ],
        },
        "collaborators": ["Intel", "NYU"],
        "images": ["/assets/images/research/marine-robotics/marine-fig3.png"],
        "body": """This collaborative project between KU and NYU explores neuromorphic hardware that mimics neural architecture and functioning of the human brain. Focus areas include development of neuromorphic chips, algorithm optimization for neuromorphic systems, applications in AI and robotics, and interdisciplinary research combining neuroscience, computer science, and electrical engineering.""",
    },
    {
        "slug": "marine-ocean-interventions",
        "title": "Marine Robotics for Ocean Interventions",
        "theme": "marine-robotics",
        "order": 4,
        "subtitle": "Underwater Mobile Manipulation for Maintenance and Repair",
        "summary": "Compliant underwater arms and multimodal perception for semi-autonomous rope manipulation and knotting.",
        "team": {
            "pi": {"name": "Federico Renda"},
            "co_investigators": [{"name": "Irfan Hussain"}],
        },
        "sponsors": ["Khalifa University"],
        "collaborators": ["Stanford University"],
        "images": ["/assets/images/research/marine-robotics/marine-fig4.jpg"],
        "body": """Constructing, maintaining, and repairing offshore facilities is challenging, requiring specialized vessels and human divers. This project investigates underwater mobile manipulators for maintenance and repair tasks, focusing on compliance and torque control, novel compliant underwater arms, and multimodal underwater perception systems.""",
    },
    {
        "slug": "underwater-swarm",
        "title": "Underwater Swarm Robotics",
        "theme": "marine-robotics",
        "order": 5,
        "subtitle": "Heterogeneous Swarm of Underwater Autonomous Vehicles",
        "summary": "A school of 30 hybrid underwater robotic fishes with distributed sensing and communication.",
        "team": {"pi": {"name": "Federico Renda"}},
        "sponsors": ["Technology Innovation Institute"],
        "collaborators": ["TII"],
        "images": ["/assets/images/research/marine-robotics/marine-fig5.png"],
        "body": """Inspired by biological school fishes, this project implements an artificial school of 30 hybrid underwater robots — 5 special fishes with enhanced sensors and communication, and 25 autonomous fishes with inter-robot communication and emergency recovery. A floating beacon collects data from the swarm, and a static seafloor robot resurfaces after operation to collect environmental data.""",
    },
    {
        "slug": "artificial-feather-stars",
        "title": "Artificial Feather Stars",
        "theme": "marine-robotics",
        "order": 6,
        "subtitle": "Multi-functional, Multi-agent Soft Underwater Robotics",
        "summary": "Soft underwater robot inspired by feather stars for propulsion and manipulation in unstructured environments.",
        "team": {"pi": {"name": "Federico Renda"}},
        "sponsors": ["ONRG"],
        "images": ["/assets/images/research/marine-robotics/marine-fig6.png"],
        "body": """This project proposes a novel underwater soft robot inspired by feather stars, composed of multiple branching soft modules that combine propulsion and manipulation skills for a highly redundant system adaptable to different tasks, including safe manipulation of human-made underwater structures such as oil and gas pipelines.""",
    },
    {
        "slug": "biomimetic-thrust",
        "title": "Biomimetic Jet Propulsion",
        "theme": "marine-robotics",
        "order": 7,
        "subtitle": "Biomimetic-joint-thrust System for Underwater Propulsion",
        "summary": "Soft jet propulsor inspired by cephalopod swimming for controllable outlet position and orientation.",
        "team": {
            "pi": {"name": "Imran Afgan"},
            "co_investigators": [
                {"name": "Federico Renda"},
                {"name": "Vladimir Parezanovic"},
                {"name": "Sajid Javed"},
            ],
        },
        "sponsors": ["Khalifa University"],
        "collaborators": ["University of Edinburgh"],
        "images": ["/assets/images/research/marine-robotics/marine-fig7.png"],
        "body": """Inspired by cephalopod jet propulsion, this project presents a soft jet propulsor that controls outlet position and orientation by combining volume-squeezing actuation with a second actuator for propulsor orientation, merging high-speed maneuverability of rigid propellers with advantages of soft robotics.""",
    },
    {
        "slug": "mbzirc-maritime",
        "title": "MBZIRC Maritime Grand Challenge",
        "theme": "marine-robotics",
        "order": 8,
        "subtitle": "Mohamed Bin Zayed International Robotics Challenge — Maritime Security",
        "summary": "Heterogeneous fleet of aerial and surface vehicles for GNSS-denied maritime search, detection, and retrieval.",
        "team": {"pi": {"name": "Irfan Hussain", "role": "KU Team Lead"}},
        "sponsors": ["Khalifa University", "ASPIRE"],
        "collaborators": ["Beijing Institute of Technology"],
        "images": ["/assets/images/research/marine-robotics/marine-fig8.png"],
        "body": """The MBZIRC Maritime Grand Challenge deploys robot technology for maritime security. A heterogeneous fleet of autonomous aerial and surface vehicles collaborates in a GNSS-denied coastal environment to detect predefined targets and retrieve objects. The KU team uses 20 UAVs and 1 USV with robotic arm for wide-area cooperative search, 3D modeling, and object retrieval.""",
    },
    {
        "slug": "aquaculture-robotics",
        "title": "Aquaculture Robotics",
        "theme": "marine-robotics",
        "order": 9,
        "subtitle": "Autonomous Underwater Robotic System for Aquaculture Applications",
        "summary": "Computer vision with ROVs to detect fish net defects and assess fish health for UAE aquaculture.",
        "team": {
            "pi": {"name": "Lakmal Seneviratne"},
            "co_investigators": [{"name": "Irfan Hussain"}],
        },
        "sponsors": ["Khalifa University"],
        "images": ["/assets/images/research/marine-robotics/marine-fig9.png"],
        "body": """UAE aims to meet fish demand through expanding aquaculture infrastructure. This project creates an autonomous underwater robotic system for efficient aquafarm monitoring, using advanced computer vision with ROVs to detect fish net defects and assess fish health.""",
    },
    {
        "slug": "port-inspection",
        "title": "Port Inspection Robotics",
        "theme": "marine-robotics",
        "order": 10,
        "subtitle": "Autonomous Robotic Systems for Port Inspection",
        "summary": "USV and UAV system for autonomous port surveillance, activity detection, and alert generation.",
        "team": {"pi": {"name": "Irfan Hussain"}},
        "sponsors": ["Chinese Ministry of Science and Technology"],
        "collaborators": ["Beijing Institute of Technology"],
        "images": ["/assets/images/research/marine-robotics/marine-fig10.png"],
        "body": """This project enhances port security through an autonomous inspection system of a USV and multiple UAVs. The USV focuses on water surface surveillance while UAVs monitor airspace. Deep learning identifies unusual activities, with path planning, collision avoidance, and autonomous landing and grasping techniques.""",
    },
    {
        "slug": "stanford-marine-collaboration",
        "title": "Stanford Marine Collaboration",
        "theme": "marine-robotics",
        "order": 11,
        "subtitle": "KUCARS and Stanford SRL Marine Robotics Research",
        "summary": "Joint research on marine robotics for environment monitoring, infrastructure inspection, and human-robot interaction.",
        "team": {
            "pi": {"name": "Irfan Hussain"},
            "co_investigators": [{"name": "Federico Renda"}],
        },
        "collaborators": ["Stanford University"],
        "body": """Khalifa University and Stanford University collaborate on marine robotic technologies for operations at depth, focusing on environment monitoring, critical infrastructure inspection, interventions including maintenance operations, and human-robot interaction with haptic interfaces and embodied intelligence.""",
    },
    {
        "slug": "coral-reef-inspection",
        "title": "Coral Reef Inspection",
        "theme": "marine-robotics",
        "order": 12,
        "subtitle": "Autonomous Coral Reef Inspection",
        "summary": "Marine robot capabilities for reef ecology monitoring with improved spatial and temporal resolution.",
        "team": {
            "pi": {"name": "Lakmal Seneviratne"},
            "co_investigators": [{"name": "Irfan Hussain"}],
        },
        "sponsors": ["ENEC"],
        "body": """Coral reefs are important indicators of marine ecology health under threat from global warming, pollution, and human activity. This project extends marine robot capabilities to monitor reefs with better spatial and temporal ranges and resolutions than traditional human diver observation.""",
    },
    {
        "slug": "erasmus-unicas",
        "title": "Erasmus+ UNICAS Partnership",
        "theme": "marine-robotics",
        "order": 99,
        "type": "partnership",
        "subtitle": "Mobility Program with University of Cassino and Southern Lazio",
        "summary": "International academic exchange between UNICAS (Italy) and Khalifa University fostering cross-cultural research collaboration.",
        "team": {
            "pi": {"name": "Jorge Dias"},
            "co_investigators": [
                {"name": "Fakhreddine Zayer"},
            ],
        },
        "collaborators": ["Università degli Studi di Cassino e del Lazio Meridionale"],
        "body": """This Erasmus+ mobility program enables students, faculty, and staff from UNICAS and Khalifa University to engage in short-term study, teaching, and training opportunities, promoting cross-cultural dialogue and strengthening institutional partnerships between Europe and the Middle East.""",
    },
    {
        "slug": "kura-robokup",
        "title": "KURA and RoboKUp",
        "theme": "industrial-robotics",
        "order": 1,
        "subtitle": "Robotics and Soccer as an Applied Autonomy Platform",
        "summary": "A robotics platform using soccer-inspired challenges to advance perception, planning, control, and cooperative autonomy.",
        "team": {
            "pi": {"name": "Hamad Karki"},
            "co_investigators": [{"name": "Giulia De Masi"}],
        },
        "images": ["/assets/images/research/industrial-robotics/the4-fig1.png"],
        "body": """At RoboKUp, robots and soccer team up for a game-changing experience. The platform sparks passion for soccer and technology, building a new playbook where humans and robots collaborate — advancing perception, planning, control, and cooperative autonomy through competitive challenges.""",
    },
    {
        "slug": "autonomous-greenhouse-farming",
        "title": "Autonomous Greenhouse Farming",
        "theme": "industrial-robotics",
        "order": 2,
        "subtitle": "Agri Robotics for Greenhouse Farming",
        "summary": "Autonomous manipulation, crop monitoring, and visual servoing for agricultural systems in controlled and desert environments.",
        "team": {
            "pi": {"name": "Lakmal Seneviratne"},
            "co_investigators": [{"name": "Irfan Hussain"}],
        },
        "sponsors": ["Khalifa University"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig2.png"],
        "body": """This theme investigates AI-driven mobile grasping and manipulation for agriculture. Robotics can revolutionize agriculture through planting, inspection, harvesting, and weeding, with advances in AI enabling deployment in unstructured environments for agriculture, conservation, and space exploration.""",
    },
    {
        "slug": "vri-indoor-farming",
        "title": "VRI Indoor Farming",
        "theme": "industrial-robotics",
        "order": 3,
        "subtitle": "AI-driven Robotics for Greenhouse and Indoor Farming",
        "summary": "AI-based localization and robot-assisted harvesting for sustainable indoor agriculture.",
        "team": {
            "pi": {"name": "Lakmal Seneviratne"},
            "co_investigators": [{"name": "Irfan Hussain"}],
        },
        "sponsors": ["ASPIRE"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig3.png"],
        "body": """This project focuses on AI-based localization and robot-assisted harvesting for indoor farming, with real-time monitoring and crop growth models optimized for local conditions. The aim is a high-quality, cost-effective agricultural solution prioritizing sustainability and yield efficiency.""",
    },
    {
        "slug": "knee-exoskeleton",
        "title": "Compliant Knee Exoskeleton",
        "theme": "industrial-robotics",
        "order": 4,
        "subtitle": "Rehabilitation and Assistance for Post-stroke Hemiplegic Patients",
        "summary": "Compliant knee exoskeleton with stiffness modulation resembling human knee gait for effective patient assistance.",
        "team": {"pi": {"name": "Irfan Hussain"}},
        "sponsors": ["ARIC", "Mubadala"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig4.jpg"],
        "body": """Stroke survivors often struggle with knee joint mobility. This project introduces a compliant knee exoskeleton with stiffness modulation resembling the human knee during gait, offering effective rehabilitation assistance beyond traditional therapist-led repetitive exercises.""",
    },
    {
        "slug": "sixth-finger",
        "title": "User-Defined Sixth Finger",
        "theme": "industrial-robotics",
        "order": 5,
        "subtitle": "Robotic Assistive Device to Support Stroke Patients",
        "summary": "Supernumerary robotic limb for stroke patients with user-centric evaluation prioritizing patient experience.",
        "team": {"pi": {"name": "Irfan Hussain"}},
        "sponsors": ["STINT", "Swedish Government"],
        "collaborators": ["Chalmers University of Technology"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig5.jpg"],
        "body": """After stroke, many face challenges with hand and finger movements. Supernumerary robotic limbs augment the functioning limb or support the impaired one. This research develops assistive technology with user-centric evaluation methods, in collaboration with Chalmers University's Interaction Design Unit.""",
    },
    {
        "slug": "compliant-robotic-hands",
        "title": "Compliant Robotic Hands",
        "theme": "industrial-robotics",
        "order": 6,
        "subtitle": "Embodied Human-like Compliance and Sensing for Soft Manipulation",
        "summary": "Robust robotic hands with human hand synergies, neuromorphic tactile sensing, and complex environment grasping.",
        "team": {"pi": {"name": "Irfan Hussain"}},
        "sponsors": ["Khalifa University"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig6.png"],
        "body": """This project merges design, actuation, sensing, and control for robust robotic hands inspired by human hand synergies. Contributions include grasping algorithms and neuromorphic event-based tactile sensing, with applications in agriculture and medicine for delicate and irregular items.""",
    },
    {
        "slug": "compliant-manipulation",
        "title": "Compliant Manipulation",
        "theme": "industrial-robotics",
        "order": 7,
        "subtitle": "Safe Human-Robot Collaboration in Industrial Tasks",
        "summary": "Compliant robotic manipulation with switchable compliant and rigid modes for safe human-robot co-working.",
        "team": {"pi": {"name": "Irfan Hussain"}},
        "sponsors": ["Khalifa University"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig7.png"],
        "body": """This project develops compliant robotic manipulation systems for safe human-robot collaboration in complex industrial tasks, combining novel mechanical design, advanced sensing, intelligent control, and human intention prediction. Systems are benchmarked against commercial manipulators such as Baxter and KUKA iiwa.""",
    },
    {
        "slug": "hubot-houbara",
        "title": "Hubot",
        "theme": "industrial-robotics",
        "order": 8,
        "subtitle": "Houbara Robot for Behavioural Studies and Sampling",
        "summary": "Robot mimicking houbara birds for field observation, interaction, and semen collection in natural habitats.",
        "team": {
            "pi": {"name": "Irfan Hussain"},
            "co_investigators": [{"name": "Lakmal Seneviratne"}],
        },
        "sponsors": ["International Fund for Houbara Conservation"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig8.png"],
        "body": """Robots mimicking bird species enable behavioural studies without disturbing natural behaviours. This houbara robot observes and interacts with birds in the wild, and can collect semen from wild males to capture genetic diversity for conservation programs without removing individuals.""",
    },
    {
        "slug": "houbara-ai",
        "title": "Houbara Wildlife AI",
        "theme": "industrial-robotics",
        "order": 9,
        "subtitle": "Artificial Intelligence for Understanding Houbara Wildlife in UAE",
        "summary": "AI-enabled models to analyze sensory data for bird pose, behavior, vegetation cover, and trap picture analysis.",
        "team": {
            "pi": {"name": "Sajid Javed"},
            "co_investigators": [
                {"name": "Naoufel Werghi"},
                {"name": "Irfan Hussain"},
                {"name": "Lakmal Seneviratne"},
            ],
        },
        "sponsors": ["International Fund for Houbara Conservation"],
        "images": ["/assets/images/research/industrial-robotics/the4-fig9.png"],
        "body": """IFHC scientists collect large amounts of sensory data including pictures and videos from wild and captive houbara populations. This project investigates AI-enabled computational models to analyze and understand this data for interpretative tasks including bird pose, behavior, vegetation cover, and trap picture analysis.""",
    },
]


def yaml_value(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if re_needs_quote(text):
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def re_needs_quote(text: str) -> bool:
    import re
    return bool(re.search(r'[:#\[\]{},&*!|>\'"%@`]', text) or text.startswith(("-", "?", "|")))


def write_person(prefix: str, person: dict, indent: str) -> list[str]:
    lines = [f"{indent}{prefix}:"]
    sub = indent + "  "
    for key in ("name", "role", "dept", "email", "affiliation"):
        if key in person:
            lines.append(f"{sub}{key}: {yaml_value(person[key])}")
    return lines


def render_project(project: dict) -> str:
    lines = ["---"]
    lines.append(f"title: {yaml_value(project['title'])}")
    lines.append(f"theme: {project['theme']}")
    lines.append(f"order: {project['order']}")
    lines.append(f"subtitle: {yaml_value(project['subtitle'])}")
    lines.append(f"summary: {yaml_value(project['summary'])}")
    if project.get("type"):
        lines.append(f"type: {project['type']}")
    team = project.get("team", {})
    if team:
        lines.append("team:")
        if team.get("pi"):
            lines.extend(write_person("pi", team["pi"], "  "))
        if team.get("co_investigators"):
            lines.append("  co_investigators:")
            for person in team["co_investigators"]:
                lines.append("    - name: " + yaml_value(person["name"]))
                for key in ("role", "dept", "email", "affiliation"):
                    if key in person:
                        lines.append(f"      {key}: {yaml_value(person[key])}")
    for field in ("keywords", "objectives", "sponsors", "collaborators"):
        if project.get(field):
            lines.append(f"{field}:")
            for item in project[field]:
                lines.append(f"  - {yaml_value(item)}")
    if project.get("images"):
        lines.append("images:")
        for src in project["images"]:
            lines.append(f"  - src: {yaml_value(src)}")
    if project.get("video"):
        lines.append(f"video: {yaml_value(project['video'])}")
    lines.append("---")
    lines.append("")
    lines.append(textwrap.dedent(project["body"]).strip())
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    for path in PROJECTS_DIR.glob("*.md"):
        path.unlink()
    for project in PROJECTS:
        dest = PROJECTS_DIR / f"{project['slug']}.md"
        dest.write_text(render_project(project), encoding="utf-8")
        print(f"Wrote {dest.name}")
    print(f"Generated {len(PROJECTS)} projects")


if __name__ == "__main__":
    main()
