import cv2
import mediapipe as mp
import time
import pyautogui as pag

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
time.sleep(3)
cap = cv2.VideoCapture('videos/nick.mp4')

while True:
    try:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        try:
            landmarks = results.pose_landmarks.landmark
        except:
            pass
        h, w, c = img.shape
        xl_hip, yl_hip = int(landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x *w), int(landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y * h)
        xr_hip, yr_hip = int(landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].x *w), int(landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].y * h)
        x_hip = (xl_hip + xr_hip)/2
        y_hip = (yl_hip + yr_hip)/2
    
        pag.dragTo(x_hip, y_hip, 0.1, button='left')
        pag.press('s')
        pag.keyDown('alt')
        pag.keyDown('+')
        pag.press('.')
        pag.keyUp('+')
        pag.keyUp('alt')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception:
        break