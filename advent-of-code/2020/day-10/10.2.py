def check_memo(lines, memo):
  memoKey = "".join(str(x) for x in lines)
  if memoKey in memo:
    return memo[memoKey]
  else:
    result = find_arrangements(lines, memo)
    memo[memoKey] = result
    return result

def find_arrangements(lines, memo):
  if len(lines) == 1:
    return 1
  if len(lines) == 0:
    return 1

  count1, count2, count3 = 0,0,0
  count1 = check_memo(lines[1:], memo)
  
  if len(lines) > 2 and lines[2] - lines[0] <= 3:
    count2 = check_memo(lines[2:], memo)
  if len(lines) > 3 and lines[3] - lines[0] <= 3:
    count3 = check_memo(lines[3:], memo)
  return count1 + count2 + count3

with open("input.txt", 'r') as f:
  lines = [int(x.rstrip()) for x in f.readlines()]
  lines.sort()
  device = max(lines) + 3
  lines = [0] + lines + [device]
  print(find_arrangements(lines, {}))