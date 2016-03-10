import os
import numpy as np
from Utility.JSONParser import JSONParser
from Utility.ReadCSV import ReadCSV


class TCE:
    def __init__(self, location=None):
        self.location = location

        # assigns only file prefixed with "sam"
        self.prefixed = [filename for filename in os.listdir(self.location) if filename.startswith("sam")]
        self.sample_number = len(self.prefixed)

        read_csv = ReadCSV(self.location)
        self.data = read_csv.read_csv()

        thresh = JSONParser(location)
        self.thresh = thresh.get_json()['parameter']['threshold']

    def encoder(self):

        variable_threshold = self.threshold()
        timelengeth = 128
        spike_state_length = timelengeth * self.sample_number

        b = []

        if self.sample_number > 0:
            threshold = np.tile(np.transpose(variable_threshold), [7680, 1])

            for i in range(0, len(self.data)):
                b.append(np.subtract(self.data[i], self.data[i - 1]).tolist())

            spike = np.concatenate(
                ((b > threshold).astype(int) - (b < -threshold).astype(int), (b < -threshold).astype(int)), axis=1)

            return spike

    def threshold(self):
        x = np.array(self.data)
        data = np.diff(list(map(list, zip(*x))))

        k = []
        z = []
        m = []

        v = 0.
        for a in range(0, len(data)):

            for i in range(0, len(data[0]), 128):
                v += np.mean(np.abs(data[a][i:i + 127])) + np.std(np.abs(data[a][i:i + 127])) * self.thresh
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


def main():
    some_object = TCE()
    # test = some_object.read_csv()
    # print(list(map(list, zip(*test[0:128]))))  # row to column

    # print(some_object.feature_names())
    # some_object.threshold()
    # print(np.matrix(some_object.read_csv()).)

    some_object.encoder()


if __name__ == '__main__':
    main()
