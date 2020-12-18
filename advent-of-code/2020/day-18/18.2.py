def find_matching_parenthesis(j, problem):
  pCount = 1
  while pCount > 0:
    j -= 1
    if problem[j] == ")":
      pCount += 1
    if problem[j] == "(":
      pCount -= 1
  return j

def solve(problem, total = 0):
  if not problem:
    return total
  c = problem[-1]
  if c == ")":
    j = len(problem) - 1
    j = find_matching_parenthesis(j, problem)
    subTotal = solve(problem[j+1:-1])
    return solve(problem[:j], subTotal)
  elif c == "+":
    if problem[-2] != ")":
      total = perform_op(c, total, int(problem[-2]))
      return solve(problem[:-2], total)
    
    j = len(problem) - 2
    j = find_matching_parenthesis(j, problem)
    subTotal = perform_op(c, total, solve(problem[j+1:-2]))
    return solve(problem[:j], subTotal)
  elif c == "*":
    return perform_op(c, total, solve(problem[:-1]))
  else:
    return solve(problem[:-1], int(c))

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