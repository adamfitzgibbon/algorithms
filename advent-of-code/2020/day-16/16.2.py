def get_valid_places(validPlaces):
  final_places = [None for x in validPlaces]
  for i, places in enumerate(validPlaces):
    if len(places) == 1:
      final_places[i] = places[0]
  while None in final_places:
    for i, places in enumerate(validPlaces):
      if len(places) > 1:
        found = ""
        conflict = False
        for place in places:
          if place not in final_places:
            if found:
              conflict = True
              break
            found = place
          if not conflict and found != "":
            final_places[i] = found
  return final_places

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  rules = {}
  isYourTicket = isNearbyTicket = False
  validValues = set()
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
      rules[label] = rangePairs
    
    if isYourTicket:
      yourTicket = line.split(",")
    if isNearbyTicket:
      nearbyTickets.append(line.split(","))
  
  for ranges in rules.values():
    for r in ranges:  
      for i in range(r[0], r[1]+1):
        validValues.add(i)

  validTickets = []
  for ticket in nearbyTickets:
    invalid = False
    for num in ticket:
      num = int(num)
      if num not in validValues:
        invalid = True
        break
    if not invalid:
      validTickets.append(ticket)
  
  validPlaces = [list(rules.keys()) for x in range(len(yourTicket))]
  for ticket in validTickets:
    for i, num in enumerate(ticket):
      for place in validPlaces[i].copy():
        invalid = True
        for r in rules[place]:
          if r[0] <= int(num) <= r[1]:
            invalid = False
            break
        if invalid:
          validPlaces[i].remove(place)
  
  final_places = get_valid_places(validPlaces)
  departures = 1
  for i, place in enumerate(final_places):
    if "departure" in place:
      departures *= int(yourTicket[i])
  
  print(departures)