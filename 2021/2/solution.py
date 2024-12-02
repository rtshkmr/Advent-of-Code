#!/usr/bin/env python3
"""
AOC Day 2
"""

__author__ = "Ritesh Kumar"


def extractInputs(): 
    inputs = list(map(lambda x: (x.rstrip("\n")), open("input").readlines()))
    return inputs
           
def extractDistances(inputs):
    forward_dist = 0
    depth = 0 
    for cmd in inputs: 
        axis, value = cmd.split(" ")
        if(axis == "forward"): 
            forward_dist += int(value)
        elif (axis == "up"): 
            depth -= int(value)
        elif(axis == "down"): 
            depth += int(value)
        else: 
            assert false
    return [forward_dist, depth]

def extractDistancesWithAim(inputs):
    forward_dist = 0
    depth = 0 
    aim = 0
    for cmd in inputs: 
        axis, value = cmd.split(" ")
        value = int(value)
        if(axis == "forward"): 
            forward_dist += (value)
            depth += aim * value
        elif (axis == "up"): 
            aim -= value
        elif(axis == "down"): 
            aim += value
        else: 
            assert false
    return [forward_dist, depth]


def main():
    inputs = extractInputs()
    forward_dist, depth = extractDistances(inputs)
    answer_1 = forward_dist *depth 
    fwd_dist, d = extractDistancesWithAim(inputs)
    answer_2 = fwd_dist * d
    print(f"The first answer is {answer_1} and the second answer is {answer_2}")

if __name__ == "__main__":
    main()