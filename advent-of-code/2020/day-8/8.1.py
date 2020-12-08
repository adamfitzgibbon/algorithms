with open("8_input.txt", 'r') as f:
  lines = f.readlines()
  i = 0
  acc = 0
  visited = set()
  while i < len(lines):
    line = lines[i].rstrip()
    op, arg = line.split(" ")
    if i in visited:
      print(acc)
      break
    else:
      visited.add(i)

    if op == "acc":
      if arg[0] == "+":
        acc += int(arg[1:]) 
      else:
        acc -= int(arg[1:])
    if op == "jmp":
      if arg[0] == "+":
        i += int(arg[1:]) - 1
      else:
        i -= (int(arg[1:]) + 1)
    
    i += 1