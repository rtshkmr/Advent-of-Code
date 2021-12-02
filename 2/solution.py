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

def main():
    inputs = extractInputs()
    forward_dist, depth = extractDistances(inputs)
    answer = forward_dist *depth 
    print(f"The answer is {answer}")

if __name__ == "__main__":
    main()