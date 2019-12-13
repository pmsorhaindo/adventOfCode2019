import itertools
f = open('input.txt', 'r')

class Moon:
  def __init__(self, x, y, z):
    self.x = int(x)
    self.y = int(y)
    self.z = int(z)
    self.vx = 0
    self.vy = 0
    self.vz = 0

  def move(self):
    self.x = self.x + self.vx
    self.y = self.y + self.vy
    self.z = self.z + self.vz

  def __repr__(self):
    return 'x:'+str(self.x)+' y:'+str(self.y)+' z:'+str(self.z)+'\nvx:'+str(self.vx)+' vy:'+str(self.vy)+' vz:'+str(self.vz)+'.\n'

  def __str__(self):
    return 'Moon()'

  def getPotEnergy(self):
    return abs(self.x) + abs(self.y) + abs(self.z)

  def getKinEnergy(self):
    return abs(self.vx) + abs(self.vy) + abs(self.vz)

moons = []
  

for line in f:
  x = line.split(',')
  z = list(map(lambda a: a.replace(' ', '').replace('<', '').replace('>', '').rstrip().split('='), x))
  q = z[0][1]
  w = z[1][1]
  e = z[2][1]
  moons.append(Moon(q,w,e))

def apply_gravity(moon1, moon2):
  if moon1.x < moon2.x:
    moon1.vx += 1
    moon2.vx -= 1
  elif moon1.x > moon2.x:
    moon2.vx +=1
    moon1.vx -=1

  if moon1.y < moon2.y:
    moon1.vy += 1
    moon2.vy -= 1
  elif moon1.y > moon2.y:
    moon2.vy +=1
    moon1.vy -=1

  if moon1.z < moon2.z:
    moon1.vz += 1
    moon2.vz -= 1
  elif moon1.z > moon2.z:
    moon2.vz +=1
    moon1.vz -=1
  
def apply_gravities():
  z = list(itertools.combinations(list(range(4)), 2))
  for x, y in z:
    apply_gravity(moons[x],moons[y])
    

print(moons)
for p in range(1000):
  apply_gravities()
  for i in moons:
    i.move()

kin = map(lambda g: g.getKinEnergy(), moons)
pot = map(lambda g: g.getPotEnergy(), moons)

sum = 0
for j,k in list(zip(kin,pot)):
  sum += j*k

print(sum)