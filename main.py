from art import logo, vs
from game_data import data
from replit import clear
from random import choice

def getFeedback(correct, score):
  """Generates a feedback string based on whether or not the user is correct and the updated score"""
  
  if correct:
    return f"You're right! Current score: {score}"
  else:
    return f"Sorry, that's wrong. Final score: {score}"

score = 0
gameOver = False

choice_b = choice(data)
print(logo)

while not gameOver:

  #Choose two choices from game data
  choice_a = choice_b
  while choice_a == choice_b:
    choice_b = choice(data)
  
  #Determine correct answer
  if choice_a["follower_count"] > choice_b["follower_count"]:
    correct_ans = 'a'
  else:
    correct_ans = 'b'

  #Get player's answer
  print(f"Compare A: {choice_a['name']}, a(n) {choice_a['description']} from {choice_a['country']}.")
  print(vs)
  print(f"Against B: {choice_b['name']}, a(n) {choice_b['description']} from {choice_b['country']}.")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Determine whether or not player is right and generate response.
  # Update score and prepare for new challenge if player is correct
  if answer == correct_ans:
    correct = True
    score += 1
  else:
    correct = False
    gameOver = True

  report = getFeedback(correct, score)

  # Clear screen and give feedback
  clear()
  print(logo)
  print(report)
