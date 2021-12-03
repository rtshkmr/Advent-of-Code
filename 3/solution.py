#!/usr/bin/env python3
"""
AOC Day 3
"""

__author__ = "Ritesh Kumar"


# assumption: the number of inputs is odd, else can't tell if more 1's or 0's for a single column
def solve(): 
    inputs = list(map(lambda x: (x.rstrip("\n")), open("input").readlines()))
    input_len = len(inputs)
    width = len(inputs[0])
    bit_counts = [0] * width # stores number of bits set per place
    for elem in inputs: 
        for idx in range(len(elem)): 
            bit_counts[idx] += 1 if elem[idx] == "1" else 0
    gamma_bits = [1 if count > input_len / 2 else 0 for count in bit_counts]
    epsilon_bits = [0 if count > input_len / 2 else 1 for count in bit_counts]
    gamma = int("".join(str(bit) for bit in gamma_bits), 2)
    epsilon = int("".join(str(bit) for bit in epsilon_bits), 2)
    return gamma * epsilon
    

    

def main():
    print(f"The answer for part 1 is {solve()}")

if __name__ == "__main__":
    main()