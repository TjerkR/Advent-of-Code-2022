# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:51:54 2022

@author: tjerk

v3: Modulo!
"""

# %% Import packages

import numpy as np
import pandas as pd
import lr_data_lib


# %% Import data

file_path = (
    "C:/Users/tjerk/Little Rocket/Projects/Advent-of-Code-2022/"
    "advent_of_code_2022/02/data.txt"
)

data = pd.read_csv(file_path, delimiter=" ", names=("them", "me"))


# %% Script 1

d_mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}
data = data.replace(d_mapping)

match_scores = [((me + 1 - them) % 3) * 3 for me, them in zip(data["me"], data["them"])]

shape_scores = [(me + 1) for me in data["me"]]

total_score = sum(match_scores) + sum(shape_scores)
print(total_score)
# 17189


# %% Script 2

match_scores_2 = [me * 3 for me in data["me"]]

shape_scores_2 = [
    ((me + them + 2) % 3) + 1 for me, them in zip(data["me"], data["them"])
]

total_score_2 = sum(match_scores_2) + sum(shape_scores_2)
print(total_score_2)
# 13490
