import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

list1=[rock,paper,scissors]

print(f"Rock: {rock}\n Paper: {paper}\n Scissors: {scissors}") 

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user >2 or user <0:
    print("You have entered an Invalid Number. Please Enter again.")
    user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

print(f"You Chose \n{list1[user]}\n")
computer=random.randint(0,2)
print(f"Computer Chose \n{list1[computer]}")

if (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1):
    print("YOU WIN!!!")
elif (user==computer):
    print("It's a DRAW!!")
else:
    print("YOU LOSE")

