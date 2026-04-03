import time
import cv2
import mediapipe as mp
import numpy as np
import winsound
import threading

model_path = r'C:\Users\SREESANKAR\Dev\drowsiness-detection\face_landmarker.task'

#              P1   P2   P3   P4   P5   P6



class DrowsinessDetector():
        def __init__(self, camera):
                self.ear_value = 0.0
                self.LEFT_EYE  = [362, 385, 387, 263, 373, 380]
                self.RIGHT_EYE = [33,  160, 158, 133, 153, 144]

                self.frame_counter = 0
                self.CONSEC_FRAMES = 20
                self.DROWSY_THRESHOLD = 0.23

                self.BaseOptions = mp.tasks.BaseOptions
                self.FaceLandmarker = mp.tasks.vision.FaceLandmarker
                self.FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
                self.FaceLandmarkerResult = mp.tasks.vision.FaceLandmarkerResult
                self.VisionRunningMode = mp.tasks.vision.RunningMode

                self.alarm_on = False

                self.camera = camera

                self.options = self.FaceLandmarkerOptions(base_options=self.BaseOptions(model_asset_path=model_path),
                                        running_mode=self.VisionRunningMode.LIVE_STREAM,
                                        result_callback=self.print_result)
                self.landmarker = mp.tasks.vision.FaceLandmarker.create_from_options(self.options)
        def get_ear(self, landmarks, eye_indices, w, h):
                pts = [(landmarks[i].x * w, landmarks[i].y * h) for i in eye_indices]
                # vertical
                A = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
                B = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))
                # horizontal
                C = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))

                return (A + B) / (2.0 * C)

        def print_result(self, result, output_image, timestamp_ms):
                if not result.face_landmarks:
                        return
                landmarks = result.face_landmarks[0]
                left_ear  = self.get_ear(landmarks, self.LEFT_EYE,  self.camera.width, self.camera.height)
                right_ear = self.get_ear(landmarks, self.RIGHT_EYE, self.camera.width, self.camera.height)
                self.ear_value = (left_ear + right_ear) / 2.0
        

        def beep(self):
                print("BEEP TRIGGERED")
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

        def stop(self):
                self.camera.release()
                self.landmarker.close()


        def run(self):
                while True:
                        frame_timestamp_ms = int(time.perf_counter() * 1000)
                        current_frame = self.camera.read()
                        rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
                        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                        self.landmarker.detect_async(mp_image, frame_timestamp_ms)

                        if self.ear_value < self.DROWSY_THRESHOLD:
                                self.frame_counter += 1
                                print(self.frame_counter)
                        else:
                                self.frame_counter = 0

                        if self.frame_counter >= self.CONSEC_FRAMES:
                                label = "DROWSY"
                                color = (0, 0, 255)

                                if not self.alarm_on:
                                        self.alarm_on = True
                                        threading.Thread(target=self.beep, daemon=True).start()

                        else:
                                label = "Alert"
                                color = (0, 255, 0)
                                self.alarm_on = False

                        cv2.putText(current_frame, label, (15, 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)
                        cv2.putText(current_frame, f"EAR: {self.ear_value:.2f}", (15, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)

                        self.camera.write(current_frame)
                        cv2.imshow('Camera', current_frame)

                        if cv2.waitKey(1) == ord('q'):
                                self.stop()
                                break