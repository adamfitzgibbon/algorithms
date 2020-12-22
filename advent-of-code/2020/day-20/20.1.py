tiles = {}

class Tile:
  def __init__(self, id, tile):
    self.id = id
    self.tile = tile
    self.left = None
    self.right = None
    self.top = None
    self.bottom = None
    self.border = { "L": [], "T": [], "R": [], "B": []}
    for j, row in enumerate(tile):
      for i, val in enumerate(row):
        if j == 0:
          self.border["T"].append(val)
        if j == len(tile) - 1:
          self.border["B"].append(val)
        if i == 0:
          self.border["L"].append(val)
        if i == len(tile[0]) - 1:
          self.border["R"].append(val)
  
  def check_border_by_label(self, label):
    if label == "L":
      return bool(self.left)
    elif label == "R":
      return bool(self.right)
    elif label == "T":
      return bool(self.top)
    elif label == "B":
      return bool(self.bottom)
    raise Exception("Unrecognized label!")

  def set_neighbor_by_label(self, label, otherId):
    if label == "L":
      self.left = otherId
    elif label == "R":
      self.right = otherId
    elif label == "T":
      self.top = otherId
    elif label == "B":
      self.bottom = otherId
    else:
      raise Exception("Unrecognized label!")

  def get_paired_sides(self):
    return sum([bool(self.left), bool(self.right), bool(self.top), bool(self.bottom)])

  def match_border(self, otherTile):
    for label, border in self.border.items():
      if self.check_border_by_label(label):
        continue
      for otherLabel, otherBorder in otherTile.border.items():
        if otherTile.check_border_by_label(otherLabel):
          continue
        if border == otherBorder or list(reversed(border)) == otherBorder:
          self.set_neighbor_by_label(label, otherTile.id)
          otherTile.set_neighbor_by_label(otherLabel, self.id)

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  isTitle = True
  currentTitle = None
  currentTile = []
  for line in lines:
    if isTitle:
      isTitle = False
      currentTitle = line[-5:-1]
    elif not line:
      isTitle = True
      tiles[currentTitle] = Tile(currentTitle, currentTile)
      currentTile = []
    else:
      currentTile.append(list(line))
  tiles[currentTitle] = Tile(currentTitle, currentTile)
  currentTile = []
  
  for tile in tiles.values():
    for otherTile in tiles.values():
      if tile.id == otherTile.id:
        continue
      tile.match_border(otherTile)
  product = 1
  for tile in tiles.values():
    if tile.get_paired_sides() == 2:
      product *= int(tile.id)
  print(product)
      