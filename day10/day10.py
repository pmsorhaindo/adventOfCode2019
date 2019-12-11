
def load_file():
  f = open('input.txt', 'r')
  asteroids = []
  y = 0
  for line in f:
    x = 0
    splitLine = list(line.rstrip())
    for pointContent in splitLine:
      if pointContent is '#':
        asteroids.append((x,y))
      x += 1
    y += 1
  return asteroids

def intercepts(p1, p2, p3):
  px1, py1 = p1
  px2, py2 = p2
  px3, py3 = p3

  if(px1 - px2) != 0:
    m = abs(py1 - py2) / abs(px1 - px2)
    c = py1 - m*px1
    return py3 == m*px3 + c
  elif py1 == py2 and py2 == py3:
    return True
  else:
    return False



def calculate_best():
  asteroids = load_file()
  asteroids_seen = []

  for p1 in asteroids:
    p1Count = 0
    for p2 in asteroids:
      if p2 != p1:
        hasIntercept = False
        for x in asteroids:
          if x != p1 and x != p2:
            if intercepts(x, p1, p2):
              hasIntercept = True
              break
        if hasIntercept == False:
          p1Count +=1
    asteroids_seen.append(p1Count)
  print(asteroids[asteroids_seen.index(max(asteroids_seen))])

# intercept issue
# print(intercepts((1,4), (1,7), (1,9)))

