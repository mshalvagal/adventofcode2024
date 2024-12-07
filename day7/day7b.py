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


def test(result, rest_operands, current_value):
    if current_value > result:
        return False, -1
    elif not rest_operands:
        return current_value == result, current_value
    else:
        add_val = current_value + rest_operands[0]
        mul_val = current_value * rest_operands[0]
        concat_val = int(str(current_value) + str(rest_operands[0]))
        test_add = test(result, rest_operands[1:], add_val)
        if test_add[0]:
            return test_add
        test_mul = test(result, rest_operands[1:], mul_val)
        if test_mul[0]:
            return test_mul
        test_concat = test(result, rest_operands[1:], concat_val)
        if test_concat[0]:
            return test_concat
        return False, -1

# def test_concat(result, operands, pos_concat):
#     if pos_concat == len(operands) - 1:
#         return test(result, operands[1:], operands[0])
#     test_result_1 = test_concat(result, operands, pos_concat + 1)
#     if test_result_1[0]:
#         return test_result_1
#     possible_concat = int(str(operands[pos_concat]) + str(operands[pos_concat + 1]))
#     test_result_2 = test_concat(result, operands[:pos_concat] + [possible_concat] + operands[pos_concat + 2:], pos_concat)
#     if test_result_2[0]:
#         return test_result_2
#     return False, -1

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

EXAMPLE_ANS = 11387

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
