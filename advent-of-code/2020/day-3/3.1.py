with open("input.txt", 'r') as f:
  x = 0
  trees = 0
  for line in f:
    wrapped_x = x % len(line.rstrip())
    if line[wrapped_x] == "#":
      trees += 1
    x += 3
  print(trees)