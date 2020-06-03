import argparse

parser = argparse.ArgumentParser(description='this is test')

parser.add_argument('-H', '--host', type=str, default='127.0.0.1',help='Server Addr')

parser.add_argument('-v', '--version', action='version', version='v1.0')
parser.add_argument('-V', '--verbose', action='store_true', help='DEBUG INFO')


a = parser.parse_args()
print(a)
