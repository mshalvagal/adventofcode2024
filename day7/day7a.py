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

class BinaryTree:
    def __init__(self, value, end_result, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.end_result = end_result
    
    def insert(self, value):
        add_val = self.value + value
        mul_val = self.value * value
        if add_val < self.end_result:
            self.left = BinaryTree(add_val, self.end_result)
        if mul_val < self.end_result:
            self.right = BinaryTree(mul_val, self.end_result)

def test(result, rest_operands, current_value):
    if current_value > result:
        return False, -1
    elif not rest_operands:
        return current_value == result, current_value
    else:
        add_val = current_value + rest_operands[0]
        mul_val = current_value * rest_operands[0]
        test_add = test(result, rest_operands[1:], add_val)
        test_mul = test(result, rest_operands[1:], mul_val)
        if test_add[0]:
            return test_add
        elif test_mul[0]:
            return test_mul
        else:
            return False, -1

def solve(path):
    ans = 0
    with open(path) as f:
        input = f.read().strip().split('\n')
    
    for line in input:
        x = ints(line)
        result = x[0]
        operands = x[1:]
        test_result = test(result, operands[1:], operands[0])
        if test_result[0]:
            ans += result

    return int(ans)

EXAMPLE_ANS = 3749

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
