import re
import typing
import math
from collections.abc import Iterable
import sys
import numpy as np

def lmap(func, *iterables):
    return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))
def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))
def floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))
def positive_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))
def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)
def alphanums(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z0-9]+", s)
def lfilter(func, *iterables):
    return list(filter(func, *iterables))
def pprint(a, name):
    print(f'\n{name}:\n{a}')

import random
from collections import defaultdict

def check_xmas(local_grid):
    diag1 = ''.join(local_grid.diagonal())
    diag2 = ''.join(np.fliplr(local_grid).diagonal())
    return (diag1 in ['MAS', 'SAM']) and (diag2 in ['MAS', 'SAM'])
    

def solve(path):
    ans = 0
    with open(path) as f:
        input = f.read().strip().split('\n')
    
    # convert to numpy array
    input = np.array([list(x) for x in input])

    # find every A in the grid
    for i in range(1, len(input)-1):
        for j in range(1, len(input[i])-1):
            if input[i][j] == 'A':
                ans += check_xmas(input[i-1:i+2, j-1:j+2])

    return int(ans)

EXAMPLE_ANS = 9

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
