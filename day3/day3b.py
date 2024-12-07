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

def solve(path):
    ans = 0
    with open(path) as f:
        input = f.read().strip()

    # regex to find mul(int, int)
    regex = r'mul\((\d+),(\d+)\)'
    # find all matches and their positions
    matches = re.findall(regex, input)
    positions = [m.start() for m in re.finditer(regex, input)]

    # regex to find do() and don't()
    regex_do = r'do\(\)'
    regex_dont = r'don\'t\(\)'
    positions_do = [m.start() for m in re.finditer(regex_do, input)]
    positions_dont = [m.start() for m in re.finditer(regex_dont, input)]

    # loop through all matches
    for i, match in enumerate(matches):
        # get the two numbers
        a, b = map(int, match)
        # multiply them if there are do() before and no dont() between
        closest_do = max([p for p in positions_do if p < positions[i]], default=0)
        closest_dont = max([p for p in positions_dont if p < positions[i]], default=-1)
        if closest_do > closest_dont:
            ans += a * b

    return int(ans)

EXAMPLE_ANS = 48

ex_ans = solve('./example2.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
