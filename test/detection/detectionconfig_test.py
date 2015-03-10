import unittest
from detection.detectionconfig import DetectionConfig


class DetectionConfigTest(unittest.TestCase):
    def setUp(self):
        self.detection = DetectionConfig()

    def test_setAndGetQuality(self):
        value = 4
        self.detection.quality = value
        self.assertEqual(value, self.detection.quality)

    def test_setAndGetQualityToHigh(self):
        value = 101
        self.detection.quality = value
        self.assertEqual(100, self.detection.quality)

    def test_setAndGetQualityToLow(self):
        value = 0
        self.detection.quality = value
        self.assertEqual(1, self.detection.quality)

    def test_setAndGetpathSaveImageTo(self):
        value = 10
        self.detection.pathSaveImageTo = value
        self.assertEqual(value, self.detection.pathSaveImageTo)

    def test_setAndGetCropX(self):
        value = 10
        self.detection.cropX = value
        self.assertEqual(value, self.detection.cropX)

    def test_setAndGetCropXToLow(self):
        value = -1
        self.detection.cropX = value
        self.assertEqual(0, self.detection.cropX)

    def test_setAndGetContrast(self):
        value = 66
        self.detection.contrast = value
        self.assertEqual(value, self.detection.contrast)

    def test_setAndGetContrastToLow(self):
        value = -101
        self.detection.contrast = value
        self.assertEqual(-100, self.detection.contrast)

    def test_setAndGetContrastToHigh(self):
        value = 101
        self.detection.contrast = value
        self.assertEqual(100, self.detection.contrast)

    def test_setAndGetGreyscale(self):
        value = True
        self.detection.greyscale = value
        self.assertEqual(value, self.detection.greyscale)

    def test_setAndGetGreyscaleNotBoolean(self):
        value = "i am not a boolean"
        self.detection.greyscale = value
        self.assertEqual(False, self.detection.greyscale)

    def test_setAndGetLineH(self):
        value = 66
        self.detection.lineH = value
        self.assertEqual(value, self.detection.lineH)

    def test_setAndGetLineHToLow(self):
        value = 0
        self.detection.lineH = value
        self.assertEqual(1, self.detection.lineH)

    def test_setAndGetLineY(self):
        value = 66
        self.detection.lineY = value
        self.assertEqual(value, self.detection.lineY)

    def test_setAndGetLineYToLow(self):
        value = -1
        self.detection.lineY = value
        self.assertEqual(0, self.detection.lineY)

    def test_setAndGetGreyscaleTreshold(self):
        value = 77
        self.detection.greyscaleThreshold = value
        self.assertEqual(value, self.detection.greyscaleThreshold)

    def test_setAndGetGreyscaleTresholdToLow(self):
        value = -1
        self.detection.greyscaleThreshold = value
        self.assertEqual(0, self.detection.greyscaleThreshold)

    def test_setAndGetGreyscaleTresholdToHigh(self):
        value = 256
        self.detection.greyscaleThreshold = value
        self.assertEqual(255, self.detection.greyscaleThreshold)


if __name__ == '__main__':
    unittest.main()