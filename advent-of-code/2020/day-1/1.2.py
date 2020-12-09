def do_work(lines):
  for i, firstVal in enumerate(lines):
    vals = set()
    targetVal = 2020 - int(firstVal)
    for j, secondVal in enumerate(lines):
      if i == j:
        continue
      val = int(secondVal)
      if val in vals:
        print (int(firstVal) * val * (targetVal-val))
        return
      vals.add(targetVal - val)


with open("input.txt", 'r') as f:
  do_work(f.readlines())