def solve_pythagorean(upper_z):
    solutions = []
    for z in range(1, upper_z + 1):
        for x in range(1, z):
            for y in range(x, z):
                if x**2 + y**2 == z**2:
                    solutions.append((x, y, z))
    return solutions

def main():
    print(solve_pythagorean(20))

if __name__ == "__main__":
    main()
