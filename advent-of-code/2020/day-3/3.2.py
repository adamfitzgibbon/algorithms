def count_trees (x_offset, y_offset, lines):
  trees = 0
  x = 0
  for i, line in enumerate(lines):
    if i % y_offset != 0:
      continue
    wrapped_x = x % len(line.rstrip())
    if line[wrapped_x] == "#":
      trees += 1
    x += x_offset
  return trees

with open("3_input.txt", 'r') as f:
  lines = f.readlines()
  print(count_trees(1,1,lines) * count_trees(3,1,lines) * count_trees(5,1,lines) * count_trees(7,1,lines) * count_trees(1,2,lines))