import unittest
from detection.Detection import DetectionConfig

class DetectionConfigTest(unittest.TestCase):

    def setUp(self):
        self.detection = DetectionConfig()

    def test_setAndGetQuality(self):
        value = 4
        self.detection.quality = value
        self.assertEqual(value, self.detection.quality);
        
    def test_setAndGetpathSaveImageTo(self):
        value = 10
        self.detection.pathSaveImageTo = value
        self.assertEqual(value, self.detection.pathSaveImageTo);

    def test_setAndGetRoiX(self):
        value = 10
        self.detection.roix = value
        self.assertEqual(value, self.detection.roix);
    
    def test_setAndGetRoiY(self):
        value = 9
        self.detection.roiy = value
        self.assertEqual(value, self.detection.roiy);
    
    def test_setAndGetRoiH(self):
        value = 55
        self.detection.roiH = value
        self.assertEqual(value, self.detection.roiH);
    
    def test_setAndGetRoiW(self):
        value = 66
        self.detection.roiW = value
        self.assertEqual(value, self.detection.roiW);
    
    def test_setAndGetContrast(self):
        value = 66
        self.detection.contrast = value
        self.assertEqual(value, self.detection.contrast);
        
    def test_setAndGetGreyscale(self):
        value = True
        self.detection.greyscale = value
        self.assertEqual(value, self.detection.greyscale);
    
    def test_setAndGetLineH(self):
        value = 66
        self.detection.lineH = value
        self.assertEqual(value, self.detection.lineH);
    
    def test_setAndGetLineY(self):
        value = 66
        self.detection.lineY = value
        self.assertEqual(value, self.detection.lineY);

if __name__ == '__main__':
    unittest.main()