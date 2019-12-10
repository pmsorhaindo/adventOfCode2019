f = open('input.txt')
line = f.readline()

layers = []
file = list(line)
file2 = list(line)
file2.pop()
file.pop()

for i in range(100):
  layer = []
  for j in range(25 * 6):
    x = file.pop(0)
    layer.append(x)
  layers.append(layer)

count_list = list(map(lambda x : x.count('0'), layers))
indx = (count_list.index(min(count_list)))
print(layers[indx].count('1') * layers[indx].count('2'))

final_layer = ['.']*150

x = 149
for i in range(100*25*6, -1, -1):
  if (file2[i-1] != '2'):
    final_layer[x] = '#' if file2[i-1] == '1' else ' '
  x -= 1
  if x == -1:
    x = 149

composite_list = [final_layer[x:x+25] for x in range(0, len(final_layer),25)]
for x in composite_list:
  print(''.join(x))