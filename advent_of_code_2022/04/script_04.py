# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:23:35 2022

@author: tjerk
"""

# %% Import packages

import numpy as np
import pandas as pd


# %% Import data

with open("advent_of_code_2022/04/data.txt") as f:
    lines = f.read().splitlines()


# %% Part 1


# Split into two
left = [line.split(",")[0] for line in lines]
right = [line.split(",")[1] for line in lines]

# Convert ranges to lists of numbers
left1 = [int(nums.split("-")[0]) for nums in left]
left2 = [int(nums.split("-")[1]) for nums in left]
right1 = [int(nums.split("-")[0]) for nums in right]
right2 = [int(nums.split("-")[1]) for nums in right]

left_range = [np.arange(start, stop+1) for start, stop in zip(left1, left2)]
right_range = [np.arange(start, stop+1) for start, stop in zip(right1, right2)]

# Find overlap
overlap = [np.intersect1d(l, r).size == min(l.size, r.size) 
           for l, r in zip(left_range, right_range)]

# Result
result = sum(overlap)
print(result)
# 459


# %% Part 2

# Find overlap
overlap_2 = [np.intersect1d(l, r).size > 0
             for l, r in zip(left_range, right_range)]

# Result
result_2 = sum(overlap_2)
print(result_2)
# 779