with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  nums = lines[0].split(",")
  count = len(nums)
  mem = {int(num): [i+1] for i, num in enumerate(nums)}
  print(mem)
  new = True
  last = nums[-1]
  while count < 30000000:
    count += 1
    if new:
      num = 0
      new = not num in mem
      if num in mem:
        mem[num].append(count)
      else:
        mem[num] = [count]
      last = num
    else:
      prev, recent = mem[last][-2:]
      num = recent - prev
      new = not num in mem
      if num in mem:
        mem[num].append(count)
      else:
        mem[num] = [count]
      last = num
  print(num)
