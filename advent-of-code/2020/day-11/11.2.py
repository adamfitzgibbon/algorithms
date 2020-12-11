def check_visible(lines, i, j):
  counter = 0
  temp = i
  while temp < len(lines) - 1:
    temp += 1
    val = lines[temp][j]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp = i
  while temp > 0:
    temp -= 1
    val = lines[temp][j]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp = j
  while temp < len(lines[i]) - 1:
    temp += 1
    val = lines[i][temp]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp = j
  while temp > 0:
    temp -= 1
    val = lines[i][temp]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp, temp2 = i, j
  while temp < len(lines) - 1 and temp2 < len(lines[i]) - 1:
    temp += 1
    temp2 += 1
    val = lines[temp][temp2]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp, temp2 = i, j
  while temp > 0 and temp2 > 0:
    temp -= 1
    temp2 -= 1
    val = lines[temp][temp2]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp, temp2 = i, j
  while temp > 0  and temp2 < len(lines[i]) - 1:
    temp -= 1
    temp2 += 1
    val = lines[temp][temp2]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  temp, temp2 = i, j
  while temp < len(lines) - 1  and temp2 > 0:
    temp += 1
    temp2 -= 1
    val = lines[temp][temp2]
    if val != ".":
      counter += 1 if val == "#" else 0
      break
  return counter

def check_seat(lines, i, j):
  if lines[i][j] == "L":
    return check_visible(lines, i, j) == 0
  # so it's occupied
  return not check_visible(lines, i, j) >= 5

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