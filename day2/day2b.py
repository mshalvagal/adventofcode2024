import re
import typing
import math
from collections.abc import Iterable
import sys
import numpy as np
import multiprocessing as mp

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

def safe(levels):
    diff_levels = np.diff(levels)
    # check if all diffs are of same sign
    if all(diff_levels > 0) or all(diff_levels < 0):
        if all(np.abs(diff_levels) <= 3):
            return True
    return False

def safe_leave_one_out(levels):
    if safe(levels):
        return True
    if safe(levels[1:]):
        return True
    if safe(levels[:-1]):
        return True
    for i in range(1, len(levels)-1):
        if safe(levels[:i] + levels[i+1:]):
            return True
    return False

def solve(path):
    ans = 0
    with open(path) as f:
        lines = f.read().strip().split('\n')
    
    reports = [ints(line) for line in lines]
    
    for report in reports:
        if safe_leave_one_out(report):
            ans += 1

    return int(ans)

EXAMPLE_ANS = 4

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input2.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
