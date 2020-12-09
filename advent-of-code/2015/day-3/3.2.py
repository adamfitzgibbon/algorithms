with open("input.txt", 'r') as f:
  visits = { (0,0) }
  currentS = 0,0
  currentR = 0,0
  for line in f:
    for i, c in enumerate(line.rstrip()):
      if i % 2 == 0:
        x, y = currentS
      else:
        x, y = currentR
      if c == "<":
        x -= 1
      if c == "v":
        y -= 1
      if c == ">":
        x += 1
      if c == "^":
        y += 1
      if i % 2 == 0:
        currentS = x,y
        visits.add(currentS)
      else:
        currentR = x,y
        visits.add(currentR)
  print(len(visits))