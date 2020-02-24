import configparser
import logging
import os
import logging

logging.basicConfig(filename='ipnotifier.log',level=logging.DEBUG)


def read_setting(session, key, config_file='setting.ini'):
    config = configparser.ConfigParser()
    cwd = os.getcwd()
    config.read(cwd + "/" + config_file)

    try:
        return config[session][key]
    except KeyError:
        logging.error("Could not find the key: " + key + " in file " + config_file)
        return None


def write_setting(session, key, value, config_file='setting.ini'):
    try:
        cwd = os.getcwd()
        config = configparser.ConfigParser()
        config.read(cwd + "/" + config_file)

        if not config.has_section(session):
            config.add_section(session)

        if not config.has_option(session, key) :
            config.set(session, key, value)

        config[session][key] = value

        with open(cwd + "/" + config_file, 'w') as f:
            config.write(f)
    except Exception as e:
        logging.error("Exception occured: {0}".format(e))