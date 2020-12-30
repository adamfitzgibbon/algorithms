def find_loop_size_or_encryption_key(subjectNum, targetKey=None, loopSize=None):
  count = value = 1
  while True:
    value *= subjectNum 
    value %= 20201227
    if value == targetKey:
      return count
    if count == loopSize:
      return value
    count += 1

with open("input.txt", 'r') as f:
  lines = [int(x.rstrip()) for x in f.readlines()]
  cardKey, doorKey = lines
  loopSize = find_loop_size_or_encryption_key(7, cardKey)
  print(find_loop_size_or_encryption_key(doorKey, None, loopSize=loopSize))