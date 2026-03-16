from detect_drowsiness import DrowsinessDetector
from load_video import Camera
import winsound

winsound.Beep(1000, 1000)
if __name__ == "__main__":
    camera = Camera()
    detector = DrowsinessDetector(camera)
    try:
        detector.run()
    finally:
        detector.stop() 