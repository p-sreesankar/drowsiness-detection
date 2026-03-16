import cv2

class Camera:
    def __init__(self, source=0, output_file='output.mp4', fps=20.0):
        self.cam = cv2.VideoCapture(source)
        self.width  = int(self.cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame = None
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(output_file, fourcc, fps, (self.width, self.height))

    def read(self):
        ret, frame = self.cam.read()
        if not ret:
            return None
        return frame

    def write(self, frame):
        self.out.write(frame)

    def release(self):
        self.cam.release()
        self.out.release()
        cv2.destroyAllWindows()
