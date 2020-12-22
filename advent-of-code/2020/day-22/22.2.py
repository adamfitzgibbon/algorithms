def play(deck1, deck2):
  memory = {1: [], 2: []}
  while len(deck1) != 0 and len(deck2) != 0:
    for p1Deck, p2Deck in zip(memory[1], memory[2]):
      if p1Deck == deck1 and p2Deck == deck2:
        return True 
    memory[1].append(deck1.copy())
    memory[2].append(deck2.copy())
    card1, card2 = deck1.pop(0), deck2.pop(0)
    if card1 <= len(deck1) and card2 <= len(deck2):
      winner = play(deck1[:card1], deck2[:card2])
      if winner:
        deck1.append(card1)
        deck1.append(card2)
      else:
        deck2.append(card2)
        deck2.append(card1)
    else:
      if card1 > card2:
        deck1.append(card1)
        deck1.append(card2)
      else:
        deck2.append(card2)
        deck2.append(card1)
  return len(deck1) > 0

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
  
  play(deck1, deck2)
  print(deck1)
  print(deck2)
  winningDeck = deck1 if len(deck1) > 0 else deck2
  sum = 0
  for i, card in enumerate(winningDeck):
    sum += card * (len(winningDeck) - i)
  
  print(sum)