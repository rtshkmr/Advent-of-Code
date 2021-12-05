#!/usr/bin/env python3
"""
AOC Day 3 - Binary Diagnostics
"""

__author__ = "Ritesh Kumar"


# assumption: the number of inputs is odd, else can't tell if more 1's or 0's for a single column
def solve_part_1(): 
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
    
def get_gamma_bits(input_bitstrings): 
    input_len = len(input_bitstrings)
    width = len(input_bitstrings[0])
    bit_counts = [0] * width # stores number of bits set per place
    for elem in input_bitstrings: 
        for idx in range(width): 
            bit_counts[idx] += 1 if elem[idx] == "1" else 0
    gamma_bits = [1 if count >= input_len / 2 else 0 for count in bit_counts] # contains the most common value in respective bit positions
    return gamma_bits

def calculate_rating(rating, input_bitstrings): 
    idx = 0
    gamma_bits = get_gamma_bits(input_bitstrings)
    oxygen_rating_predicate = lambda bitstring, idx, gamma_bits: int(bitstring[idx]) == gamma_bits[idx]
    carbon_rating_predicate = lambda bitstring, idx, gamma_bits: int(bitstring[idx]) ^ gamma_bits[idx] == 1
    predicate =  oxygen_rating_predicate if rating == "oxygen" else carbon_rating_predicate
    while(len(input_bitstrings) > 1 ):
        input_bitstrings = [bitstring for bitstring in input_bitstrings if predicate(bitstring, idx, gamma_bits)]
        gamma_bits = get_gamma_bits(input_bitstrings)
        idx += 1 
    return int(input_bitstrings[0], 2)
    

def solve_part_2(): 
    input_bitstrings = list(map(lambda x: (x.rstrip("\n")), open("input").readlines()))
    oxygen_generator_rating =  calculate_rating("oxygen", input_bitstrings)
    co2_rating = calculate_rating("co2", input_bitstrings)
    return oxygen_generator_rating * co2_rating

def main():
    print(f"The answer for part 1 is {solve_part_1()} and for part 2 is {solve_part_2()}")

if __name__ == "__main__":
    main()