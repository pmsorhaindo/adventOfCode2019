from functools import reduce, partial

lower_bound = 158126
upper_bound = 624574
num = lower_bound
validCount = 0


def hasDouble(list):
  foundDouble = False
  for i in range(0, len(list)-1):
    if i < (len(list)-1):
      foundDouble = foundDouble or (list[i] == list[i+1] and list.count(list[i]) == 2)
  return foundDouble

def isAscending(list):
  isAscending = True
  for i in range(0, len(list)-1):
    if i < (len(list)-1):
      isAscending = isAscending and list[i] <= list[i+1]
  return isAscending

def validate_number(numb):
  str_numb = str(numb)
  list_numb = list(str_numb)
  hasDbl = hasDouble(list_numb)
  isAsc = isAscending(list_numb)
  return hasDbl and isAsc

while num <=upper_bound:
  if(validate_number(num)):
    validCount = validCount + 1
  num = num + 1

print(validCount)