def get_id(s, lowerR, upperR, lowerC, upperC):
  if len(s) == 0:
    return (upperR, upperC)
  if s[0] == "F":
    return get_id(s[1:], lowerR, upperR - (upperR - lowerR) // 2 - 1, lowerC, upperC)
  if s[0] == "B":
    return get_id(s[1:], lowerR + (upperR - lowerR) // 2 + 1, upperR, lowerC, upperC)
  if s[0] == "R":
    return get_id(s[1:], lowerR, upperR, lowerC + (upperC - lowerC) // 2 + 1, upperC)
  if s[0] == "L":
    return get_id(s[1:], lowerR, upperR, lowerC, upperC - (upperC - lowerC) // 2 - 1)

with open("input.txt", 'r') as f:
  ids = []
  for line in f:
    row, column = get_id(line.rstrip(), 0, 127, 0, 7)
    id = row * 8 + column
    ids.append(id)
  sorted_ids = ids.sort()

  for i,id in enumerate(ids):
    if id == ids[i+1] - 2:
      print (id + 1)
      break
