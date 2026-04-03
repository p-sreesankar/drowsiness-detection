# Drowsiness Detection System

Real-time computer vision project that monitors eye aspect ratio (EAR) from webcam input and triggers an alert when sustained eye closure indicates potential driver fatigue.

## Problem Statement

Driver drowsiness is a major safety risk, especially during long-distance travel and night driving. Manual monitoring is unreliable, and many low-cost setups lack real-time feedback.

## Solution

This project performs live face-landmark inference using MediaPipe, computes EAR per frame, applies threshold-based decision logic, and raises an audible warning when drowsiness persists across consecutive frames.

## Key Features

- Real-time webcam pipeline for continuous fatigue monitoring.
- Face landmark inference with EAR-based eye-state estimation.
- Consecutive-frame logic to reduce false positives from normal blinking.
- Visual overlay showing current status and EAR value.
- Modular structure with separate camera and detection components.

## Tech Stack

- Python
- OpenCV
- MediaPipe Tasks Vision (Face Landmarker)
- NumPy
- Windows audio alert via winsound

Relevant ML and deployment keywords for recruiters and ATS:
- Inference
- Preprocessing
- Real-time computer vision
- Threshold-based classification
- UI integration (live overlay)
- TensorFlow and Keras extensibility path
- MNIST-style benchmarking approach (future evaluation pattern)

Note: TensorFlow, Keras, and MNIST are not currently used in runtime code; they are included here as part of a realistic extension and benchmarking direction.

## Architecture / Workflow

1. Capture frame from webcam.
2. Preprocess frame (BGR to RGB conversion).
3. Run asynchronous face-landmark inference.
4. Compute left-eye and right-eye EAR.
5. Average EAR and compare against drowsiness threshold.
6. Count consecutive low-EAR frames.
7. Trigger alert and show status overlay when threshold window is exceeded.

## Setup and Quick Start

### Prerequisites

- Python 3.10 or newer
- Webcam
- Windows OS (current alert implementation uses winsound)

### Installation

```powershell
git clone https://github.com/<your-username>/drowsiness-detection.git
cd drowsiness-detection
python -m venv .env
.\.env\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Run

```powershell
python main.py
```

## Usage Steps

1. Start the application with python main.py.
2. Sit in front of the webcam with adequate lighting.
3. Watch the live window for EAR and status labels.
4. Simulate prolonged eye closure to verify alert behavior.
5. Press q to exit safely.

## Measurable Outcomes

- Throughput target: configured around 20 FPS capture/write flow in local runs.
- Detection responsiveness: near-immediate status update once consecutive low-EAR condition is met.
- Usability: single-command startup, live on-screen indicator, and audible alert feedback.

Current repository version does not include formal benchmark logs or accuracy metrics on a labeled dataset; adding benchmark scripts is listed in ROADMAP.md.

## Resume-Ready Project Highlights

- Built a real-time drowsiness detection pipeline using MediaPipe face landmarks, OpenCV, and EAR-based fatigue logic.
- Implemented asynchronous inference and thresholded consecutive-frame decisioning to distinguish normal blinks from sustained eye closure.
- Delivered an end-to-end safety-focused prototype with live UI overlay, alert mechanism, and modular Python design for extensibility.

## Future Improvements

- Add calibration mode for user-specific EAR thresholds.
- Add benchmark suite with precision/recall on labeled fatigue events.
- Add cross-platform alerting for Linux and macOS.
- Add lightweight UI layer for settings and sensitivity tuning.
- Evaluate TensorFlow/Keras-based classifier as an alternative to rule-based detection.

## License

MIT License. See LICENSE for details.