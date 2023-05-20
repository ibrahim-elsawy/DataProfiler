from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
db_path = config['DB']['dir']

