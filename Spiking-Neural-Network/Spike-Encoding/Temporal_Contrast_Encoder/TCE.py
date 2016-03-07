import csv
import os
import re


class TCE:
    def __init__(self):
        self.current_folder = os.path.dirname(os.path.realpath(__file__)) + "/data/"

    def feature_names(self):
        """
        Reads feature names if present
        :return:
        """
        # data =''
        # if os.path.isfile(self.current_folder + 'feature_names_eeg.txt'):
        #     with open(self.current_folder + 'feature_names_eeg.txt', 'r') as f:
        #         data = f.read()
        #     f.close()
        try:
            with open(self.current_folder + 'feature_names_eeg.txt', 'r') as f:
                data = f.read()
            f.close()
            return data.split('\n')
        except IOError as e:
            print("file not found")


    def read_csv(self):
        """
        Search for samples, and format it into one array
        :return: data
        """

        # assigns only file prefixed with "sam"
        prefixed = [filename for filename in os.listdir(self.current_folder) if filename.startswith("sam")]

        prefixed.sort(key=natural_keys)  # Sorted with filename and sample number

        data = []  # place holder

        for files in prefixed:
            with open(self.current_folder + files, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
                for row in reader:
                    data.append(row[0].split(','))
            csv_file.close()
        return data

        # @staticmethod
        # def encoder():


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


def main():
    some_object = TCE()
    # test = some_object.read_csv()
    # print(list(map(list, zip(*test[0:128]))))  # row to column

    print(some_object.feature_names())


if __name__ == '__main__':
    main()
