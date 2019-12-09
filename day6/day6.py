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


def calculate_orbits():
  direct_orbits = len(tree.all_nodes())
  indirect_orbits = 0
  for x in tree.all_nodes():
    indirect_orbits = indirect_orbits + (tree.depth(x.identifier) -1)

  print('direct + indirect',  direct_orbits + indirect_orbits)

def minimum_orbit_transfers():
  santa = tree.get_node('SAN')
  me = tree.get_node('YOU')
  transfers = 0

  while me.identifier != santa.identifier:
    if tree.depth(me) > tree.depth(santa):
      me = tree.parent(me.identifier)
      transfers = transfers + 1
    elif tree.depth(santa) > tree.depth(me):
      santa = tree.parent(santa.identifier)
      transfers = transfers + 1
    else:
      me = tree.parent(me.identifier)
      santa = tree.parent(santa.identifier)
      transfers = transfers + 2
  print('transfers', transfers - 2)

calculate_orbits()
minimum_orbit_transfers()