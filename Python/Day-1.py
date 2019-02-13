import os
import re

fileDir = os.path.dirname(os.path.abspath('__file__'))
input_file = os.path.join(fileDir, '.\Inputs\Day-1-Input')
f = open(input_file)

freqs = f.readlines()
freqs = [int(re.sub('\s*','',f)) for f in freqs]

print(sum(freqs))   