# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:51:54 2022

@author: tjerk

v4: Grimmige "oneliners"
"""

# %% Import packages

import numpy as np
import pandas as pd


# %% Import data

file_path = "advent_of_code_2022/02/data.txt"

data = pd.read_csv(file_path, delimiter=" ", names=("them", "me"))


# %% Part 1

total_score = sum([r["me"] + 1 + ((r["me"] + 1 - r["them"]) % 3) * 3
     for _, r in pd.read_csv(file_path, delimiter=" ", names=("them", "me"))
     .replace({"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2,}).iterrows()])

print(total_score)


# %% Part 2

total_score_2 = sum([r["me"] * 3 + ((r["me"] + r["them"] + 2) % 3) + 1
     for _, r in pd.read_csv(file_path, delimiter=" ", names=("them", "me"))
     .replace({"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2,}).iterrows()])

print(total_score_2)