import cv2
from ultralytics import YOLO

# Load a pre-trained, lightweight YOLOv8 model
model = YOLO("yolov8n.pt")

# Run inference on an image, video, or webcam stream (0 for webcam)
# It automatically downloads the model file on the first run
results = model.predict(source="0", show=True, conf=0.5)

print("Success! Press 'q' in the window to exit.")
