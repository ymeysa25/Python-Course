#https://docs.python.org/3/py-modindex.html

#random

import random

print(random.random()) #ga ada argumennya
print("------")

for item in range(3):
    print(random.randint(1,10))


#exercise to make a dice roll
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print(f"({dice1}, {dice2})")

#exercide yang diminta


class Dice:
    def roll(self):
        first =  random.randint(1, 6)
        second = random.randint(1, 6)
        return first,second #return sebagai tuple


dice = Dice()

print("-----------")
print(dice.roll())

#memilih pemimpin
person = ["Yogie", "Smith", "Brock", "Luffy"]
print(random.choice(person))