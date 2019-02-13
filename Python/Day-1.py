import os
import re

input_file = os.path.normpath("C:/Users/mezan/Documents/Deep Learning Nanodegree/Advent-of-Code-2018/Inputs/Day-1-Input")
f = open(input_file)
freqs = f.readlines()
freqs = [int(re.sub('\s*','',f)) for f in freqs]
print(sum(freqs))