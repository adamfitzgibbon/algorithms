mem = {}

def execute(mask, commands):
  for command in commands:
    memLocation, num = command
    for i, bit in enumerate(mask):
      if bit != "X":
        bitMask = 1 << len(mask) - i - 1
        num &= ~bitMask
        if int(bit):
          num |= bitMask
    mem[memLocation] = num
      

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  currentMask = ""
  storedCommands = []
  for line in lines:
    command, val = line.split(" = ")
    if command == "mask":
      if currentMask:
        execute(currentMask, storedCommands)
      currentMask = val
      storedCommands = []
    else:
      storedCommands.append((command[4:-1], int(val)))
  execute(currentMask, storedCommands)
  print(sum(mem.values()))
