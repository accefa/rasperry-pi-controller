import os
import unittest
import config.loggerconfig as loggerconfig


LEVEL_NORMAL = 10
LEVEL_INVALID = 11

TEST_CONFIG_FILE_PATH = os.path.dirname(__file__) + '/../config_test.json'


class DetectionConfigTest(unittest.TestCase):
    def setUp(self):
        self.loggerconfig = loggerconfig.LoggerConfig()
        self.loggerconfig.CONFIG_FILE_PATH = TEST_CONFIG_FILE_PATH

    def tearDown(self):
        os.remove(TEST_CONFIG_FILE_PATH)

    def test_set_from_dict_only_level(self):
        lovel_dict = {loggerconfig.LEVEL_KEY: LEVEL_NORMAL}
        self.loggerconfig.set_from_dict(lovel_dict)
        self.assertEquals(LEVEL_NORMAL, self.loggerconfig.level)

    def test_set_get_from_dict_all(self):
        set_dict = {
            loggerconfig.LEVEL_KEY: LEVEL_NORMAL,
        }
        self.loggerconfig.set_from_dict(set_dict)
        get_dict = self.loggerconfig.get_as_dict()
        self.assertEquals(set_dict, get_dict)

    def test_set_get_quality(self):
        self.loggerconfig.level = LEVEL_NORMAL
        self.assertEqual(LEVEL_NORMAL, self.loggerconfig.level)

    def test_set_get_quality_invalid_level(self):
        self.loggerconfig.level = LEVEL_INVALID
        self.assertEqual(loggerconfig.LEVEL_DEFAULT, self.loggerconfig.level)


if __name__ == '__main__':
    unittest.main()