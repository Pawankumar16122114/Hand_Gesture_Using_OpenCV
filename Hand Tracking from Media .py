import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import HandLandmarker
import time
import os

# Change the video file path to your own file
video_path = 'a.mp4'
cap = cv2.VideoCapture(video_path)

# Get video details for the output video
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_path = 'output_video.mp4'
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

model_path = 'hand_landmarker.task'
if not os.path.exists(model_path):
    import urllib.request
    urllib.request.urlretrieve('https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task', model_path)

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
landmarker = HandLandmarker.create_from_options(options)

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    if not success:
        break  # Break the loop if the video ends or there is an issue reading the video

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    result = landmarker.detect(mp_image)

    if result.hand_landmarks:
        connections = [
            (0,1),(1,2),(2,3),(3,4),
            (0,5),(5,6),(6,7),(7,8),
            (5,9),(9,10),(10,11),(11,12),
            (9,13),(13,14),(14,15),(15,16),
            (13,17),(17,18),(18,19),(19,20),
            (0,17)
        ]

        for hand_landmarks in result.hand_landmarks:
            pts = []
            h, w, c = img.shape
            for id, landmark in enumerate(hand_landmarks):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                pts.append((cx, cy))
                cv2.circle(img, (cx, cy), 4, (0, 255, 0), cv2.FILLED)
                if id == 0:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            for (start_i, end_i) in connections:
                if start_i < len(pts) and end_i < len(pts):
                    cv2.line(img, pts[start_i], pts[end_i], (255, 0, 0), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    
    # Write the frame to the output video
    out.write(img)

    # Break the loop and close the window when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file, output video, and close the window
landmarker.close()
cap.release()
out.release()
cv2.destroyAllWindows()