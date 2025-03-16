# utils/config_loader.py
import configparser

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config