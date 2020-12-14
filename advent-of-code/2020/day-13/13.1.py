with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  minutes = int(lines[0])
  buses = [int(x) for x in lines[1].split(",") if x != "x"]
  minDiff = -1
  minId = -1
  for bus in buses:
    diff = bus - minutes % bus
    if minDiff == -1 or diff < minDiff:
      minId = bus
      minDiff = diff

  print(minDiff * minId)