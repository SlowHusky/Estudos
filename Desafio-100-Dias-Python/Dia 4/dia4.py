import random

paper_draw = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor_draw = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_draw = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
def competition():
    var = input()
    computer = random.randint(0,2)
    if var not in [0,1,2]:
        print("choose 0, 1, 2")
        exit
    if var == computer:
        print("draw")
    elif (var == 0 and computer==1) or (var == 1 and computer == 2) or (var==2 and computer == 0):
        print("lose")
    else:
        print("win")