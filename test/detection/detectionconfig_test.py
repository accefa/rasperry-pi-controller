import os
import unittest
import detection.detectionconfig as detectionconfig

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

LINE_Y_NORMAL = 88
LINE_Y_LOW = -1

IMAGE_PATH_NORMAL = 'some/path/to/nowhere'

IMAGE_NAME_NORMAL = 'normal_image.jpeg'

TEST_CONFIG_FILE_PATH = os.path.dirname(__file__) + '/../config_test.json'


class DetectionConfigTest(unittest.TestCase):
    def setUp(self):
        self.detection = detectionconfig.DetectionConfig()
        self.detection.CONFIG_FILE_PATH = TEST_CONFIG_FILE_PATH

    def tearDown(self):
        os.remove(TEST_CONFIG_FILE_PATH)

    def test_set_from_dict_only_quality(self):
        quality_dict = {detectionconfig.QUALITY_KEY: QUALITY_NORMAL}
        self.detection.set_from_dict(quality_dict)
        self.assertEquals(QUALITY_NORMAL, self.detection.quality)

    def test_set_from_dict_only_crop_x(self):
        crop_x_dict = {detectionconfig.CROP_X_KEY: CROP_X_NORMAL}
        self.detection.set_from_dict(crop_x_dict)
        self.assertEquals(CROP_X_NORMAL, self.detection.crop_x)

    def test_set_from_dict_only_contrast(self):
        contrast_dict = {detectionconfig.CONTRAST_KEY: CONTRAST_NORMAL}
        self.detection.set_from_dict(contrast_dict)
        self.assertEquals(CONTRAST_NORMAL, self.detection.contrast)

    def test_set_from_dict_only_greyscale(self):
        greyscale_dict = {detectionconfig.GREYSCALE_KEY: GREYSCALE_NORMAL}
        self.detection.set_from_dict(greyscale_dict)
        self.assertEquals(GREYSCALE_NORMAL, self.detection.greyscale)

    def test_set_from_dict_only_greyscale_threshold(self):
        greyscale_threshold_dict = {detectionconfig.GREYSCALE_THRESHOLD_KEY: GREYSCALE_THRESHOLD_NORMAL}
        self.detection.set_from_dict(greyscale_threshold_dict)
        self.assertEquals(GREYSCALE_THRESHOLD_NORMAL, self.detection.greyscale_threshold)

    def test_set_from_dict_only_line_h(self):
        line_h_dict = {detectionconfig.LINE_H_KEY: LINE_H_NORMAL}
        self.detection.set_from_dict(line_h_dict)
        self.assertEquals(LINE_H_NORMAL, self.detection.line_h)

    def test_set_from_dict_only_line_y(self):
        line_y_dict = {detectionconfig.LINE_Y_KEY: LINE_Y_NORMAL}
        self.detection.set_from_dict(line_y_dict)
        self.assertEquals(LINE_Y_NORMAL, self.detection.line_y)

    def test_set_from_dict_only_image_path(self):
        image_path_dict = {detectionconfig.IMAGE_PATH_KEY: IMAGE_PATH_NORMAL}
        self.detection.set_from_dict(image_path_dict)
        self.assertEquals(IMAGE_PATH_NORMAL, self.detection.image_path)

    def test_set_get_from_dict_all(self):
        set_dict = {
            detectionconfig.QUALITY_KEY: QUALITY_NORMAL,
            detectionconfig.CROP_X_KEY: CROP_X_NORMAL,
            detectionconfig.CONTRAST_KEY: CONTRAST_NORMAL,
            detectionconfig.GREYSCALE_KEY: GREYSCALE_NORMAL,
            detectionconfig.GREYSCALE_THRESHOLD_KEY: GREYSCALE_THRESHOLD_NORMAL,
            detectionconfig.LINE_H_KEY: LINE_H_NORMAL,
            detectionconfig.LINE_Y_KEY: LINE_Y_NORMAL,
            detectionconfig.IMAGE_PATH_KEY: IMAGE_PATH_NORMAL,
            detectionconfig.IMAGE_NAME_KEY: IMAGE_NAME_NORMAL
        }
        self.detection.set_from_dict(set_dict)
        get_dict = self.detection.get_as_dict()
        self.assertEquals(set_dict, get_dict)

    def test_set_get_quality(self):
        self.detection.quality = QUALITY_NORMAL
        self.assertEqual(QUALITY_NORMAL, self.detection.quality)

    def test_set_get_quality_to_high(self):
        self.detection.quality = QUALITY_HIGH
        self.assertEqual(QUALITY_HIGH, self.detection.quality)

    def test_set_get_quality_to_low(self):
        self.detection.quality = QUALITY_LOW
        self.assertEqual(1, self.detection.quality)

    def test_set_get_crop_x(self):
        self.detection.crop_x = CROP_X_NORMAL
        self.assertEqual(CROP_X_NORMAL, self.detection.crop_x)

    def test_set_get_crop_x_to_low(self):
        self.detection.crop_x = CROP_X_LOW
        self.assertEqual(0, self.detection.crop_x)

    def test_set_get_contrast(self):
        self.detection.contrast = CONTRAST_NORMAL
        self.assertEqual(CONTRAST_NORMAL, self.detection.contrast)

    def test_set_get_contrast_to_low(self):
        self.detection.contrast = CONTRAST_LOW
        self.assertEqual(-100, self.detection.contrast)

    def test_set_get_contrast_to_high(self):
        self.detection.contrast = CONTRAST_HIGH
        self.assertEqual(100, self.detection.contrast)

    def test_set_get_greyscale(self):
        self.detection.greyscale = GREYSCALE_NORMAL
        self.assertEqual(GREYSCALE_NORMAL, self.detection.greyscale)

    def test_set_get_greyscale_not_boolean(self):
        self.detection.greyscale = GREYSCALE_INVALID
        self.assertEqual(False, self.detection.greyscale)

    def test_set_get_greyscale_threshold(self):
        self.detection.greyscale_threshold = GREYSCALE_THRESHOLD_NORMAL
        self.assertEqual(GREYSCALE_THRESHOLD_NORMAL, self.detection.greyscale_threshold)

    def test_set_get_greyscale_threshold_to_low(self):
        self.detection.greyscale_threshold = GREYSCALE_THRESHOLD_LOW
        self.assertEqual(0, self.detection.greyscale_threshold)

    def test_set_get_greyscale_threshold_to_high(self):
        self.detection.greyscale_threshold = GREYSCALE_THRESHOLD_HIGH
        self.assertEqual(255, self.detection.greyscale_threshold)

    def test_set_get_line_h(self):
        self.detection.line_h = LINE_H_NORMAL
        self.assertEqual(LINE_H_NORMAL, self.detection.line_h)

    def test_set_get_line_h_to_low(self):
        self.detection.line_h = LINE_H_LOW
        self.assertEqual(1, self.detection.line_h)

    def test_set_get_line_y(self):
        self.detection.line_y = LINE_Y_NORMAL
        self.assertEqual(LINE_Y_NORMAL, self.detection.line_y)

    def test_set_get_line_y_to_low(self):
        self.detection.line_y = LINE_Y_LOW
        self.assertEqual(0, self.detection.line_y)

    def test_set_get_image_path(self):
        self.detection.image_path = IMAGE_PATH_NORMAL
        self.assertEqual(IMAGE_PATH_NORMAL, self.detection.image_path)

    def test_set_get_image_name(self):
        self.detection.image_name = IMAGE_NAME_NORMAL
        self.assertEquals(IMAGE_NAME_NORMAL, self.detection.image_name)


if __name__ == '__main__':
    unittest.main()