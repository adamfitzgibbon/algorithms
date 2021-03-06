def is_sum(preamble, val):
  for i, num in enumerate(preamble):
    for j, num2 in enumerate(preamble):
      if i != j:
        if num + num2 == val:
          return True
  return False

with open("input.txt", 'r') as f:
  lines = [int(x) for x in f.readlines()]
  preamble = lines[:25]
  rest = lines[25:]
  for num in rest:
    if not is_sum(preamble, num):
      print(num)
      break
    preamble.pop(0)
    preamble.append(num)
  