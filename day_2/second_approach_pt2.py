import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def is_safe(report):
    def is_valid_sequence(values):
        increasing = all(values[i] < values[i+1] for i in range(len(values)-1))
        decreasing = all(values[i] > values[i+1] for i in range(len(values)-1))
        valid_differences = all(1 <= abs(values[i] - values[i+1]) <= 3 for i in range(len(values)-1))
        return (increasing or decreasing) and valid_differences

    if is_valid_sequence(report):
        return True

    for i in range(len(report)):
        temp = np.delete(report, i)
        if is_valid_sequence(temp):
            return True

    return False

def validator(file_path):
    data = read_file(file_path)
    safe_count = 0

    for line in data:
        report = np.array(line.split(), dtype=int)
        if is_safe(report):
            safe_count += 1

    print(f"Number of safe: {safe_count}")
    return safe_count

print(validator('input_folder/day_2_input.txt'))
