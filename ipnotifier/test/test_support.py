import os
import configparser

class ConfigTestSupport(object):
    def setUp(self):
        super().setUp()
        print('setUp TestSupport')
        # Check if there is already a configurtion file
        config_filename = 'test_setting.ini'
        if not os.path.isfile(config_filename):
            # Create the configuration file as it doesn't exist yet
            cfgfile = open(config_filename, 'w')

            # Add content to the file
            Config = configparser.ConfigParser()
            Config.add_section('Session1')
            Config.set('Session1', 'username', 'abc')
            Config.set('Session1', 'password', 'abcpwd')

            Config.write(cfgfile)
            cfgfile.close()

    def tearDown(self):
        print('tearDown TestSupport')
        super().tearDown()
