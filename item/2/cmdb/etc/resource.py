# encoding: utf-8

import os

if __name__ == '__main__':
    f = os.popen('top -n 1')
    lines = f.readlines()
    cpu_line = lines[2]
    cpu_line = cpu_line.split()[1]

    cpu = float(cpu_line[:cpu_line.find('%')])

    mem_line = lines[3]
    mem = mem_line.split()

    mem = 100 * float(mem[4][:-1] / float(mem[2][:-1]))

    print(cpu)
    print(mem)

    f.close()