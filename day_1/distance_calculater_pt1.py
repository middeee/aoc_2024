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
    left = np.array(left, dtype=float)
    right = np.array(right, dtype=float)
    final_data = np.abs(left - right)
    
    total_distance = sum(final_data)
        
    print(total_distance)
    return total_distance

distance_calculater('input_folder/day_1_input.txt')