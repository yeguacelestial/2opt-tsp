# 2-OP Heuristic
# a) Best Found Strategy
#    1. Read tour -> T
#    2. Compute f(T) of current T
#    3. 
# b) First Found Strategy

import sys
import openpyxl
from itertools import permutations
from itertools import combinations

def main():
    try:
        filename = sys.argv[1]
        tour = read_tour(filename)
        print(best_found(tour))
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


def best_found(tour):
    list_of_combinations = get_combitations(tour)

    return list_of_combinations


def first_found(tour):
    return


def distance(exl, i, j):
    # Open Workbook object
    wb_obj = openpyxl.load_workbook(exl)

    # Get workbook active sheet object from active attribute
    sheet_obj = wb_obj.active

    # Cell object
    cell_obj = sheet_obj.cell(row = i, column = j)
    distance_value = cell_obj.value

    return distance_value


def obj_f(distances:list):
    objective = 0
    for d in distances:
        objective += d
    
    return objective


def get_combitations(tour):
    comb = combinations(tour, 2)
    comb_list = list(comb)

    return comb_list


if __name__ == '__main__':
    main()