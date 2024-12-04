import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def count_mas_x_shape():
    data = read_file('./aoc_2024/input_folder/day_4_input.txt')
    count = 0
    rows, cols = len(data), len(data[0])
    data = [row.lower() for row in data]
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            left_diag = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
            right_diag = data[i+1][j-1] + data[i][j] + data[i-1][j+1]
            
            if left_diag == "mas" and right_diag == "mas":
                count += 1
            if left_diag == "sam" and right_diag == "sam":
                count += 1
            if left_diag == "mas" and right_diag == "sam":
                count += 1
            if left_diag == "sam" and right_diag == "mas":
                count += 1
    
    return count


print(f"Total found:{count_mas_x_shape()}")
