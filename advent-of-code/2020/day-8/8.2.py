def execute(lines, visited, swap):
  acc = 0
  i = 0
  while i < len(lines):
    line = lines[i].rstrip()
    op, arg = line.split(" ")
    if i in visited:
      print("infinite loop")
      return
    else:
      visited[i] = op

    if op == "acc":
      if arg[0] == "+":
        acc += int(arg[1:]) 
      else:
        acc -= int(arg[1:])
    if op == "jmp" or (op == "nop" and i == swap):
      if i == swap and op != "nop":
        i += 1
        continue
      if arg[0] == "+":
        i += int(arg[1:]) - 1
      else:
        i -= (int(arg[1:]) + 1)
    
    i += 1
  return acc

with open("input.txt", 'r') as f:
  lines = f.readlines()
  visited = {}
  execute(lines, visited, -1)

  for i in visited:
    if visited[i] == "jmp" or visited[i] == "nop":
      acc = execute(lines, {}, i)
      if acc:
        print(acc)
        break