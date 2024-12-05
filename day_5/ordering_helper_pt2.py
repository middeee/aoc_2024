import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def find_next(rules, order):
    values = [v for k,v in rules.items() if k in order]
    rule_values = [item for sublist in values for item in sublist]
    for i in range(len(order)):
        if order[i] not in rule_values:
            return order[i], i
    return order[0],0

def is_correct_order(rules, order):
    values = [v for k,v in rules.items() if k in order]
    rule_values = [item for sublist in values for item in sublist]
    if order[0] not in rule_values or len(order) == 1:
        return True
    
    return False

def find_middle_value(rules, order):
    result_order = []
    checking_order = [o for o in order]
    current_order = [o for o in order]
    while len(checking_order) > 0:
        correct = is_correct_order(rules, checking_order)
        if correct:
            checking_order.pop(0)
        else:
            break
        
    if checking_order == []:
        return 0    
    while len(result_order) < len(order):
        next_value, index = find_next(rules, current_order)
        result_order.append(next_value)
        current_order.pop(index)
    
        
    middle_value = result_order[len(result_order) // 2]
    return middle_value
                            
def order_data(data):
    rules = {}
    orders = []
    for row in data:
        if len(row) == 5:
            k,v = row.split('|')[0], row.split('|')[1]
            if rules.get(k):
                rules[k].append(v)
            else:
                rules[k] = [v]
        elif len(row) > 5:
            orders.append(row.split(','))

    return rules, orders

def solve():
    rules, orders = order_data(read_file('./input_folder/day_5_input.txt'))
    return sum([int(find_middle_value(rules, order)) for order in orders])
    


print(solve())