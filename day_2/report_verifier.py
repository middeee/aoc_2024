import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def check_distance(values):
    prev_value = values[0]
    for i in range(len(values)):
        value = values[i]
        diff = abs(prev_value - value)
        if diff > 3 or (diff == 0 and i != 0):
            return 1
        prev_value = value
    return 0

def validator():
    data = read_file('input_folder/day_2_input.txt')
    failed_count = 0
    
    for line in data:
        vals = np.array(line.split()).astype(int)
        sorted_vals = np.sort(vals)
        reverse_sorted_vals = np.sort(vals)[::-1]
        
        if not (np.array_equal(vals, sorted_vals) or np.array_equal(vals, reverse_sorted_vals)):
            failed_count += 1
        else:
            failed_count += check_distance(vals)
        
    success_count = len(data) - failed_count
    print(f"Success count: {success_count}")
    
    return success_count


print(validator())
        
        
        