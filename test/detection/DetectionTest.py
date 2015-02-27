import unittest
from detection.Detection import Detection

class DetectionTest(unittest.TestCase):

    def setUp(self):
        self.detection = Detection()

    def test_setAndGetQuality(self):
        value = 4
        self.detection.setQuality(value)
        self.assertEqual(value, self.detection.getQuality());

    def test_setAndGetRoiX(self):
        value = 10
        self.detection.setRoiX(value)
        self.assertEqual(value, self.detection.getRoiX());

if __name__ == '__main__':
    unittest.main()