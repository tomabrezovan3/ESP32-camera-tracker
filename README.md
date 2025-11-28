!!!This is (hopefully) my first true and successful project!!!!


ESP32 camera tracker - project overview


1. Goal

Build an autonomous camera-tracking system using:
    -> ESP32-S3-CAM
    -> Python computer vision (OpenCV)
    -> Serial communication
    -> Pan/tilt servos for tracking


2. Planned features

    -> Real-time object detection (OpenCV)
    -> Tracking algorithm (centroid tracking)
    -> Send servo commands to ESP32 via USB/Serial
    -> ESP32 controls the camera module + servos
    -> Optional: PID control for smooth tracking


3. Hardware required

    -> ESP32-S3-CAM
    -> Micro servos (2x - pan & tilt)
    -> USB-C Cable
    -> 3D-printed or simple servo mount


4. Software structure

    ESP32-camera-tracker/
    │
    ├─ Arduino/ # ESP32 firmware
    ├─ Python/ # Tracking scripts
    ├─ venv/ # Virtual environment
    ├─ README.md
    ├─ requirements.txt
    └─ .gitignore


5. Roadmap

    -> Set up project structure
    -> Write initial README
    -> Initialize Python environment
    -> Test OpenCV webcam tracking
    -> Write serial communication code
    -> Write Arduino servo control module
    -> Integrate tracking + ESP32
    -> Real-time tuning
    -> Final testing + documentation



