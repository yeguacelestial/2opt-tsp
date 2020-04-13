# 2-OP Heuristic
# a) Best Found Strategy
#    1. Read tour -> T
#    2. Compute f(T) of current T
#    3. 
# b) First Found Strategy

import sys
import openpyxl

def main():
    try:
        filename = sys.argv[1]
        tour = read_file(filename)
        best_found(tour)
    except:
        pass

def read_file(filename):
    try:
        tour = []

        with open(f'{filename}', 'r') as f:
            line = list(f.read())
            for c in line:
                try:
                    tour.append(int(c))
                except:
                    pass
            print(tour)
            return tour
    except:
        print("[-] Couldn't read file.")


def best_found(tour):
    
    return


def first_found(tour):
    return


def distance(exl, i, j):
    # Open Workbook object
    wb_obj = openpyxl.load_workbook(exl)

    # Get workbook active sheet object from active attribute
    sheet_obj = wb_obj.active

    # Cell object
    cell_obj = sheet_obj.cell(row = i, column = j)

    return print(cell_obj.value)

if __name__ == '__main__':
    main()