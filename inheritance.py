class Mammal:  #Parrent/ Superclass
    def walk(self):
        print("Walk")


class Dog(Mammal): #Subclass ,  sintax inheritance pada python
    def bark(self):
        print("Bark")


class Cat(Mammal): #pada java, class Cat extends Mammals
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat = Cat()
cat.be_annoying()
cat.walk()
