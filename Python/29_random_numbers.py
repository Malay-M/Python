import random

x = random.randint(1,6)
print(x)

y = random.random()
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

cards = ["A",2,3,4,5,6,7,8,9,"J","Q","K"]
random.shuffle(cards)
print(cards)