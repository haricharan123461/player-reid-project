## ⚙️ Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt

pip install ultralytics opencv-python torch torchvision deep_sort_realtime


🧠 Models Used
YOLOv8 (via Ultralytics) – for player detection.

Deep SORT – for re-identification and consistent tracking.

🚀 How to Run
Clone the repo / move into folder:

bash
Copy
Edit
cd player-reid-project
Ensure input video exists in input/input.mp4.

Run the main code:

bash
Copy
Edit
python main.py
Output will be saved to:

bash
Copy
Edit
output/reid_output.mp4
🧪 Optional: Check OpenCV installation
bash
Copy
Edit
python
>>> import cv2
>>> print(cv2.__version__)
📌 Notes
If using a different video, update the path in main.py:

python
Copy
Edit
input_path = 'input/your_video.mp4'
Output directory will be auto-created if not present.
