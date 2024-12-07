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

def check_valid(nums, rules, rules_2):
    for i in range(len(nums)):
        if nums[i] in rules.keys():
            for j in rules[nums[i]]:
                if j in nums[:i]:
                    return False
        if nums[i] in rules_2.keys():
            for j in rules_2[nums[i]]:
                if j in nums[i+1:]:
                    return False
    return True

def solve(path):
    ans = 0
    with open(path) as f:
        input = f.read().strip().split('\n')
    
    rules = {}
    rules_2 = {}
    i = 0
    for line in input:
        if line == '':
            updates = input[i+1:]
            break
        before, after = line.split('|')
        # convert to ints
        before = int(before)
        after = int(after)
        if before not in rules.keys():
            rules[before] = [after]
        else:
            rules[before].append(after)
        if after not in rules_2.keys():
            rules_2[after] = [before]
        else:
            rules_2[after].append(before)
        i += 1

    for line in updates:
        nums = ints(line)
        if check_valid(nums, rules, rules_2):
            middle_elem = nums[len(nums)//2]
            ans += middle_elem

    return int(ans)

EXAMPLE_ANS = 143

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
