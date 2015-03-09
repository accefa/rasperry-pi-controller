import unittest
import json
from paste.fixture import TestApp
from nose.tools import *
from webserver.main import app


class MainTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_index(self):
        r = self.testApp.get('/')
        assert_equal(r.status, 200)
        r.mustcontain('Hello, world!')


if __name__ == "__main__":
    unittest.main()