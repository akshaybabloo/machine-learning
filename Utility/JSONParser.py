import json
import sys


class JSONParser:
    def __init__(self, location=None):
        self.current_folder = location

    def get_json(self):
        """
        Returns JSON attributes.
        :return:
        """
        try:
            with open(self.current_folder + 'conf.json') as f:
                data = json.load(f)
            return data
        except IOError as e:
            print('File not found - ', e)
            sys.exit(1)

    def neucube_json(self):
        """
        Returns NeuCube JSON attributes.
        :return:
        """
        try:
            with open(self.current_folder) as f:
                data = json.load(f)
            return data
        except IOError as e:
            print('File not found - ', e)
            sys.exit(1)
