import json
from paste.fixture import TestApp
import unittest
from webserver.main import app

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

    def test_camera_put_invalid_json(self):
        request = self.testApp.put('/camera', self._invalidJSON, expect_errors=True)
        self.assertEquals(request.status, 406)

    def test_camera_put_json(self):
        request = self.testApp.put('/camera', self._validJSON, expect_errors=True)
        self.assertEquals(request.status, 200)
        self.assertEquals(request.header_dict['content-type'], 'text/json')


if __name__ == "__main__":
    unittest.main()