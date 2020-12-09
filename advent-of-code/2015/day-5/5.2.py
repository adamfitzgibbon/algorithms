def check_nice(line):
  doublePair = False
  skipPair = False
  for i, c in enumerate(line):
    if i + 2 < len(line):
      if c + line[i+1] in line[i+2:]:
        doublePair = True
      if c == line[i+2]:
        skipPair = True
  return doublePair and skipPair


with open("input.txt", 'r') as f:
  counter = 0
  for line in f:
    line = line.rstrip()
    if check_nice(line):
      counter += 1
  print(counter)