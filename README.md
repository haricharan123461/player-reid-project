Player Re-Identification and Tracking
This project performs player detection, tracking, and Re-ID (Re-Identification) using a combination of YOLOv8 and Deep SORT. You provide a sports match video as input, and the system tracks individual players across frames and re-identifies them consistently using bounding boxes.

📦 Dependencies
To ensure smooth execution, install the following:

Python 3.8 or later

OpenCV (opencv-python)

PyTorch

Ultralytics YOLOv8 (ultralytics)

Deep SORT Realtime (deep_sort_realtime)

NumPy

tqdm

Install everything using:

bash
Copy
Edit
pip install -r requirements.txt
⚙️ Setup Instructions
Clone or download this repository to your local machine.

Place your input video in the project directory and name it (e.g., input.mp4).

Run the script using:

bash
Copy
Edit
python main.py
(Make sure your video path and file name are correctly referenced in main.py.)

Output: A processed video is generated with bounding boxes tracking individual players (default name: reid_output.mp4). It will be saved in the output folder created automatically.

📌 Notes
The video should contain distinguishable players and consistent lighting for best tracking performance.

Ensure CUDA is available for faster performance, or fallback to CPU (slower).

Report (Methodology & Observations)
🎯 Objective
Build an AI-powered video analysis system capable of tracking players across frames and assigning consistent IDs using re-identification logic.

🧠 Approach & Methodology
Used YOLOv8 for fast and accurate object detection (players).

Integrated Deep SORT for robust real-time multi-object tracking with re-ID capability.

Frames are processed sequentially, and tracked players are assigned persistent IDs shown with bounding boxes.

The processed frames are compiled back into a final output video.

🔍 Techniques Tried & Outcomes
YOLOv8 outperformed other detectors (like YOLOv5 or Haar cascades) in both speed and accuracy.

Deep SORT provided reliable ID continuity even with partial occlusions and fast motion.

⚠️ Challenges Faced
Bounding boxes not appearing: Often due to incorrect video path or failure to load the model properly.

Frame skipping or lag: Happens when GPU is not available; fallback to CPU is significantly slower.

Players not detected: If the model’s confidence is low or the video quality is poor.

⏳ Incomplete / Next Steps
Current system only uses default YOLOv8 weights. For better accuracy, custom training on player datasets would be ideal.

Future additions could include: player statistics, heatmaps, pose estimation, or event detection (e.g., goals or fouls).
