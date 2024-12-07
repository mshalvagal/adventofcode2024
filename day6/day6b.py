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

def propagate_full(map, pos, direction, visitation):
    x, y = pos
    dx, dy = direction
    boundary = False
    while True:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= map.shape[0] or y >= map.shape[1]:
            boundary = True
            break
        if map[x, y] == '#':
            pos = (x - dx, y - dy)
            direction = (dy, -dx)
            break
        if map[x, y] == '.':
            map[x, y] = 'X'
            visitation.append(((x, y), direction))
    return boundary, map, pos, direction, visitation

def propagate(map, pos, direction, visitation):
    boundary = False
    loop = False

    while True:
        x, y = pos
        dx, dy = direction
        if direction == (1, 0):
            potential_path = map[x+1:, y]
        elif direction == (-1, 0):
            potential_path = map[:x, y][::-1]
        elif direction == (0, 1):
            potential_path = map[x, y+1:]
        elif direction == (0, -1):
            potential_path = map[x, :y][::-1]
        # print(x, y, direction, potential_path)
        
        # stop if we hit a wall or the end of the map
        if '#' in potential_path:
            if direction == (1, 0):
                pos = (x + np.where(potential_path == '#')[0][0], y)
            elif direction == (-1, 0):
                pos = (x - np.where(potential_path == '#')[0][0], y)
            elif direction == (0, 1):
                pos = (x, y + np.where(potential_path == '#')[0][0])
            elif direction == (0, -1):
                pos = (x, y - np.where(potential_path == '#')[0][0])
            direction = (dy, -dx)
            map[pos[0], pos[1]] = 'X'
            if (pos, direction) in visitation:
                loop = True
                return boundary, map, pos, direction, visitation, loop
            else:
                visitation.append((pos, direction))
        else:
            boundary = True
            break

    # while True:
    #     x += dx
    #     y += dy
    #     if x < 0 or y < 0 or x >= map.shape[0] or y >= map.shape[1]:
    #         boundary = True
    #         break
    #     if map[x, y] == '#' or map[x, y] == 'O':
    #         pos = (x - dx, y - dy)
    #         direction = (dy, -dx)
    #         break
    #     elif map[x, y] == '.':
    #         map[x, y] = 'X'
    #         visitation.append(((x, y), direction))
    #     elif map[x, y] == 'X':
    #         pos = (x, y)
    #         direction = (dx, dy)
    #         if ((x, y), direction) in visitation:
    #             loop = True
    #             return boundary, map, pos, direction, visitation, loop
    #         else:
    #             visitation.append(((x, y), direction))
    return boundary, map, pos, direction, visitation, loop

def test_loop_with_new_obstacle(map, initial_pos, initial_direction):

    loops = 0

    visitation_all = []
    visitation_all.append((initial_pos, initial_direction))
    pos = initial_pos
    direction = initial_direction
    og_map = np.copy(map)

    while True:
        done, map, pos, direction, visitation_all = propagate_full(map, pos, direction, visitation_all)
        if done:
            break

    loop_obstacles = []

    for i in range(1, len(visitation_all)):
        new_map = np.copy(og_map)
        new_map[visitation_all[i][0][0], visitation_all[i][0][1]] = '#'
        visitation = [(initial_pos, initial_direction)]
        pos = initial_pos
        direction = initial_direction
        while True:
            done, new_map, pos, direction, visitation, loop = propagate(new_map, pos, direction, visitation)
            if done or loop:
                break
        if loop:
            if visitation_all[i][0] not in loop_obstacles:
                loop_obstacles.append(visitation_all[i][0])
            new_map[visitation_all[i][0][0], visitation_all[i][0][1]] = 'O'
            # print(new_map)
            # print('')
    return len(loop_obstacles)

def solve(path):
    ans = 0
    with open(path) as f:
        input = f.read().strip().split('\n')
    
    # convert to array
    map = np.array([list(x) for x in input])
    visitation = []

    # find the starting point indicated by '^', 'v', '<', or '>'
    if np.any(map == '^'):
        pos = np.where(map == '^')
        direction = (-1, 0)
    elif np.any(map == 'v'):
        pos = np.where(map == 'v')
        direction = (1, 0)
    elif np.any(map == '<'):
        pos = np.where(map == '<')
        direction = (0, -1)
    elif np.any(map == '>'):
        pos = np.where(map == '>')
        direction = (0, 1)
    map[pos[0][0], pos[1][0]] = 'X'
    initial_pos = (pos[0][0], pos[1][0])
    initial_direction = direction
    
    ans = test_loop_with_new_obstacle(map, initial_pos, initial_direction)

    return int(ans)

EXAMPLE_ANS = 6

ex_ans = solve('./example1.txt')

if ex_ans == EXAMPLE_ANS:
    print("\nWorks on the example! Trying full case.\n")
    final_ans = solve('./input1.txt')
    print("=====>     ", final_ans, "     <=====\n")
else:
    print(f"\nDoes not work on the example, got {ex_ans} instead of {EXAMPLE_ANS}\n")
