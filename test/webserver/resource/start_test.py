import unittest
from paste.fixture import TestApp

from nose.tools import *

from webserver.main import app


class StartTest(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))

    def test_start_get(self):
        request = self.testApp.get("/start")
        assert_equals(request.status, 200)

    def test_start_put(self):
        request = self.testApp.put("/start")
        assert_equals(request.status, 200)


if __name__ == "__main__":
    unittest.main()