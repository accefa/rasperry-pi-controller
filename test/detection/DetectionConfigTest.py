import unittest
from detection.Detection import DetectionConfig

class DetectionConfigTest(unittest.TestCase):

    def setUp(self):
        self.detection = DetectionConfig()

    def test_setAndGetQuality(self):
        value = 4
        self.detection.quality = value
        self.assertEqual(value, self.detection.quality);
        
    def test_setAndGetQualityToHigh(self):
        value = 101
        self.detection.quality = value
        self.assertEqual(100, self.detection.quality);
    
    def test_setAndGetQualityToLow(self):
        value = 0
        self.detection.quality = value
        self.assertEqual(1, self.detection.quality);
        
    def test_setAndGetpathSaveImageTo(self):
        value = 10
        self.detection.pathSaveImageTo = value
        self.assertEqual(value, self.detection.pathSaveImageTo);

    def test_setAndGetRoiX(self):
        value = 10
        self.detection.roiX = value
        self.assertEqual(value, self.detection.roiX);
        
    def test_setAndGetRoiXToLow(self):
        value = -1
        self.detection.roiX = value
        self.assertEqual(0, self.detection.roiX);
    
    def test_setAndGetRoiY(self):
        value = 9
        self.detection.roiY = value
        self.assertEqual(value, self.detection.roiY);
        
    def test_setAndGetRoiYToLow(self):
        value = -1
        self.detection.roiY = value
        self.assertEqual(0, self.detection.roiY);
    
    def test_setAndGetRoiH(self):
        value = 55
        self.detection.roiH = value
        self.assertEqual(value, self.detection.roiH);
    
    def test_setAndGetRoiHToLow(self):
        value = 0
        self.detection.roiH = value
        self.assertEqual(1, self.detection.roiH);
    
    def test_setAndGetRoiW(self):
        value = 66
        self.detection.roiW = value
        self.assertEqual(value, self.detection.roiW);
    
    def test_setAndGetRoiWToLow(self):
        value = 0
        self.detection.roiW = value
        self.assertEqual(1, self.detection.roiW);
    
    def test_setAndGetContrast(self):
        value = 66
        self.detection.contrast = value
        self.assertEqual(value, self.detection.contrast);
        
    def test_setAndGetContrastToLow(self):
        value = -101
        self.detection.contrast = value
        self.assertEqual(-100, self.detection.contrast);
        
    def test_setAndGetContrastToHigh(self):
        value = 101
        self.detection.contrast = value
        self.assertEqual(100, self.detection.contrast);
        
    def test_setAndGetGreyscale(self):
        value = True
        self.detection.greyscale = value
        self.assertEqual(value, self.detection.greyscale);
    
    def test_setAndGetGreyscaleNotBoolean(self):
        value = "i am not a boolean"
        self.detection.greyscale = value
        self.assertEqual(False, self.detection.greyscale);
    
    def test_setAndGetLineH(self):
        value = 66
        self.detection.lineH = value
        self.assertEqual(value, self.detection.lineH);
        
    def test_setAndGetLineHToLow(self):
        value = 0
        self.detection.lineH = value
        self.assertEqual(1, self.detection.lineH);
    
    def test_setAndGetLineY(self):
        value = 66
        self.detection.lineY = value
        self.assertEqual(value, self.detection.lineY);
        
    def test_setAndGetLineYToLow(self):
        value = -1
        self.detection.lineY = value
        self.assertEqual(0, self.detection.lineY);

if __name__ == '__main__':
    unittest.main()