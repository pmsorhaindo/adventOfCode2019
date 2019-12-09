import math
import numpy as  np
import pandas as pd

f = open('input.txt', 'r')

f = ['R8,U5,L5,D3',
'U7,R6,D4,L4']

def go_right(grid, currentX, currentY, distance, wire_no):
  for i in range(currentX, currentX+distance):
    if wire_no == 1:
      grid[i+1][currentY] = '-'
    elif (grid[i+1][currentY] == '|' or grid[i+1][currentY] == '-'):
      grid[i+1][currentY] = 'X'
    else:
      grid[i+1][currentY] = '~'
  return (grid, currentX+distance, currentY)

def go_left(grid, currentX, currentY, distance, wire_no):
  for i in range(currentX, currentX-distance, -1):
    if wire_no == 1:
      grid[i-1][currentY] = '-'
    elif (grid[i-1][currentY] == '|' or grid[i-1][currentY] == '-'):
      grid[i-1][currentY] = 'X'
    else:
      grid[i-1][currentY] = '~'
  return (grid, currentX-distance, currentY)

def go_up(grid, currentX, currentY, distance, wire_no):
  for i in range(currentY, currentY-distance, -1):
    if wire_no == 1:
      grid[currentX][i-1] = '|'
    elif (grid[currentX][i-1] == '|' or grid[currentX][i-1] == '-'):
      grid[currentX][i-1] = 'X'
    else:
      grid[currentX][i-1] = '/'
  return (grid, currentX, currentY-distance)

def go_down(grid, currentX, currentY, distance, wire_no):
  for i in range(currentY, currentY+distance):
    if wire_no == 1:
      grid[currentX][i+1] = '|'
    elif (grid[currentX][i+1] == '|' or grid[currentX][i+1] == '-'):
      grid[currentX][i+1] = 'X'
    else:
      grid[currentX][i+1] = '/'
  return (grid, currentX, currentY+distance)

def draw_wire(grid, wire, currentX, currentY, wire_no):
  for x in wire:
    direction = x[0]
    distance = int(x[1:])
    if (direction == 'R'):
      (grid, currentX, currentY) = go_right(grid, currentX, currentY, distance, wire_no)
    if (direction == 'L'):
      (grid, currentX, currentY) = go_left(grid, currentX, currentY, distance, wire_no)
    if (direction == 'U'):
      (grid, currentX, currentY) = go_up(grid, currentX, currentY, distance, wire_no)
    if (direction == 'D'):
      (grid, currentX, currentY) = go_down(grid, currentX, currentY, distance, wire_no)
  return grid

def calculate_dimension(directions):
  maxLimitX = 0
  maxLimitY = 0
  minLimitX = 0
  minLimitY = 0
  currentX = 0
  currentY = 0

  for x in directions:
    direction = x[0]
    distance = int(x[1:])
    if (direction == 'R'):
      currentX = currentX + distance + 1
    if (direction == 'L'):
      currentX = currentX - distance - 1
    if (direction == 'U'):
      currentY = currentY + distance + 1
    if (direction == 'D'):
      currentY = currentY - distance - 1
    
    if currentX > maxLimitX:
      maxLimitX = currentX
    if currentX < minLimitX:
      minLimitX = currentX
    if currentY > maxLimitY:
      maxLimitY = currentY
    if currentY < minLimitY:
      minLimitY = currentY
  return (minLimitX, minLimitY, maxLimitX, maxLimitY)

largestXOffset = 0
largestYOffset = 0
largestLimitX = 0
largestLimitY = 0

for line in f:
  minLimitX, minLimitY, maxLimitX, maxLimitY = calculate_dimension(line.split(','))

  if(minLimitX < largestXOffset):
    largestXOffset = minLimitX
  if (minLimitY < largestYOffset):
    largestYOffset = minLimitY
  if largestLimitX < maxLimitX:
    largestLimitX = maxLimitX
  if largestLimitY < maxLimitY:
    largestLimitY = maxLimitY

originX = abs(largestXOffset)
originY = abs(largestYOffset)

grid = pd.DataFrame(np.empty((largestLimitX  + abs(largestXOffset) + 2, largestLimitY + abs(largestYOffset) + 2), dtype = np.str))
print(originX, originY)

grid[:][:] = '.'
grid[0][8] = 'o'
wire_no = 1

for line in f:
  grid = draw_wire(grid, line.split(','), 0, 8, wire_no)
  wire_no = wire_no + 1

for x in range(0, largestLimitX + abs(largestXOffset) + 1):
  for y in range(0, largestLimitY + abs( largestYOffset) + 1):
    if grid[x][y] == 'X':
      print(x, y, abs(x-0), abs(y-8), abs(x-0)+ abs(y-8))

print(grid)