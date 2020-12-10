with open("input.txt", 'r') as f:
  joltDifs = { 1: 0, 2: 0, 3:1 }
  current = 0
  lines = [int(x.rstrip()) for x in f.readlines()]
  lines.sort()
  ratedJolts = max(lines) + 3
  for line in lines:
    diff = line - current
    joltDifs[diff] += 1
    current = line
  print(joltDifs)
  print(joltDifs[1] * joltDifs[3])