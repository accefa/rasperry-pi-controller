import unittest

from paste.fixture import TestApp

from main import app


class DcTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_drive_dc_forward(self):
        request = self.testApp.post('/drive/dc/forward')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

    def test_drive_dc_backward(self):
        request = self.testApp.post('/drive/dc/backward')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)

    def test_drive_dc_reset(self):
        request = self.testApp.post('/drive/dc/reset')
        self.assertEquals(request.header_dict['content-type'], 'text/json')
        self.assertEquals(request.status, 200)


if __name__ == "__main__":
    unittest.main()