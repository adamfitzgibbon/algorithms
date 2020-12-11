def check_seat(lines, i, j):
  if lines[i][j] == "L":
    if i > 0:
      if lines[i-1][j] == "#":
        return False
      if j > 0 and lines[i-1][j-1] == "#":
        return False
      if j < len(lines[i]) - 1 and lines[i-1][j+1] == "#":
        return False
    if i < len(lines) - 1:
      if lines[i+1][j] == "#":
        return False
      if j > 0 and lines[i+1][j-1] == "#":
        return False
      if j < len(lines[i]) - 1 and lines[i+1][j+1] == "#":
        return False
    if j > 0 and lines[i][j-1] == "#":
      return False
    if j < len(lines[i]) - 1 and lines[i][j+1] == "#":
      return False
    return True
  
  # so it's occupied
  occupiedCount = 0
  if i > 0:
    if lines[i-1][j] == "#":
      occupiedCount += 1
    if j > 0 and lines[i-1][j-1] == "#":
      occupiedCount += 1
    if j < len(lines[i]) - 1 and lines[i-1][j+1] == "#":
      occupiedCount += 1
  if i < len(lines) - 1:
    if lines[i+1][j] == "#":
      occupiedCount += 1
    if j > 0 and lines[i+1][j-1] == "#":
      occupiedCount += 1
    if j < len(lines[i]) - 1 and lines[i+1][j+1] == "#":
      occupiedCount += 1
  if j > 0 and lines[i][j-1] == "#":
    occupiedCount += 1
  if j < len(lines[i]) - 1 and lines[i][j+1] == "#":
    occupiedCount += 1
  return not occupiedCount >= 4:

def print_board(lines):
  for line in copy:
    print(line)
  print()

def check_diff(copy, copy2):
  for i, line in enumerate(copy):
    for j, c in enumerate(line):
      if c != "." and copy2[i][j] != c:
        return True
  return False

def count_occupied_seats(lines):
  counter = 0
  for line in lines:
    for c in line:
      if c == "#":
        counter += 1
  return counter

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  copy = []
  copy2 = []
  for line in lines:
    copy.append([c for c in line])
    copy2.append([c for c in line])
  while True:
    for i, line in enumerate(copy):
      for j, c in enumerate(line):
        if c != ".":
          copy2[i][j] = "#" if check_seat(copy, i, j) else "L"
    # print_board(copy2)
    if not check_diff(copy, copy2):
      print(count_occupied_seats(copy))
      exit(0)
    copy = []
    for line in copy2:
      copy.append([c for c in line])