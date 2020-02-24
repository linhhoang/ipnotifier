import unittest
import config_helper
from test import test_support

class ConfigHelperReadTestCase(test_support.ConfigTestSupport ,unittest.TestCase):


    def test_ReadSetting(self):
        username = config_helper.read_setting('Session1', 'username', 'test_setting.ini')
        self.assertEqual('abc', username)

        password = config_helper.read_setting('Session1', 'password', 'test_setting.ini')
        self.assertEqual('abcpwd', password)

    def test_ReadSetting_notFoundKey(self):
        username = config_helper.read_setting('Session1', 'notfound', 'test_setting.ini')
        self.assertIsNone(username)


    def test_ReadSetting_FileNotFound(self):
        username = config_helper.read_setting('Session1', 'username', 'not_found.ini')

        self.assertIsNone(username)


#@unittest.skip
class ConfigHelperWriteTestCase(unittest.TestCase):
    def test_WriteSetting(self):
        config_helper.write_setting('Session1', 'username', 'uname1', 'test_setting.ini')
        username = config_helper.read_setting('Session1', 'username', 'test_setting.ini')
        self.assertEqual('uname1', username)

    def test_WriteSetting(self):
        config_helper.write_setting('Session2', 'username2', 'uname2', 'test_setting.ini')
        username = config_helper.read_setting('Session2', 'username2', 'test_setting.ini')
        self.assertEqual('uname2', username)

if __name__ == '__main__':
    unittest.main()
