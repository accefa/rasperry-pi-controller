import unittest
from paste.fixture import TestApp
from webserver.main import app
from nose.tools import *

VALID_IMAGE_NAME = 'test_image.jpg'
INVALID_IMAGE_NAME = 'invalid_image.jpg'


class ImageTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_image_get(self):
        request = self.testApp.get('/image/' + VALID_IMAGE_NAME)
        assert_equals(request.status, 200)
        assert_equals(request.header_dict['content-type'], 'images/jpeg')

    def test_image_get_invalid_path(self):
        request = self.testApp.get('/image/' + INVALID_IMAGE_NAME, expect_errors=True)
        assert_equals(request.status, 404)


if __name__ == "__main__":
    unittest.main()