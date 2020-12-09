def is_sum(preamble, val):
  for i, num in enumerate(preamble):
    for j, num2 in enumerate(preamble):
      if i != j:
        if num + num2 == val:
          return True
  return False

with open("9_input.txt", 'r') as f:
  lines = [int(x) for x in f.readlines()]
  preamble = lines[:25]
  rest = lines[25:]
  for num in rest:
    if not is_sum(preamble, num):
      for i, startNum in enumerate(lines):
        target = num - startNum
        j = i
        while target > 0 and len(lines) > j+1:
          j += 1
          target -= lines[j]
        if target == 0:
          contiguousSet = lines[i:j+1]
          print(min(contiguousSet) + max(contiguousSet))
          break

    preamble.pop(0)
    preamble.append(num)
  