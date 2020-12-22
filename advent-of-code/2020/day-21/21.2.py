allMap = {}

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  for line in lines:
    ingredients, allergens = line.split(" (contains ")
    ingrList = ingredients.split(" ")
    allList = allergens[:-1].split(", ")
    for a in allList:
      if a in allMap:
        allMap[a] &= set(ingrList)
      else:
        allMap[a] = set(ingrList)

  pairedIngredients = {}
  allergenNum = len(allMap.keys())
  while len(pairedIngredients) < allergenNum:
    for allergen, ingredients in allMap.items():
      possibleMatch = None
      for ingredient in ingredients:
        if ingredient not in pairedIngredients:
          if possibleMatch:
            possibleMatch = None
            break
          possibleMatch = ingredient
      if possibleMatch:
        pairedIngredients[possibleMatch] = allergen
  print(allMap)
  print(pairedIngredients)
  sortedPairs = sorted(pairedIngredients.items(), key=lambda x: x[1])
  print(",".join([x[0] for x in sortedPairs]))