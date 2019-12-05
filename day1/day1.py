import math
f = open('input.txt', 'r')
y = 0

def calculate_fuel(mass):
  fuel = calculate_fuel_for_mass(mass)
  if calculate_fuel_for_mass(fuel) > 0:
    fuel = fuel + calculate_fuel(fuel)
  return fuel

def calculate_fuel_for_mass(mass):
  return math.floor(float(mass) / 3.0 ) - 2

for x in f:
  y += calculate_fuel(x)

print(y)