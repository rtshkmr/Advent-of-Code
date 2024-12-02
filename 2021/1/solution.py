#!/usr/bin/env python3
"""
AOC Day 1
"""

__author__ = "Ritesh Kumar"


def extractInputs(): 
    inputs = open("input").readlines()
    return list(map(lambda x: int(x.rstrip("\n")), inputs))

def countSingleIncreases(inputs):
    counter = 0
    for idx in range(len(inputs)):
        if (idx == 0): continue
        counter += 1 if inputs[idx] > inputs[idx - 1] else 0
    return counter

# returns a list of values representing sum of sliding windows of size 3:
def mergeWindows(inputs): 
    merged_inputs = []
    for idx in range(len(inputs) - 2): # note the ending boundary here
        merged_inputs.append(sum(inputs[idx:idx+3]))
    return merged_inputs   

def main():
    inputs = extractInputs()
    answer_first = countSingleIncreases(inputs)
    answer_second = countSingleIncreases(mergeWindows(inputs))
    print(f"This be the first answer: {answer_first} and this be the second answer: {answer_second}")

if __name__ == "__main__":
    main()