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
    do_split = data_string.split("do()")
    do_instructions = ""
    for i in range(len(do_split)):
        dont_split = do_split[i].split("don't()")
        do_instructions += dont_split[0]

    instructions = re.findall(r'mul\([0-9]+,[0-9]+\)', do_instructions)
    sum = 0
    should_mul = True
    for instruction in instructions:
        if instruction == "do()": 
            should_mul = True
        elif instruction == "don't()":
            should_mul = False
        else:
            if should_mul:
                sum += multiplier(instruction)
    return sum
print(read_memory())


