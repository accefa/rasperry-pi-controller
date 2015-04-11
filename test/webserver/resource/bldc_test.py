import unittest
import json

from paste.fixture import TestApp

from main import app

class DriveTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_drive_bldc_start(self):
        request = self.testApp.post('/drive/bldc/start', json.dumps({'rpm': 5000}))
        self.assertEquals(request.status, 200)

    def test_drive_bldc_start_with_negativ_rpm(self):
        request = self.testApp.post('/drive/bldc/start', json.dumps({'rpm': -5000}), expect_errors=True)
        self.assertEquals(request.status, 406)

    def test_drive_bldc_start_without_rpm(self):
        request = self.testApp.post('/drive/bldc/start', expect_errors=True)
        self.assertEquals(request.status, 406)

    def test_drive_bldc_stop(self):
        request = self.testApp.post('/drive/bldc/stop')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

    def test_drive_bldc_reset(self):
        request = self.testApp.post('/drive/bldc/reset')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

if __name__ == "__main__":
    unittest.main()