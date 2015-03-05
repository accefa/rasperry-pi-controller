import unittest
import json
from paste.fixture import TestApp
from nose.tools import *
from Webserver import app

class TestCode(unittest.TestCase):
    def setUp(self):
        middleware = []
        self.testApp = TestApp(app.wsgifunc(*middleware))
    
    def test_index(self):
        r = self.testApp.get('/')
        assert_equal(r.status, 200)
        r.mustcontain('Hello, world!')
        
    def test_camera_put_wrong_json(self):
        parameters = 'No JSON!'
        r = self.testApp.put('/camera', parameters, expect_errors=True)
        assert_equal(r.status, 406)
        
    def test_camera_put_json(self):
        data = {'json': 'test'}
        parameters = json.dumps(data)
        r = self.testApp.put('/camera', parameters)
        assert_equal(r.status, 200)

if __name__ == "__main__": 
    unittest.main()