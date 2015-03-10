import json
from paste.fixture import TestApp
import unittest
from webserver.main import app
from webserver.resource.camera import CONFIG_FILE_PATH


class CameraTest(unittest.TestCase):
    def __init__(self, method_name):
        unittest.TestCase.__init__(self, method_name)
        self._validJSON = json.dumps({'contrast': 10})
        self._invalidJSON = 'No JSON!'

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_camera_get(self):
        self.write_valid_json_to_config()
        r = self.testApp.get('/camera')
        self.assertEquals(r.status, 200)
        r.mustcontain(self._validJSON)

    def test_camera_get_invalid_json(self):
        self.write_invalid_json_to_config()
        r = self.testApp.get('/camera', expect_errors=True)
        self.assertEquals(r.status, 500)

    def test_camera_put_invalid_json(self):
        r = self.testApp.put('/camera', self._invalidJSON, expect_errors=True)
        self.assertEquals(r.status, 406)

    def test_camera_put_json(self):
        r = self.testApp.put('/camera', self._validJSON, expect_errors=True)
        self.assertEquals(r.status, 200)

    def write_valid_json_to_config(self):
        with open(CONFIG_FILE_PATH, 'w') as configFile:
            configFile.write(self._validJSON)

    def write_invalid_json_to_config(self):
        with open(CONFIG_FILE_PATH, 'w') as configFile:
            configFile.write(self._invalidJSON)


if __name__ == "__main__":
    unittest.main()