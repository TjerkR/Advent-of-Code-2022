# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:51:54 2022

@author: tjerk

v2: v1 maar dan met functies
"""

# %% Import packages

import numpy as np
import pandas as pd


# %% Import data

file_path = "advent_of_code_2022/02/data.txt"

data = pd.read_csv(file_path, delimiter=" ", names=("them", "me"))


# %% Part 1


def get_match_score(them_list, me_list):
    return [
        6
        if (them == "A" and me == "Y")
        or (them == "B" and me == "Z")
        or (them == "C" and me == "X")
        else 3
        if (them == "A" and me == "X")
        or (them == "B" and me == "Y")
        or (them == "C" and me == "Z")
        else 0
        for them, me in zip(them_list, me_list)
    ]


def get_shape_score(me_list):
    return [1 if me == "X" else 2 if me == "Y" else 3 for me in me_list]


match_score = get_match_score(data["them"], data["me"])
shape_score = get_shape_score(data["me"])

total_score = sum(match_score) + sum(shape_score)
print(total_score)
# 17189

# %% Part 2


def convert_strategy(them_list, me_list):
    return [
        "X"
        if (them == "A" and me == "Y")
        or (them == "B" and me == "X")
        or (them == "C" and me == "Z")
        else "Y"
        if (them == "A" and me == "Z")
        or (them == "B" and me == "Y")
        or (them == "C" and me == "X")
        else "Z"
        for them, me in zip(them_list, me_list)
    ]


strategy = convert_strategy(data["them"], data["me"])

match_score_2 = get_match_score(data["them"], strategy)
shape_score_2 = get_shape_score(strategy)

total_score_2 = sum(match_score_2) + sum(shape_score_2)
print(total_score_2)
# 13490
