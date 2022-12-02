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

with open("advent_of_code_2022/01/data.txt") as f:
    lines = f.read().splitlines()


# %% Part 1

total_calories = []
calories = []
for line in lines:
    try:
        calories.append(int(line))
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
