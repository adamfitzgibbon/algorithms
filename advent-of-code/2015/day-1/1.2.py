with open("input.txt", 'r') as f:
  counter = 0
  for line in f:
    for i,c in enumerate(line):
      if c == "(":
        counter += 1
      if c == ")":
        counter -= 1
      if counter == -1:
        print(i + 1)
        break