import unittest
import cv2
from scripts.detector.tensorflow_detector import TensorFlowDetector
from scripts.config.constants import tflite_path, images_path


class Detector(unittest.TestCase):
    def test_detect_cow_banana(self):
        detector = TensorFlowDetector(
            "{}/ssd_mobilenet_v1_1_metadata_1.tflite".format(tflite_path),
            "{}/mscoco_complete_labels".format(tflite_path))
        img = cv2.imread("{}/banana_and_cow.png".format(images_path))
        results = detector.detect(img)
        labels = {d['label'] for d in results}
        self.assertSetEqual(labels, {'cow', 'banana'})


if __name__ == '__main__':
    unittest.main()
