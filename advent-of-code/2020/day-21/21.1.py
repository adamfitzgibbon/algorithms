allMap = {}
runningIngredients = []

with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  for line in lines:
    ingredients, allergens = line.split(" (contains ")
    ingrList = ingredients.split(" ")
    allList = allergens[:-1].split(", ")
    runningIngredients += ingrList
    for a in allList:
      if a in allMap:
        allMap[a] &= set(ingrList)
      else:
        allMap[a] = set(ingrList)
  safeIngredients = set(runningIngredients) - { val for vals in allMap.values() for val in vals }
  print(sum([x in safeIngredients for x in runningIngredients]))