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

import numpy as np
import time

def solve_pythagorean_mesh(upper_z):
    solutions = []
    for z in range(1, upper_z + 1):
        x, y = np.meshgrid(range(1, z), range(1, z))
        test_z = square(x) + square(y) 
        if np.any(test_z == square(z)):
            y_vals, x_vals = np.where(test_z == square(z))
            for (x_val, y_val) in zip(x_vals, y_vals):
                    if x_val <= y_val:
                        solutions.append((int(x_val) + 1, int(y_val) + 1, z))
    return solutions

import math
def solve_pythagorean_gpt(upper_z):
    solutions = []
    for z in range(1, upper_z + 1):
        z2 = z * z
        for x in range(1, z):
            y2 = z2 - x * x
            y = int(math.isqrt(y2))
            if y >= x and y < z and y * y == y2:
                solutions.append((x, y, z))
    return solutions

def main():
    st = time.time()
    solve_pythagorean(200)
    et = time.time()
    print("Elapsed (nested loop):", et - st)
    st = time.time()
    solve_pythagorean_mesh(200)
    et = time.time()
    print("Elapsed (meshgrid)):", et - st)
    st = time.time()
    solve_pythagorean_gpt(200)
    et = time.time()
    print("Elapsed (gpt)):", et - st)

if __name__ == "__main__":
    main()
