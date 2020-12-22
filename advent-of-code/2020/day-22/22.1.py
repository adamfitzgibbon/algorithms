with open("input.txt", 'r') as f:
  lines = [x.rstrip() for x in f.readlines()]
  isPlayer2 = False
  deck1 = []
  deck2 = []
  for line in lines:
    if not line:
      isPlayer2 = True
      continue
    if line in ["Player 1:", "Player 2:"]:
      continue
    if isPlayer2:
      deck2.append(int(line))
    else:
      deck1.append(int(line))

  while len(deck1) != 0 and len(deck2) != 0:
    card1, card2 = deck1.pop(0), deck2.pop(0)
    if card1 > card2:
      deck1.append(card1)
      deck1.append(card2)
    else:
      deck2.append(card2)
      deck2.append(card1)
  
  winningDeck = deck1 if len(deck1) > 0 else deck2
  sum = 0
  for i, card in enumerate(winningDeck):
    sum += card * (len(winningDeck) - i)
  
  print(sum)