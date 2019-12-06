from treelib import Node, Tree, exceptions
  

tree = Tree()

def add_orbit(orbitee, orbiter):
  tree.create_node(orbiter, orbiter, parent=orbitee)

def init_tree():
  tree.create_node('COM', 'COM')
  f = open('input.txt', 'r')
  for line in f:
    line_info = line.split(')')
    orbitee = line_info[0].rstrip()
    orbiter = line_info[1].rstrip()

    if orbitee == 'COM':
      add_orbit(orbitee, orbiter)

def populate_tree():
  not_fully_parsed = True
  while not_fully_parsed == True:
    f = open('input.txt', 'r')
    not_fully_parsed = False
    for line in f:
      line_info = line.split(')')
      orbitee = line_info[0].rstrip()
      orbiter = line_info[1].rstrip()

      try:
        add_orbit(orbitee, orbiter)
      except exceptions.NodeIDAbsentError:
        not_fully_parsed = True
      except exceptions.DuplicatedNodeIdError:
        pass

init_tree()
populate_tree()

print(len(tree.paths_to_leaves()))
