import csv
import os
import re
import numpy as np
from Temporal_Contrast_Encoder.JsonParser import JSON
from distutils.util import strtobool


class TCE:
    def __init__(self, location=None):
        if location is None:
            self.current_folder = os.path.dirname(os.path.realpath(__file__)) + "/data/"
        else:
            self.current_folder = location
        # assigns only file prefixed with "sam"
        self.prefixed = [filename for filename in os.listdir(self.current_folder) if filename.startswith("sam")]
        self.sample_number = len(self.prefixed)

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
                    # data.append(row[0])
            csv_file.close()

        # return np.matrix([list(map(float, da)) for da in data])
        return [list(map(float, da)) for da in data]
        # return data

    # @staticmethod
    def encoder(self):
        np.set_printoptions(threshold=np.nan)
        variable_threshold = self.threshold()
        data = self.read_csv()
        print(len(data))

        timelengeth = 128
        spike_state_length = timelengeth * self.sample_number

        if self.sample_number > 0:
            threshold = np.tile(np.transpose(variable_threshold), [7680, 1])
            print(len(threshold))

            b = []
            for i in range(0, len(data)):
                b.append(np.subtract(data[i], data[i - 1]).tolist())

            spike = np.concatenate(((b > threshold).astype(int) - (b < -threshold).astype(int), (b < -threshold).astype(int)), axis=1)

            print(spike)
            # spike_state = []
            # for g in range(len(data)):
            #     spike_state =

    def threshold(self):
        x = np.array(self.read_csv())
        data = np.diff(list(map(list, zip(*x))))

        param = JSON()
        param.parse_json()

        k = []
        z = []
        m = []

        v = 0.
        for a in range(0, len(data)):

            for i in range(0, len(data[0]), 128):
                v += np.mean(np.abs(data[a][i:i + 127])) + np.std(np.abs(data[a][i:i + 127])) * 0.5
                k.append(v)

            for l in range(0, len(data)):
                if a == l:
                    v = 0.

        for x in range(14):
            z.append(k[:60])
            del k[:60]

        for s in range(len(z)):
            m.append(z[s][59])

        return np.transpose(m) / 60


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

    # print(some_object.feature_names())
    # some_object.threshold()
    # print(np.matrix(some_object.read_csv()).)

    print(some_object.encoder())


if __name__ == '__main__':
    main()
