import json
import unittest

from paste.fixture import TestApp

from main import app
import config.detectionconfig as detectionconfig


class CameraTest(unittest.TestCase):
    def __init__(self, method_name):
        unittest.TestCase.__init__(self, method_name)
        self._validJSON = json.dumps({'contrast': 10})
        self._invalidJSON = 'No JSON!'

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_camera_get(self):
        request = self.testApp.get('/camera')
        self.assertEquals(request.status, 200)
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        request.mustcontain(
            detectionconfig.QUALITY_KEY,
            detectionconfig.CROP_X_KEY,
            detectionconfig.CONTRAST_KEY,
            detectionconfig.GREYSCALE_KEY,
            detectionconfig.GREYSCALE_THRESHOLD_KEY,
            detectionconfig.LINE_H_KEY,
            detectionconfig.LINE_Y_KEY,
            detectionconfig.IMAGE_PATH_KEY
        )

    def test_camera_put_invalid_json(self):
        request = self.testApp.put('/camera', self._invalidJSON, expect_errors=True)
        self.assertEquals(request.status, 406)

    def test_camera_put_json(self):
        request = self.testApp.put('/camera', self._validJSON)
        self.assertEquals(request.status, 200)
        self.assertEquals(request.header_dict['content-type'], 'text/json')


if __name__ == "__main__":
    unittest.main()