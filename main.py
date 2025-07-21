# player_reid_project/main.py

import cv2
import torch
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import os
from tqdm import tqdm

# ----------------------
# Setup
# ----------------------
VIDEO_PATH = "video/15sec_input_720p.mp4"
MODEL_PATH = "yolov11_model.pt"
OUTPUT_PATH = "output/reid_output.mp4"
CONFIDENCE_THRESHOLD = 0.4

# Create output dir if not exists
os.makedirs("output", exist_ok=True)

# ----------------------
# Load YOLOv11 model
# ----------------------
model = YOLO(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# ----------------------
# Load Video
# ----------------------
cap = cv2.VideoCapture(VIDEO_PATH)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Save video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

# ----------------------
# Load Deep SORT Tracker
# ----------------------
tracker = DeepSort(max_age=30)

# ----------------------
# Process Each Frame
# ----------------------
print("Processing video...")

for _ in tqdm(range(frame_count)):
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame, verbose=False)[0]
    detections = []

    for det in results.boxes:
        cls_id = int(det.cls[0].item())
        conf = det.conf[0].item()

        if conf < CONFIDENCE_THRESHOLD:
            continue

        # Class 0 assumed to be player
        if cls_id == 0:
            x1, y1, x2, y2 = det.xyxy[0].cpu().numpy()
            detections.append([[x1, y1, x2 - x1, y2 - y1], conf, 'player'])

    # Run Deep SORT tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw results
    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"Player {track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    out.write(frame)

cap.release()
out.release()
print("Saved re-ID output to:", OUTPUT_PATH)
