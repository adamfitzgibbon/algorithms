with open("1_input.txt", 'r') as f:
  counter = 0
  for line in f:
    for c in line:
      if c == "(":
        counter += 1
      if c == ")":
        counter -= 1
  print(counter)