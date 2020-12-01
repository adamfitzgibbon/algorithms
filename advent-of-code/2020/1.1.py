with open("1.1_input.txt", 'r') as f:
  vals = set()
  for line in f:
    if int(line) in vals:
        print (int(line) * (2020-int(line)))
        break
    vals.add(2020-int(line))