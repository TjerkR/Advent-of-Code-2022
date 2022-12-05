# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:53:04 2022

@author: tjerk
"""

# %% Import packages

import numpy as np
import pandas as pd
import collections


# %% Import data

with open("advent_of_code_2022/03/data.txt") as f:
    lines = f.read().splitlines()


# %% Part 1

first_part = []
second_part = []
first_unique = []
second_unique = []
joined_unique = []
overlap = []
for line in lines:
    fp = line[:len(line)//2]
    sp = line[len(line)//2:]
    
    first_part.append(fp)
    second_part.append(sp)
    
    fpu = "".join(set(fp))
    spu = "".join(set(sp))
    
    first_unique.append(fpu)
    second_unique.append(spu)
    
    joined_unique.append(fpu + spu)
    
    # Assuming only one character in both strings!
    ov = collections.Counter(fpu + spu).most_common(1)[0][0]
    
    overlap.append(ov)


def convert_to_value(char):
    val = ord(char) - 96
    if val < 0:
        val += 58
    return val


values = list(map(convert_to_value, overlap))

result = sum(values)
print(result)
# 8185


# %% Part 2

# Get lines with only unique chars
lines_unique = []
for line in lines:
    lines_unique.append("".join(set(line)))

# Groups of three
lines_three = []
overlap3 = []
for i in range(0, len(lines), 3):
    line_three = lines_unique[i] + lines_unique[i+1] + lines_unique[i+2]
    lines_three.append(line_three)
    ov3 = collections.Counter(line_three).most_common(1)[0][0]
    overlap3.append(ov3)
    
values3 = list(map(convert_to_value, overlap3))

result3 = sum(values3)
print(result3)
# 2817
