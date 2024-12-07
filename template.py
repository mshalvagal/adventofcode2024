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

def karger_min_cut(graph):
    while len(graph) > 2:
        node1, node2 = random.choice(list(graph.items()))
        node2 = node2[0]
        # print(node1)
        # print(graph[node1])
        # print(node2)
        # print(' ')
        # print(graph[node2])
        for node in graph[node2]:
            # print(node2)
            # print(node)
            # print(graph[node])
            if node not in graph[node1]:
                graph[node1].append(node)
                graph[node].append(node1)
            graph[node].remove(node2)
        del graph[node2]
    return len(list(graph.values())[0])

def find_min_cut(graph, iterations):
    min_cut = float('inf')
    for _ in range(iterations):
        new_graph = defaultdict(list, {k: v[:] for k, v in graph.items()})
        cut = karger_min_cut(new_graph)
        min_cut = min(min_cut, cut)
    return min_cut

def solve(path):
    ans = 0
    with open(path) as f:
        lines = f.read().strip().split('\n')

    graph = {}
    for line in lines:
        x = alphanums(line)
        key = x[0]
        vals = x[1:]
        if key in graph.keys():
            graph[key].extend(vals)
        else:
            graph[key] = vals
        for val in vals:
            if val in graph.keys():
                graph[val].append(key)
            else:
                graph[val] = [key]

    print(graph)
    min_cut = find_min_cut(graph, 100)

    print(min_cut)

    return int(ans)

EXAMPLE_ANS = 54

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
