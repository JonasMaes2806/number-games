def square(x):
    return x**2

a = 3

def solve_pythagorean(upper_z):
    solutions = []
    for z in range(1, upper_z + 1):
        for x in range(1, z):
            for y in range(x, z):
                if square(x) + square(y) == square(z):
                    solutions.append((x, y, z))
    return solutions

def main():
    print(solve_pythagorean(20))
if __name__ == "__main__":
    main()
