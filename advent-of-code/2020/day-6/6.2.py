with open("6_input.txt", 'r') as f:
  sum = 0
  group = {}
  groupCounter = 0
  for line in f:
    line = line.rstrip()
    if line == "":
      for val in group.values():
        if val == groupCounter:
          sum += 1
      group = {}
      groupCounter = 0
      continue
    for c in line:
      if c in group:
        group[c] += 1
      else:
        group[c] = 1
    groupCounter += 1
  for val in group.values():
    if val == groupCounter:
      sum += 1
  print(sum)
