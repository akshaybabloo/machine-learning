import os
import json


class JSONParser:
    def __init__(self, location=None):
        if location is None:
            self.current_folder = os.path.dirname(os.path.realpath(__file__)) + "/data/"
        else:
            self.current_folder = location

    def get_json(self):

        with open(self.current_folder + 'conf.json') as f:
            data = json.load(f)

        return data
