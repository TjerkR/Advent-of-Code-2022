# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:56:54 2022

@author: tjerk
"""

# %% Import packages

import numpy as np
import pandas as pd


# %% Import data

file_path = "advent_of_code_2022/05/data.txt"

with open(file_path) as f:
    lines = f.read().splitlines()


# %% Part 1

# Get stacks
lines_stacks = lines[:8]
num_lines = len(lines_stacks)
num_stacks = (len(lines[0])+1) // 4

stacks_array = []
for i in range(num_stacks):
    stacks_array.append([])
    index = i*4 + 1
    j = -1
    while abs(j) <= num_lines and lines_stacks[j][index] != " ":
        stacks_array[i].append(lines_stacks[j][index])
        j -= 1

# Get moves
lines_moves = lines[10:]
lines_moves_split = [[int(n) for n in line.split()[1:6:2]] for line in lines_moves]
moves_df = pd.DataFrame(lines_moves_split, columns=["move", "from", "to"])

# Rearrange
for index, row in moves_df.iterrows():
    from_stack = stacks_array[row["from"]-1].copy()
    to_stack = stacks_array[row["to"]-1].copy()
    num_move = row["move"]

    to_stack += from_stack[-num_move:][::-1]
    from_stack = from_stack[:-num_move]
    
    stacks_array[row["from"]-1] = from_stack
    stacks_array[row["to"]-1] = to_stack
    
result = "".join([stack[-1] for stack in stacks_array])
print(result)
# LBLVVTVLP


# %% Part 2

# Get stacks
lines_stacks = lines[:8]
num_lines = len(lines_stacks)
num_stacks = (len(lines[0])+1) // 4

stacks_array = []
for i in range(num_stacks):
    stacks_array.append([])
    index = i*4 + 1
    j = -1
    while abs(j) <= num_lines and lines_stacks[j][index] != " ":
        stacks_array[i].append(lines_stacks[j][index])
        j -= 1

# Get moves
lines_moves = lines[10:]
lines_moves_split = [[int(n) for n in line.split()[1:6:2]] for line in lines_moves]
moves_df = pd.DataFrame(lines_moves_split, columns=["move", "from", "to"])

# Rearrange
for index, row in moves_df.iterrows():
    from_stack = stacks_array[row["from"]-1].copy()
    to_stack = stacks_array[row["to"]-1].copy()
    num_move = row["move"]

    to_stack += from_stack[-num_move:]
    from_stack = from_stack[:-num_move]
    
    stacks_array[row["from"]-1] = from_stack
    stacks_array[row["to"]-1] = to_stack
    
result = "".join([stack[-1] for stack in stacks_array])
print(result)
# TPFFBDRJD