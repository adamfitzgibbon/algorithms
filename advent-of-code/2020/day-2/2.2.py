with open("input.txt", 'r') as f:
  validCount = 0
  for line in f:
    limits, letter, pwd = line.split(" ")
    letter = letter[0]
    pwd.rstrip()
    limits = limits.split("-")
    found = False
    valid = False
    for i, c in enumerate(pwd):
      if c == letter and str(i+1) in limits:
        if found:
          valid = False
          break
        valid = True
        found = True
    if valid:
      validCount += 1
  
  print(validCount)