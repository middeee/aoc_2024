import numpy as np


# read from file
def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def distance_calculater(file_path):
    left, right = [], []
    data = read_file(file_path)
    for i in range(len(data)):
        left.append(data[i].split()[0])
        right.append(data[i].split()[1])
        
    left = sorted(left)
    right = sorted(right)   
    
    # find how many times each element in left appears in right
    total_distance = 0
    for i in range(len(left)):
        total_distance += right.count(left[i]) * int(left[i])
        
    print(total_distance)
    return total_distance

distance_calculater('input_folder/day_1_input.txt')