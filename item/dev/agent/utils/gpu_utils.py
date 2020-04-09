#encoding: utf-8

from nvml import Nvml

if __name__ == '__main__':
    print(Nvml.user_info())