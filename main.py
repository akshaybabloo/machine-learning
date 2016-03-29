from SNN.SpikeEncoding.TemporalContrastEncoder.TCE import TCE
import os
import argparse
import sys


parser = argparse.ArgumentParser(prog='NeuCube',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='''\
                                                                Description
                                                         ------------------------

                                 If you want to change the default folder from "/data/" to a different one \n
                                 you can do the following: \n
                                 python main.py -d folder_name -c conf.json
                                 ''',
                                 epilog='Contact akshay.gollahalli@aut.ac.nz for more info.')
parser.add_argument('-d', '--data', default='data', help='Location of data folder', type=str)
parser.add_argument('-c', '--config', default='data', help='Location of configuration file', type=str)
args = parser.parse_args()

if sys.version_info < (3, 0):
    print("Python 2 is not supported, please download and install Python 3 from -> https://www.python.org/downloads/")
    sys.exit(1)

if args.data == 'data' and args.config == 'data':
    location = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data' + os.sep)
    var = TCE(location, location)
else:
    data_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.data + os.sep)
    config_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), args.config + os.sep)
    var = TCE(data_location, config_location)

print(var.encoder())
