class Point:
    def __init__(self, x, y): #Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("Draw")


point1 = Point(10,20) #make a new Object
point1.draw()
point1.move()

print(point1.x) #jika ini  dieksekusi tanpat constructor maka AttributeError

#exercise
#make a class woth atribute name and method talk
"""Setelah class, harus ada jarak 2 spasi"""


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, My Name is {self.name}")


person1 = Person("Yogie Meysa Tama")
person1.talk()

bob = Person("Bob Power")
bob.talk()