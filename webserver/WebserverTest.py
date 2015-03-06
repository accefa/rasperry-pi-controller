import unittest
import json
from paste.fixture import TestApp
from nose.tools import *
from Webserver import app, CONFIG_FILE_PATH

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
    
    def test_camera_get(self):
        self.write_valid_json_to_config()
        r = self.testApp.get('/camera')
        assert_equal(r.status, 200)
        r.mustcontain(self._validJSON)
        
    def test_camera_get_invalid_json(self):
        self.write_invalid_json_to_config()
        r = self.testApp.get('/camera', expect_errors=True)
        assert_equal(r.status, 500)
         
    def test_camera_put_invalid_json(self):
        r = self.testApp.put('/camera', self._invalidJSON, expect_errors=True)
        assert_equal(r.status, 406)
         
    def test_camera_put_json(self):
        r = self.testApp.put('/camera', self._validJSON)
        assert_equal(r.status, 200)
        
    def write_valid_json_to_config(self):
        with open(CONFIG_FILE_PATH, 'w') as configFile:
            configFile.write(self._validJSON)
        
    def write_invalid_json_to_config(self):
        with open(CONFIG_FILE_PATH, 'w') as configFile:
            configFile.write(self._invalidJSON)

if __name__ == "__main__": 
    unittest.main()