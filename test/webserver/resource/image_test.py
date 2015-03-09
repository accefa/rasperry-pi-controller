import unittest
from paste.fixture import TestApp
from webserver.main import app
from nose.tools import *

class ImageTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_image_get(self):
        request = self.testApp.get("/image")
        assert_equals(request.status, 200)