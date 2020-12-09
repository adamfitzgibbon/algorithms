with open("input.txt", 'r') as f:
  runningTotal = 0
  for line in f:
    dims =  [int(x) for x in line.rstrip().split("x")]
    sqdims = [dims[0]*dims[1], dims[0]*dims[2], dims[1]*dims[2]]
    runningTotal += sum(sqdims * 2) + min(sqdims)
  print(runningTotal)