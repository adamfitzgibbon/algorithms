with open("2_input.txt", 'r') as f:
  validCount = 0
  for line in f:
    limits, letter, pwd = line.split(" ")
    letter = letter[0]
    pwd.rstrip()
    min,max = limits.split("-")
    letterCount = 0
    for c in pwd:
      if c == letter:
        letterCount += 1
    if int(min) <= letterCount and int(max) >= letterCount:
      validCount += 1
  
  print(validCount)