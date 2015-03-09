import unittest
import json
from paste.fixture import TestApp
from nose.tools import *
from Webserver import app

class TestCode(unittest.TestCase):

    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        self._validJSON = json.dumps({'json': 'test'})
        self._invalidJSON = 'No JSON!'

    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))
    
    def test_index(self):
        r = self.testApp.get('/')
        assert_equal(r.status, 200)
        r.mustcontain('Hello, world!')

if __name__ == "__main__": 
    unittest.main()