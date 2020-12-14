mem = {}

def apply_floating_bits(mask, i, locations):
  if i >= len(mask):
    return locations
  bit = mask[i]
  if bit == "1" or bit == "0":
    return apply_floating_bits(mask, i+1, locations)

  newLocations = locations.copy()
  for location in locations:
    bitOn = set_bit(i, location, "0", mask)
    bitOff = set_bit(i, location, "1", mask)
    
    if bitOn not in newLocations:
      newLocations.append(bitOn)
    if bitOff not in newLocations:
      newLocations.append(bitOff)

  return apply_floating_bits(mask, i+1, newLocations)
  
def set_bit(i, num, bit, mask):
  bitMask = 1 << len(mask) - i - 1
  num &= ~bitMask
  if int(bit):
    num |= bitMask
  return num

def execute(mask, commands):
  for command in commands:
    memLocation, num = command
    for i, bit in enumerate(mask):
      if bit == "1":
        memLocation = set_bit(i, memLocation, bit, mask)
    locations = apply_floating_bits(mask, 0, [memLocation]) 
    for location in locations:
      mem[location] = num
      

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
      storedCommands.append((int(command[4:-1]), int(val)))
  execute(currentMask, storedCommands)
  print(sum(mem.values()))
