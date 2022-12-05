# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:51:54 2022

@author: tjerk

v1: Lekker hardcoden
"""

# %% Import packages

import numpy as np
import pandas as pd


# %% Import data

file_path = (
    "C:/Users/tjerk/Little Rocket/Projects/Advent-of-Code-2022/"
    "advent_of_code_2022/02/data.txt"
)

data = pd.read_csv(file_path, delimiter=" ", names=("them", "me"))
# data = data.squeeze()
# with open(file_path) as f:
#     lines = f.read().splitlines()


# %% Script 1

match_score = [
    6
    if (them == "A" and me == "Y")
    or (them == "B" and me == "Z")
    or (them == "C" and me == "X")
    else 3
    if (them == "A" and me == "X")
    or (them == "B" and me == "Y")
    or (them == "C" and me == "Z")
    else 0
    for them, me in zip(data["them"], data["me"])
]

shape_score = [1 if me == "X" else 2 if me == "Y" else 3 for me in data["me"]]

total_score = sum(match_score) + sum(shape_score)
print(total_score)
# 17189


# %% Script 2

strategy = [
    "X"
    if (them == "A" and me == "Y")
    or (them == "B" and me == "X")
    or (them == "C" and me == "Z")
    else "Y"
    if (them == "A" and me == "Z")
    or (them == "B" and me == "Y")
    or (them == "C" and me == "X")
    else "Z"
    for them, me in zip(data["them"], data["me"])
]

match_score_2 = [
    6
    if (them == "A" and me == "Y")
    or (them == "B" and me == "Z")
    or (them == "C" and me == "X")
    else 3
    if (them == "A" and me == "X")
    or (them == "B" and me == "Y")
    or (them == "C" and me == "Z")
    else 0
    for them, me in zip(data["them"], strategy)
]

shape_score_2 = [1 if me == "X" else 2 if me == "Y" else 3 for me in strategy]

total_score_2 = sum(match_score_2) + sum(shape_score_2)
print(total_score_2)
# 13490