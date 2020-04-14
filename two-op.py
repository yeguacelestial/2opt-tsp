# 2-OP Heuristic
# a) Best Found Strategy
# 
# b) First Found Strategy

import sys
import openpyxl
from itertools import permutations
from itertools import combinations

def main():
    try:
        tour_file = sys.argv[1]
        tour = read_tour(tour_file)
        matrix_xl_file = sys.argv[2]

        # a) Best Found Strategy
        best_found(tour, matrix_xl_file)

        # b) First Found strategy

    except:
        pass


def read_tour(filename):
    try:
        tour = []

        with open(f'{filename}', 'r') as f:
            line = list(f.read())

            for c in line:
                try:
                    tour.append(int(c))
                except:
                    pass

            return tour

    except:
        print("[-] Couldn't read file.")


def best_found(tour, exl):
    output_str = "\na) BEST FOUND TRATEGY IN 2-OPT\n"
    output_str += f'T = {tour}\n'

    list_of_combinations = get_combinations(tour)
    filtered_combs = filter_combinations(list_of_combinations)
    distances = []

    for comb in filtered_combs:
        d = distance(exl, comb[0], comb[1])
        distances.append(d)
    
    output_str += f'Current f(T) = '
    for comb in filtered_combs:
        if comb == filtered_combs[-1]:
            output_str += f'd({comb[0]},{comb[1]})'
        else:
            output_str += f' d({comb[0]},{comb[1]}) + '

    output_str += f'\nCurrent f(T) = '
    for d in distances:
        if d == distances[-1]:
            output_str += f'{d}'
        else:
            output_str += f'{d} + '

    objective_function = obj_f(distances)

    output_str += f'\nCurrent f(T) = {objective_function}'
    print(output_str)

    return objective_function


def first_found(tour):
    return


def two_opt(a, b):
    return


def distance(exl, i, j):
    # Open Workbook object
    wb_obj = openpyxl.load_workbook(exl)

    # Get workbook active sheet object from active attribute
    sheet_obj = wb_obj.active

    # Cell object
    cell_obj = sheet_obj.cell(row = i, column = j)

    if cell_obj.value == None:
        cell_obj = sheet_obj.cell(row = j, column = i)

    distance_value = cell_obj.value

    return distance_value


def obj_f(distances:list):
    objective = 0
    for d in distances:
        objective += d
    
    return objective


def get_combinations(tour):
    comb = combinations(tour, 2)
    comb_list = list(comb)

    return comb_list


def filter_combinations(combinations):
    comb_copy = combinations
    first_index_list = []
    filtered_combs = []

    # Add all combinations
    for comb in comb_copy:
        if comb[0] not in first_index_list:
            filtered_combs.append(comb)
            first_index_list.append(comb[0])

        else:
            pass
    
    # Add last combination
    last_index_list = []
    for comb in comb_copy:
        last_index_list.append(comb[1])
    
    max_index = max(last_index_list)
    first_index = first_index_list[0]

    last_combination = (max_index, first_index)
    filtered_combs.append(last_combination)

    return filtered_combs


if __name__ == '__main__':
    main()