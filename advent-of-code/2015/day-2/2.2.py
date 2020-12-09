from functools import reduce
def find_perim(dims):
  maxIndex = 0
  for i, dim in enumerate(dims):
    if dim > dims[maxIndex]:
      maxIndex = i
  perim = 0
  for i, dim in enumerate(dims):
    if i != maxIndex:
      perim += dim * 2
  return perim

with open("input.txt", 'r') as f:
  runningTotal = 0
  for line in f:
    dims =  [int(x) for x in line.rstrip().split("x")]
    runningTotal += find_perim(dims) + reduce(lambda acc, item: acc * item, dims)
  print(runningTotal)