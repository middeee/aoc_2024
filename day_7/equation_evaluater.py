import itertools
import numpy as np

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def create_equations(data):
    cleaned_equations = []
    for line in data:
        equation = line.split(':')
        result = int(equation[0].strip())
        operands = equation[1].split(" ")
        cleaned_operands = [int(o) for o in operands if o != '']
        cleaned_equations.append((result, cleaned_operands))
    return cleaned_equations

def evaluate_equations(equations):
    def apply_operators(numbers, operators):
        result = numbers[0]
        for num, op in zip(numbers[1:], operators):
            if op == '+':
                result += num
            elif op == '*':
                result *= num
        return result

    sum_of_correct_equations = 0

    for result, equation in equations:
        correct_equation = False
        operator_combinations = itertools.product(['+', '*'], repeat=len(equation)-1)
        
        for operators in operator_combinations:
            if apply_operators(equation, operators) == result:
                correct_equation = True
                break
        
        if correct_equation:
            sum_of_correct_equations += result

    return sum_of_correct_equations

def solve():
    data = read_file('input_folder/day_7_input.txt')
    equations = create_equations(data)
    result = evaluate_equations(equations)
    return result

print(solve())