# 2-OP Heuristic
# a) Best Found Strategy
#    1. Read tour -> T
#    2. Compute f(T) of current T
#    3. 
# b) First Found Strategy
import sys

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

def obj_f(tour):
    
    return

if __name__ == '__main__':
    main()