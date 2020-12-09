with open("input.txt", 'r') as f:
  sum = 0
  group = set()
  for line in f:
    line = line.rstrip()
    if line == "":
      sum += len(group)
      group = set()
      continue
    for c in line:
      group.add(c)
  sum += len(group)
  print(sum)
