import json
import os
import logging

class Settings:
    def __init__(self, settings_path='settings.json'):
        self.port = 80
        self.loglevel = "DEBUG"
        self.webdir = "./src"

        if os.path.exists(settings_path):
            with (open(settings_path, 'r') as f):
                data = json.load(f)
                self.webdir = data.get('webdir', self.webdir)
                self.port = data.get('port', self.port)
                self.loglevel = data.get('loglevel', self.loglevel).upper()

settings = Settings()

def setup_logging():
    level = getattr(logging, settings.loglevel, logging.INFO)
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

setup_logging()
