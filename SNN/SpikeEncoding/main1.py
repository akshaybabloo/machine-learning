from Utility.JSONParser import JSONParser
import numpy as np

a = JSONParser('cube_20160219T110901.json')

print(a.neucube_json()['classifier']['firing_order'])
