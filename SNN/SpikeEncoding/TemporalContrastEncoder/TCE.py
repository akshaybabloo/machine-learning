import numpy as np
from Utility.ReadJSON import JSONParser
from Utility.ReadCSV import ReadCSV

class TCE:
    def __init__(self, location=None, config=None):
        self.location = location

        read_csv = ReadCSV(self.location)
        self.sample_number = read_csv.sample_size()
        self.data = read_csv.read_csv()
        self.time_length = read_csv.time_feature_length()['time_length']
        self.feature_length = read_csv.time_feature_length()['feature_length']

        thresh = JSONParser(config)
        self.thresh = thresh.get_json()['parameter']['threshold']

    def encoder(self):
        """
        Encodes the given data into spikes depending upon the given spike rate
        :return:
        """
        variable_threshold = self.threshold()
        # timelengeth = 128
        # spike_state_length = timelengeth * self.sample_number

        b = []

        if self.sample_number > 0:
            threshold = np.tile(np.transpose(variable_threshold), [len(self.data), 1])

            for i in range(0, len(self.data)):
                b.append(np.subtract(self.data[i], self.data[i - 1]).tolist())

            spike = np.concatenate(
                ((b > threshold).astype(int) - (b < -threshold).astype(int), (b < -threshold).astype(int)), axis=1)

            return spike
        else:
            raise(Exception('Sample number is either less than or equal to 0.'))

    def threshold(self):
        """
        Returns the threshold values for each input value.
        :return:
        """
        x = np.array(self.data)
        data = np.diff(list(map(list, zip(*x))))

        k = []
        z = []
        m = []

        v = 0.
        for a in range(0, len(data)):

            for i in range(0, len(data[0]), self.time_length):
                v += np.mean(np.abs(data[a][i:i + self.time_length-1])) + np.std(np.abs(data[a][i:i + self.time_length-1])) * self.thresh
                k.append(v)

            for l in range(0, len(data)):
                if a == l:
                    v = 0.

        for x in range(self.feature_length):
            z.append(k[:self.sample_number])
            del k[:self.sample_number]

        for s in range(len(z)):
            m.append(z[s][self.sample_number-1])

        return np.transpose(m) / self.sample_number


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
