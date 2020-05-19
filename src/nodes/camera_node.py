import cv2
import numpy as np
import camera_node_interface


class Camera(camera_node_interface.CameraNodeInterface):
    def __init__(self, cam_id: int):
        """
        Video dimensions and camera ID defined at construction.
        """
        self.set_camera_id(cam_id)

    def set_camera_id(self, cam_id: int):
        self.camera_id = cam_id
        self.cap = cv2.VideoCapture(self.camera_id)

    def frameRGB(self) -> np.ndarray:
        """
        Return the newest frame from the camera as a 3 dimensional numpy array.
            """
        ret, frame = self.cap.read()
        # if ret is False, no image was captured and black image is returned
        if ret == False:
            return np.zeros(shape=(300, 300, 3)).astype(np.uint8)

        return frame
