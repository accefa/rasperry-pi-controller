import os
import unittest
from detection.detectionconfig import DetectionConfig


class DetectionConfigTest(unittest.TestCase):
    QUALITY_NORMAL = 4
    QUALITY_HIGH = 100
    QUALITY_LOW = 0

    CROP_X_NORMAL = 10
    CROP_X_LOW = -1

    CONTRAST_NORMAL = 50
    CONTRAST_HIGH = 101
    CONTRAST_LOW = -101

    GREYSCALE_NORMAL = False
    GREYSCALE_INVALID = "I am not a boolean"

    GREYSCALE_THRESHOLD_NORMAL = 77
    GREYSCALE_THRESHOLD_HIGH = 256
    GREYSCALE_THRESHOLD_LOW = -1

    LINE_H_NORMAL = 66
    LINE_H_LOW = 0

    LINE_Y_NORMAL =88
    LINE_Y_LOW = -1

    IMAGE_PATH_NORMAL = 'some/path/to/nowhere'
    TEST_CONFIG_FILE_PATH = os.path.dirname(__file__) + '/../config_test.json'

    def setUp(self):
        self.detection = DetectionConfig()
        self.detection.CONFIG_FILE_PATH = self.TEST_CONFIG_FILE_PATH

    def tearDown(self):
        os.remove(self.TEST_CONFIG_FILE_PATH)

    def test_set_from_dict_only_quality(self):
        quality_dict = {DetectionConfig._QUALITY_KEY: self.QUALITY_NORMAL}
        self.detection.set_from_dict(quality_dict)
        self.assertEquals(self.QUALITY_NORMAL, self.detection.quality)

    def test_set_from_dict_only_crop_x(self):
        crop_x_dict = {DetectionConfig._CROP_X_KEY: self.CROP_X_NORMAL}
        self.detection.set_from_dict(crop_x_dict)
        self.assertEquals(self.CROP_X_NORMAL, self.detection.crop_x)

    def test_set_from_dict_only_contrast(self):
        contrast_dict = {DetectionConfig._CONTRAST_KEY: self.CONTRAST_NORMAL}
        self.detection.set_from_dict(contrast_dict)
        self.assertEquals(self.CONTRAST_NORMAL, self.detection.contrast)

    def test_set_from_dict_only_greyscale(self):
        greyscale_dict = {DetectionConfig._GREYSCALE_KEY: self.GREYSCALE_NORMAL}
        self.detection.set_from_dict(greyscale_dict)
        self.assertEquals(self.GREYSCALE_NORMAL, self.detection.greyscale)

    def test_set_from_dict_only_greyscale_threshold(self):
        greyscale_threshold_dict = {DetectionConfig._GREYSCALE_THRESHOLD_KEY: self.GREYSCALE_THRESHOLD_NORMAL}
        self.detection.set_from_dict(greyscale_threshold_dict)
        self.assertEquals(self.GREYSCALE_THRESHOLD_NORMAL, self.detection.greyscale_threshold)

    def test_set_from_dict_only_line_h(self):
        line_h_dict = {DetectionConfig._LINE_H_KEY: self.LINE_H_NORMAL}
        self.detection.set_from_dict(line_h_dict)
        self.assertEquals(self.LINE_H_NORMAL, self.detection.line_h)

    def test_set_from_dict_only_line_y(self):
        line_y_dict = {DetectionConfig._LINE_Y_KEY: self.LINE_Y_NORMAL}
        self.detection.set_from_dict(line_y_dict)
        self.assertEquals(self.LINE_Y_NORMAL, self.detection.line_y)

    def test_set_from_dict_only_image_path(self):
        image_path_dict = {DetectionConfig._IMAGE_PATH_KEY: self.IMAGE_PATH_NORMAL}
        self.detection.set_from_dict(image_path_dict)
        self.assertEquals(self.IMAGE_PATH_NORMAL, self.detection.image_path)

    def test_set_get_from_dict_all(self):
        set_dict = {
            DetectionConfig._QUALITY_KEY: self.QUALITY_NORMAL,
            DetectionConfig._CROP_X_KEY: self.CROP_X_NORMAL,
            DetectionConfig._CONTRAST_KEY: self.CONTRAST_NORMAL,
            DetectionConfig._GREYSCALE_KEY: self.GREYSCALE_NORMAL,
            DetectionConfig._GREYSCALE_THRESHOLD_KEY: self.GREYSCALE_THRESHOLD_NORMAL,
            DetectionConfig._LINE_H_KEY: self.LINE_H_NORMAL,
            DetectionConfig._LINE_Y_KEY: self.LINE_Y_NORMAL,
            DetectionConfig._IMAGE_PATH_KEY: self.IMAGE_PATH_NORMAL
        }
        self.detection.set_from_dict(set_dict)
        get_dict = self.detection.get_as_dict()
        self.assertEquals(set_dict, get_dict)

    def test_set_get_quality(self):
        self.detection.quality = self.QUALITY_NORMAL
        self.assertEqual(self.QUALITY_NORMAL, self.detection.quality)

    def test_set_get_quality_to_high(self):
        self.detection.quality = self.QUALITY_HIGH
        self.assertEqual(self.QUALITY_HIGH, self.detection.quality)

    def test_set_get_quality_to_low(self):
        self.detection.quality = self.QUALITY_LOW
        self.assertEqual(1, self.detection.quality)

    def test_set_get_crop_x(self):
        self.detection.crop_x = self.CROP_X_NORMAL
        self.assertEqual(self.CROP_X_NORMAL, self.detection.crop_x)

    def test_set_get_crop_x_to_low(self):
        self.detection.crop_x = self.CROP_X_LOW
        self.assertEqual(0, self.detection.crop_x)

    def test_set_get_contrast(self):
        self.detection.contrast = self.CONTRAST_NORMAL
        self.assertEqual(self.CONTRAST_NORMAL, self.detection.contrast)

    def test_set_get_contrast_to_low(self):
        self.detection.contrast = self.CONTRAST_LOW
        self.assertEqual(-100, self.detection.contrast)

    def test_set_get_contrast_to_high(self):
        self.detection.contrast = self.CONTRAST_HIGH
        self.assertEqual(100, self.detection.contrast)

    def test_set_get_greyscale(self):
        self.detection.greyscale = self.GREYSCALE_NORMAL
        self.assertEqual(self.GREYSCALE_NORMAL, self.detection.greyscale)

    def test_set_get_greyscale_not_boolean(self):
        self.detection.greyscale = self.GREYSCALE_INVALID
        self.assertEqual(False, self.detection.greyscale)

    def test_set_get_greyscale_threshold(self):
        self.detection.greyscale_threshold = self.GREYSCALE_THRESHOLD_NORMAL
        self.assertEqual(self.GREYSCALE_THRESHOLD_NORMAL, self.detection.greyscale_threshold)

    def test_set_get_greyscale_threshold_to_low(self):
        self.detection.greyscale_threshold = self.GREYSCALE_THRESHOLD_LOW
        self.assertEqual(0, self.detection.greyscale_threshold)

    def test_set_get_greyscale_threshold_to_high(self):
        self.detection.greyscale_threshold = self.GREYSCALE_THRESHOLD_HIGH
        self.assertEqual(255, self.detection.greyscale_threshold)

    def test_set_get_line_h(self):
        self.detection.line_h = self.LINE_H_NORMAL
        self.assertEqual(self.LINE_H_NORMAL, self.detection.line_h)

    def test_set_get_line_h_to_low(self):
        self.detection.line_h = self.LINE_H_LOW
        self.assertEqual(1, self.detection.line_h)

    def test_set_get_line_y(self):
        self.detection.line_y = self.LINE_Y_NORMAL
        self.assertEqual(self.LINE_Y_NORMAL, self.detection.line_y)

    def test_set_get_line_y_to_low(self):
        self.detection.line_y = self.LINE_Y_LOW
        self.assertEqual(0, self.detection.line_y)

    def test_set_get_image_path(self):
        self.detection.image_path = self.IMAGE_PATH_NORMAL
        self.assertEqual(self.IMAGE_PATH_NORMAL, self.detection.image_path)


if __name__ == '__main__':
    unittest.main()