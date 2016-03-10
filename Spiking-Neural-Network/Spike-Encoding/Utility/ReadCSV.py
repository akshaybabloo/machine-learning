import os
import csv
import re
import sys


class ReadCSV:
    def __init__(self, location=None):
        if location is None:
            self.current_folder = os.path.dirname(os.path.realpath(__file__)) + "/data/"
        else:
            self.current_folder = location
        # assigns only file prefixed with "sam"
        try:
            self.prefixed = [filename for filename in os.listdir(self.current_folder) if filename.startswith("sam")]
        except IOError as e:
            print("File not found - ", e)
            sys.exit(1)

    def read_csv(self):
        """
        Search for samples, and format it into one array
        :return: data
        """

        self.prefixed.sort(key=natural_keys)  # Sorted with filename and sample number
        data = []  # place holder

        for files in self.prefixed:
            with open(self.current_folder + files, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
                for row in reader:
                    data.append(row[0].split(','))
            csv_file.close()

        return [list(map(float, da)) for da in data]

    def sample_size(self):

        return len(self.prefixed)

    def feature_names(self):
        """
        Reads feature names if present
        :return:
        """
        if os.path.isfile(self.current_folder + 'feature_names_eeg.txt'):
            try:
                with open(self.current_folder + 'feature_names_eeg.txt', 'r') as f:
                    data = f.read()
                f.close()
                return data.split('\n')
            except IOError:
                print("file not found")
        else:
            with open(self.current_folder + self.prefixed[0]) as f:
                number_of_features = len(f.readline().split(','))
                name = []
                for x in range(1, number_of_features):
                    name.append("feature {}".format(x))
                f.close()

                return {'number_of_features': number_of_features, 'name_features': name}


def atoi(text):
    """
    Checks if the file names contain numbers
    :param text:
    :return:
    """
    return int(text) if text.isdigit() else text


def natural_keys(text):
    """
    Splits the number from the file name
    :param text:
    :return:
    """
    return [atoi(c) for c in re.split('(\d+)', text)]
