from Utility.ReadJSON import JSONParser
import numpy as np

# from pip import


class DeSNN:
    def __init__(self, location=None):
        self.location = location

    def validation(self, drift=None, mod=None, k=None, sigma=None, c=None):
        reader = JSONParser(self.location)
        spike_state = np.matrix(reader.neucube_json()['structure']['spike_states'])
        print(spike_state.shape)



    def training(self):
        pass
