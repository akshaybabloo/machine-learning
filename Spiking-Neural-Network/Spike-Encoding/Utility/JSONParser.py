import json


class JSONParser:
    def __init__(self, location=None):
        self.current_folder = location

    def get_json(self):

        with open(self.current_folder + 'conf.json') as f:
            data = json.load(f)

        return data
