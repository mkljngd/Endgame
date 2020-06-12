import re
import os
f = open('actual_data.txt').readlines()

# for i in f:
print(map(int, re.findall('[0-9]+', i)) for i in open('actual_data.txt').readlines())
