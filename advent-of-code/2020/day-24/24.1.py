"""in case anyone happens upon this and gets the wrong idea, the variable names in this problem are referring to black and white tiles"""

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  commands = []
  for line in lines:
    command = []
    stash = None
    for c in line:
      if stash:
        command.append(stash + c)
        stash = None
      elif c not in ("n", "s"):
        command.append(c)
      else:
        stash = c
    commands.append(command)
  
  count = {}
  for command in commands:
    x,y = 0,0
    for c in command:
      if c == "e":
        x += 2
      if c == "se":
        x += 1
        y -= 1
      if c == "sw":
        x -= 1
        y -= 1
      if c == "w":
        x -= 2
      if c == "nw":
        x -= 1
        y += 1
      if c == "ne":
        x += 1
        y += 1
      
    if (x,y) in count:
      count[x,y] = not count[x,y]
    else:
      count[x,y] = True

  print(sum(count.values()))