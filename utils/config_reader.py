import os
from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))


def readConfig(section,key):
    config = ConfigParser()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory where configReader.py is located
    CONFIG_PATH = os.path.join(BASE_DIR, "..", "config", "config.ini")  # Navigate to conf.ini
    config.read(CONFIG_PATH)
    return config.get(section,key)


def get_config(section, key):
    config = ConfigParser()
    config.read(os.path.join("config", "config.ini"), encoding="utf-8")
    return config.get(section, key)