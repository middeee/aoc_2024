import numpy as np
import regex as re

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def multiplier(substring):
    value1 = np.array(re.findall(r'\(([0-9]+)',substring),int)[0] 
    value2 = np.array(re.findall(r',([0-9]+)',substring),int)[0]
    return value1 * value2

def read_memory():
    data = read_file("./inputs/input_day_3.txt")
    data_string = str(data)
    instructions = re.findall(r'mul\([0-9]+,[0-9]+\)', data_string)
    sum = 0
    for instruction in instructions:
        sum += multiplier(instruction)
    return sum
print(read_memory())


