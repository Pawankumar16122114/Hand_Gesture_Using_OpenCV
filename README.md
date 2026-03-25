🖐️ Hand Tracking Using OpenCV & MediaPipe
<p align="center"> <img src="https://readme-typing-svg.herokuapp.com?size=25&duration=3000&color=00F7FF&center=true&vCenter=true&width=600&lines=Real-Time+Hand+Tracking+System;Powered+by+OpenCV+%2B+MediaPipe;Detects+21+Hand+Landmarks;Build+Futuristic+Vision+Apps+🚀" /> </p>
🚀 Project Overview

This project is a real-time hand tracking system built using OpenCV and MediaPipe. It detects and visualizes 21 hand landmarks including fingers and palm with high accuracy.

🎯 Designed for:

Computer Vision Projects
Gesture Recognition Systems
AI/ML Portfolio Enhancement
AR/VR Interaction Ideas
✨ Features

✅ Real-time hand detection
✅ 21 landmark tracking (fingers + palm)
✅ Smooth visualization with connections
✅ FPS display for performance tracking
✅ Works with webcam & video files
✅ Pause (P) and Quit (Q) controls
✅ Prints landmark coordinates (x, y)

🧠 How It Works
MediaPipe detects hand landmarks using a pre-trained ML model
OpenCV captures frames from webcam/video
Each frame is processed:
🟢 Green dots → Landmarks
🔵 Blue lines → Finger connections
🟣 Magenta dot → Wrist point
FPS is calculated and displayed
📸 Output Preview
🔹 Hand Detection with Skeleton Tracking
![Hand Tracking 1](./assets/hand1.png)

👉 Shows full hand skeleton with accurate landmark connections

🔹 Palm Detection with High Accuracy
![Hand Tracking 2](./assets/hand2.png)

👉 Demonstrates clear palm detection and improved alignment

🔹 Minimal Detection Mode
![Hand Tracking 3](./assets/hand3.png)

👉 Displays only essential tracking (wrist focus)

🔹 Low-Light Detection
![Hand Tracking 4](./assets/hand4.png)

👉 Shows system performance under low lighting conditions

🎮 Demo Animation (Optional but Powerful)
![Demo](https://raw.githubusercontent.com/your-username/your-repo/main/demo.gif)

💡 Tip: Record your screen and convert to GIF → boosts portfolio impact 🔥

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/hand-tracking-opencv.git
cd hand-tracking-opencv
2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ How to Run
🎥 Webcam Mode
python app.py
📁 Video Mode
python "Hand Tracking from Media .py"

📌 Update video path inside code if needed

📦 Requirements
Python 3.7+ (Recommended: 3.11)
OpenCV 4.13+
MediaPipe 0.10.33+

Install manually if needed:

pip install opencv-python mediapipe
🛠️ Project Structure
<br>
📦 hand-tracking-opencv
 ┣ 📜 app.py
 ┣ 📜 Hand Tracking from Media.py
 ┣ 📜 requirements.txt
 ┣ 📂 assets
 ┃ ┣ hand1.png
 ┃ ┣ hand2.png
 ┃ ┣ hand3.png
 ┃ ┗ hand4.png
 ┗ 📜 README.md
 <br>
⚡ Performance
Condition	Accuracy
Good Lighting	⭐⭐⭐⭐⭐
Medium Lighting	⭐⭐⭐⭐
Low Lighting	⭐⭐⭐
🧪 Troubleshooting

❌ Only one dot showing?
✔️ Ensure loop draws all 21 landmarks

❌ Camera not opening?
✔️ Check webcam permissions

❌ Low accuracy?
✔️ Improve lighting conditions

💡 Future Enhancements

🚀 Gesture recognition (thumbs up, swipe, etc.)
🎮 Cursor control using hand
🕶️ AR/VR interaction system
🤖 AI-based sign language detection

🏆 Why This Project Stands Out

🔥 Real-time computer vision
🔥 Industry-level libraries (MediaPipe)
🔥 Expandable to advanced AI systems
🔥 Perfect for Top 1% Portfolio Projects

🤝 Contributing

Pull requests are welcome!
If you have ideas → fork & improve 🚀

📬 Connect With Me
<p align="center"> <a href="https://github.com/your-username"> <img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github"> </a> </p>
⭐ Give a Star

If you like this project:
👉 ⭐ Star this repo
👉 🔁 Share with others
