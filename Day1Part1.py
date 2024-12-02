left_values = []
right_values = []

with open('Inputs/AdventOfCode1.txt', 'r') as file:
    for line in file:
        left, right = line.strip().split()
        left_values.append(int(left))
        right_values.append(int(right))






def calculate_list_distance(left_list, right_list):
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    distances = [abs(left - right) for left, right in zip(sorted_left, sorted_right)]
    
    return sum(distances)
print(calculate_list_distance(left_values, right_values))


