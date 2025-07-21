🎯 Player Re-Identification and Tracking
This project enables automatic player detection, tracking, and re-identification in sports videos using YOLOv8 for object detection and Deep SORT for multi-object tracking. The system processes a given match video and visually annotates each player with consistent ID-based bounding boxes throughout the video.

📦 Dependencies
To run the project smoothly, make sure the following libraries and tools are installed:

Python 3.8+

OpenCV

PyTorch

Ultralytics (YOLOv8)

Deep SORT Realtime

NumPy

tqdm

Install dependencies using the provided requirements.txt file.

⚙️ Setup Instructions
Clone or download the project repository to your local system.

Place your input video file (e.g., a football or basketball match) in the root directory of the project.

Ensure the file name is correctly referenced in the script (e.g., main.py) before execution.

Run the main script to start the process.

Once the video is processed, a new output video will be generated with bounding boxes consistently tracking each player. The output is saved automatically in the output folder.

📌 Important Notes
Use high-quality, well-lit videos with distinguishable players for best results.

CUDA-enabled GPU is recommended for faster processing; if not available, the system will use CPU (which is slower).

Ensure model weights are downloaded correctly when using YOLOv8 for the first time.

📄 Report: Methodology & Observations
🎯 Objective
The goal is to build an AI-based system capable of tracking players and maintaining their identity across frames, even with fast movement, occlusion, or camera panning.

🧠 Approach & Methodology
YOLOv8 is used for detecting players in each frame due to its superior accuracy and speed.

Deep SORT assigns a unique ID to each player and maintains it across the video using appearance features and motion prediction.

Each video frame is processed to draw bounding boxes with player IDs.

All frames are finally compiled back into a single annotated output video.

🔍 Techniques Tried & Their Outcomes
Compared YOLOv8 with earlier detectors like YOLOv5 and Haar cascades; YOLOv8 consistently showed higher frame rate and precision.

Deep SORT’s re-ID mechanism worked well even under camera movement, occlusion, or overlapping players.

Confidence thresholds and NMS (non-max suppression) settings were adjusted to reduce false positives.

⚠️ Challenges Encountered
Bounding boxes not visible: Usually caused by incorrect video path or missing model weights.

Slow frame rate: On systems without GPU acceleration, CPU fallback results in significant delays.

Missed detections: Poor lighting or low resolution can cause YOLO to miss players or misidentify objects.

⏳ Incomplete Tasks / Future Work
The current version uses pre-trained YOLOv8 weights. Custom training on domain-specific player data could significantly boost accuracy.

Potential extensions:

Pose Estimation

Player Heatmaps

Event Detection (e.g., goals, offsides)

Player Statistics Overlay

Consider implementing GUI-based video upload and real-time processing dashboard in future iterations.

