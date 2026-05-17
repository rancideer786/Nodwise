# NODWISE

# NODWISE: A Smart ML Framework for Continuous Head Movement Awareness

NODWISE is a real-time posture monitoring and head movement awareness system developed using Computer Vision and Machine Learning techniques. The system continuously monitors neck posture and head movement using a webcam and provides alerts whenever poor posture or prolonged static posture is detected.

The project is designed to support ergonomic health and reduce neck strain caused by prolonged screen usage.

---

# Features

## Real-Time Posture Monitoring
- Live webcam-based monitoring
- Continuous posture tracking
- Real-time head movement analysis

## Neck Angle Detection
- Detects forward head posture
- Calculates neck alignment angle
- Displays live angle measurements

## Static Posture Detection
- Detects prolonged inactivity
- Tracks neck movement over time
- Generates movement reminders

## Smart Alert System
- Poor posture alerts
- Static posture alerts
- On-screen notifications

## Research Graph Visualization
- Accuracy graph
- Precision graph
- Recall graph
- F1-score graph
- FPS graph
- User improvement graph

## Dashboard UI
- User-friendly interface
- Monitoring controls
- Graph visualization controls

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam and image processing |
| MediaPipe | Pose estimation |
| NumPy | Mathematical operations |
| Matplotlib | Graph generation |
| CustomTkinter | Dashboard UI |
| Pandas | Data handling |
| Pygame | Alert system |

---

# Project Structure

```text
NODWISE/
│
├── app.py
├── requirements.txt
├── README.md
│
├── core/
│   ├── detector.py
│   ├── angle_calculator.py
│   ├── movement_tracker.py
│   ├── posture_classifier.py
│   └── alerts.py
│
├── gui/
│   ├── dashboard.py
│   └── styles.py
│
├── graphs/
│   ├── generate_graphs.py
│   ├── accuracy_graph.png
│   ├── precision_graph.png
│   ├── recall_graph.png
│   ├── f1_graph.png
│   ├── fps_graph.png
│   └── user_improvement.png
│
├── data/
│   ├── posture_logs.csv
│   └── results.csv
│
├── assets/
│   ├── logo.png
│   ├── alert.wav
│   └── background.png
│
└── screenshots/
    ├── dashboard.png
    └── detection.png