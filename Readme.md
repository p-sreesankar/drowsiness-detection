<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:1f2937,100:2563eb&text=Drowsiness%20Detection%20System&fontColor=ffffff&fontSize=42&fontAlignY=40&desc=Real-time%20Driver%20Fatigue%20Monitoring%20with%20Python&descAlignY=62&animation=fadeIn" alt="header"/>
</p>

<p align="center">
  <a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white"></a>
  <a href="#"><img alt="Platform" src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white"></a>
  <a href="#"><img alt="Status" src="https://img.shields.io/badge/Status-Active-success"></a>
  <a href="#"><img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white"></a>
</p>

<p align="center">
  <b>Stay awake. Stay safe.</b><br/>
  A professional and practical real-time drowsiness alert system using webcam input and Python.
</p>

---

## 🎬 Demo

> Put your GIF at `assets/demo.gif` and GitHub will show it here automatically.

<p align="center">
  <img src="assets/demo.gif" alt="Drowsiness Detection Demo" width="920"/>
</p>

---

## ✨ Highlights

- 📹 Real-time webcam monitoring  
- 🧠 Drowsiness detection pipeline  
- 🔔 Audible startup alert (`winsound`)  
- 🛡️ Safe shutdown flow with `try/finally`  
- 🧩 Clean modular design (`Camera` + `DrowsinessDetector`)  

---

## ⚙️ How the current code works

From your `main.py`:

1. Imports:
   - `DrowsinessDetector` from `detect_drowsiness`
   - `Camera` from `load_video`
   - `winsound` for Windows beep
2. Plays startup beep: `winsound.Beep(1000, 1000)`
3. Creates `camera` and `detector`
4. Runs detector loop with `detector.run()`
5. Always calls `detector.stop()` in `finally`

---

## 📁 Project Structure

```text
drowsiness-detection/
├── main.py
├── detect_drowsiness.py
├── load_video.py
├── assets/
│   └── demo.gif
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1) Clone

```bash
git clone https://github.com/<your-username>/drowsiness-detection.git
cd drowsiness-detection
```

### 2) Create virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies

```powershell
pip install -r requirements.txt
```

### 4) Run

```powershell
python main.py
```

---



---

## 🧪 Pro Tips

- Use good lighting for better face/eye detection.
- Keep camera at eye level.
- If webcam is busy, close other apps using the camera.

---

## 🛣️ Roadmap

- [ ] Cross-platform audio alerts (Linux/macOS fallback)
- [ ] Sensitivity tuning options
- [ ] Alert log export (CSV/JSON)
- [ ] On-screen confidence metrics
- [ ] Packaging + release build
- [ ] EAR smoothing
- [ ] FPS-based timing instead of frame counting
- [ ] Blink duration detection
- [ ] PERCLOS
- [ ] Head nodding
- [ ] Yawning
- [ ] Continuous alarm loop
- [ ] Logging fatigue events
- [ ] GUI dashboard

---

## 🤝 Contributing

PRs and issues are welcome.  
Suggestions for model quality, UX, and performance are encouraged.

---

## 📄 License

Add a `LICENSE` file (MIT is a common choice).

---

<p align="center">
  <sub>Built with focus, caffeine, and a mission for safety.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:2563eb,100:1f2937" alt="footer"/>
</p>