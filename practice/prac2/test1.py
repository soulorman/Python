#encoding: utf-8

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, help='Server Addr', default='127.0.0.1')
    parser.add_argument('-P', '--port', type=int, help='Server Port', default=80)
    parser.add_argument('-I', '--plugins', type=str, nargs='+', help='Plugins', default=['ens'])
    parser.add_argument('-I2', '--plugins2', type=str, nargs='*', help='Plugins', default=['ens'])
    parser.add_argument('-V', '--verbor', action='store_true')

    args = parser.parse_args()
    print(args)