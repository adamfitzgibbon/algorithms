with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  rules = {}
  isYourTicket = isNearbyTicket = False
  validValues = set()
  invalidValues = []
  nearbyTickets = []
  for line in lines:
    if not line:
      continue
    if line == "your ticket:":
      isYourTicket = True
      continue
    if line == "nearby tickets:":
      isYourTicket = False
      isNearbyTicket = True
      continue

    if not isYourTicket and not isNearbyTicket:
      label, values = line.split(": ")
      ranges = values.split(" or ")
      rangePairs = []
      for r in ranges:
        start, end = r.split("-")
        rangePairs.append((int(start),int(end)))
      # rangePairs = [(min,max) for r in ranges for (min, max) in r.split("-")]
      rules[label] = rangePairs
    
    if isYourTicket:
      yourTicket = line.split(",")
    if isNearbyTicket:
      nearbyTickets.append(line.split(","))
  
  for ranges in rules.values():
    for r in ranges:  
      for i in range(r[0], r[1]+1):
        validValues.add(i)

  for ticket in nearbyTickets:
    for num in ticket:
      num = int(num)
      if num not in validValues:
        invalidValues.append(num)
  
  print(sum(invalidValues))
        