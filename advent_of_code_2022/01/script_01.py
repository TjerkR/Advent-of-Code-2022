# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 00:08:00 2022

@author: tjerk
"""

# %% Import packages

import numpy as np
import pandas as pd
import lr_data_lib


# %% Import data

# data = pd.read_csv("C:/Users/tjerk/Little Rocket/Projects/Advent-of-Code-2022/advent_of_code_2022/01/data.txt")
# data = data.squeeze()
with open("C:/Users/tjerk/Little Rocket/Projects/Advent-of-Code-2022/advent_of_code_2022/01/data.txt") as f:
    lines = f.read().splitlines()


# %% Script

total_calories = []
calories = []
for line in lines:
    # if not line:
    #     sum_ = sum(calories)
    #     calories = []
    #     total_calories.append(sum)
    #     print("YES")
    try:
        calories.append(int(line))
        # print(line)
    except ValueError:
        sum_ = sum(calories)
        calories = []
        total_calories.append(sum_)       
        
max_calories = max(total_calories)
print("Answer 1: {}".format(max_calories))


# %% Part 2
calories_series = pd.Series(total_calories)
calories_series = calories_series.sort_values(ascending=False)

answer = sum(calories_series.tolist()[0:3])
print("Answer 2: {}".format(answer))