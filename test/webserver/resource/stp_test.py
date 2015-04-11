import unittest
import json

from paste.fixture import TestApp

from main import app


class DriveTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_drive_stp_start_with_positiv_step(self):
        request = self.testApp.post('/drive/stp/start', json.dumps({'steps': 50}))
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

    def test_drive_stp_start_with_negtiv_step(self):
        request = self.testApp.post('/drive/stp/start', json.dumps({'steps': -30}))
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

    def test_drive_stp_start_without_step(self):
        request = self.testApp.post('/drive/stp/start', expect_errors=True)
        self.assertEquals(request.status, 406)

    def test_drive_stp_reset(self):
        request = self.testApp.post('/drive/stp/reset')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)


if __name__ == "__main__":
    unittest.main()