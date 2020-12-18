def solve(problem):
  total = 0
  currentOp = None
  i = 0
  while i < len(problem):
    c = problem[i]
    if c == "(":
      j = i + 1
      pCount = 1
      while pCount > 0:
        if problem[j] == "(":
          pCount += 1
        if problem[j] == ")":
          pCount -= 1
        j += 1
      total = perform_op(currentOp, total, solve(problem[i+1:j-1]))
      if j+1 >= len(problem):
        return total
      i = j-1
      currentOp = None
    elif c in ("+", "*"):
      currentOp = c
    elif c == ")":
      continue
    else:
      if currentOp:
        total = perform_op(currentOp, total, int(c))
        currentOp = None
      else:
        total = int(c)
    i += 1
  return total

def perform_op(op, val1, val2):
  if not op:
    return val2
  if op == "+":
    return val1 + val2
  if op == "*":
    return val1 * val2      
      
with open("input.txt", 'r') as f:
  problems = [x.rstrip().replace(" ", "") for x in f.readlines()]
  total = 0
  for problem in problems:
    total += solve(problem)
  print(total)