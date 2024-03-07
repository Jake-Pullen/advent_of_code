import sympy

with open(r'advent_of_code\2023\24\input.txt', 'r') as file:
    input_data = file.read()

test_input_data = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''

#input_data = test_input_data
input_lines = input_data.split('\n')

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in input_lines]

x_ref, y_ref, z_ref, vx_ref, vy_ref, vz_ref = sympy.symbols("x_ref, y_ref, z_ref, vx_ref, vy_ref, vz_ref")

equations = []

for i, (start_x, start_y, start_z, velocity_x, velocity_y, velocity_z) in enumerate(hailstones):
    equations.append((x_ref - start_x) * (velocity_y - vy_ref) - (y_ref - start_y) * (velocity_x - vx_ref))
    equations.append((y_ref - start_y) * (velocity_z - vz_ref) - (z_ref - start_z) * (velocity_y - vy_ref))
    if i < 2:
        continue
    solutions = [solution for solution in sympy.solve(equations) if all(value % 1 == 0 for value in solution.values())]
    if len(solutions) == 1:
        break
    
final_solution = solutions[0]

print(final_solution[x_ref] + final_solution[y_ref] + final_solution[z_ref])
