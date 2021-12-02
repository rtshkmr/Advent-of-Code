#!/usr/bin/env python3
"""
AOC Day 1
"""

__author__ = "Ritesh Kumar"
__version__ = "0.1.0"
__license__ = "MIT"


def extractInputs(): 
    inputs = open("input").readlines()
    return list(map(lambda x: int(x.rstrip("\n")), inputs))

def countSingleIncreases(inputs):
    counter = 0
    for idx in range(len(inputs)):
        if (idx == 0): continue
        counter += 1 if inputs[idx] > inputs[idx - 1] else 0
    return counter


def main():
    answer_first = countSingleIncreases(extractInputs())
    print(f"This be the first answer: {answer_first}")

if __name__ == "__main__":
    main()