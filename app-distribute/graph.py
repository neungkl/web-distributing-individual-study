import matplotlib.pyplot as plt
import numpy as np
import re

from os import listdir
from os.path import isfile, join

fileList = [f for f in listdir('./report') if isfile(join('./report', f))]

# fileList = [f for f in fileList if re.compile('^single').match(f)]

color = []

for f in fileList:

    if re.compile('^lb_b1').match(f):
        color.append('blue')
    elif re.compile('^lb_b2').match(f):
        color.append('red')
    elif re.compile('^sg_b1').match(f):
        color.append('yellow')
    else:
        color.append('green')

plt.gca().set_color_cycle(color)

for f in fileList:

    with open(join('./report/',f)) as hfile:
        content = hfile.readlines()
        content = [filter(lambda x: x != '', c.split(' ')) for c in content]

        value =[]

        t = 0

        fetch = False
        for subCon in content:
            if fetch and len(subCon) >= 2:
                if t == 1:
                    value.append([subCon[0], subCon[1]])
                if subCon[1] == '1.000000' :
                    fetch = False
            if subCon[0] == 'Value' :
                fetch = True
                t = t + 1

        for i in range(0,10):
            value.pop()

        y = [c[0] for c in value]
        x = [c[1] for c in value]

        plt.plot(x, y)
        # print value

legend_col = [
    plt.Line2D((0,1),(0,0), color='blue'),
    plt.Line2D((0,1),(0,0), color='red'),
    plt.Line2D((0,1),(0,0), color='yellow'),
    plt.Line2D((0,1),(0,0), color='green')
]

plt.legend(legend_col,['LB transaction', 'LB static', 'One transaction', 'One static'], loc='upper left')
plt.show()
