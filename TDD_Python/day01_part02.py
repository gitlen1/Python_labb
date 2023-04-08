
def calculate_fuel(masses):
    fuel = 0
    for mass in masses:
        fuel += (mass // 3) - 2
    return fuel

masses = [12, 14, 1969, 100756]
total = calculate_fuel(masses)
print(total)

