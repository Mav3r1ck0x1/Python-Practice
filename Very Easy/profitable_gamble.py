def profitable_gamble(prob, prize, pay):
  outcome = prob * prize - pay
  if outcome > 0:
    return True
  else:
    return False




profitable_gamble(0.2, 50, 9) #True
profitable_gamble(0.9, 1, 2) #False
profitable_gamble(0.9, 3, 2) #True
