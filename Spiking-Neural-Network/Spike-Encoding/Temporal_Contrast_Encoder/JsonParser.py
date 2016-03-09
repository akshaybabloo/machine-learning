import json
import os


class JSON:
    def __init__(self):
        try:
            self.current_folder = os.path.dirname(os.path.realpath(__file__)) + '/'
        except IOError:
            print("JSON file not found")

    def parse_json(self):
        with open(self.current_folder + 'conf.json') as f:
            data = json.load(f)

        return data


def main():
    test = JSON()
    print(test.parse_json()['parameter']['threshold'])


if __name__ == '__main__':
    main()
