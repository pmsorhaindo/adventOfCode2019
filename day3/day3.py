import math
import numpy as  np

f = open('input.txt', 'r')

f = ['R8,U5,L5,D3',
'U7,R6,D4,L4']

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
      currentX = currentX + distance
    if (direction == 'L'):
      currentX = currentX - distance
    if (direction == 'U'):
      currentY = currentY + distance
    if (direction == 'D'):
      currentY = currentY - distance
    
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

print(originX, originY)
zero_shape = np.zeros(shape=(largestLimitX + abs(largestXOffset), largestLimitY+ abs(largestYOffset)))

print(zero_shape)