import numpy as np
import regex as re

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def count_string():
    data = read_file('./aoc_2024/input_folder/day_4_input.txt')
    count = 0
    for row in data:
        count += row.lower().count('xmas')
        count += row[::-1].lower().count('xmas')
    for col in zip(*data):
        col_str = ''.join(col).lower()
        count += col_str.count('xmas')
        count += col_str[::-1].count('xmas')
    return count
          
    
def count_diagonals(data):
    count = 0
    rows, cols = len(data), len(data[0])
    array = np.array([list(row) for row in data])

    for offset in range(-rows + 1, cols):
        diag = ''.join(array.diagonal(offset)).lower()
        count += diag.count('xmas')
        count += diag[::-1].count('xmas')

    flipped_array = np.fliplr(array)
    for offset in range(-rows + 1, cols):
        diag = ''.join(flipped_array.diagonal(offset)).lower()
        count += diag.count('xmas')
        count += diag[::-1].count('xmas')

    return count

data = read_file('./aoc_2024/input_folder/day_4_input.txt')   
print(count_diagonals(data))                
print(count_string())
print(f"Total count: {count_string() + count_diagonals(data)}")
