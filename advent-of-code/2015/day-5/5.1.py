def check_nice(line):
  vowels = "aeiou"
  vowelCounter = 0
  hasDouble = False
  blacklist = ["ab", "cd", "pq", "xy"]
  for b in blacklist:
    if b in line:
      return False
  for i, c in enumerate(line):
    if i < len(line) - 1 and c == line[i+1]:
      hasDouble = True
    if c in vowels:
      vowelCounter += 1
  return vowelCounter >= 3 and hasDouble


with open("input.txt", 'r') as f:
  counter = 0
  for line in f:
    line = line.rstrip()
    if check_nice(line):
      counter += 1
  print(counter)