with open("input.txt", 'r') as f:
  visits = { (0,0) }
  current = 0,0
  for line in f:
    for c in line.rstrip():
      x, y = current
      if c == "<":
        current = x-1,y
      if c == "v":
        current = x,y-1
      if c == ">":
        current = x+1,y
      if c == "^":
        current = x,y+1
      visits.add(current)
  print(len(visits))