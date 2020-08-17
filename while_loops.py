i = 1
while i <=5:
    print(i)
    i += 1
print("Done")

print("Another While Loop Example")

x = 1
while x <=5: #Segitiga siku2
    print("*" * x)
    x +=1

y = 1
z = 5
while y <= 5:
    while z >=1:
        print(" " * z,end = '')
        print("*" * y)
        y += 1
        z -= 1
    print()


#guess number
secret_number = 9

i = 0
while i < 3:
    guess_number = int(input(f"Guess a Number: "))
    if guess_number == secret_number:
        print("You Won")
        i +=3 #You can use break
    else:
        i += 1
print("Finish")

#car Game
is_quit = True;
is_started = False

while is_quit:
    instruksi = input("> ")
    if instruksi.lower() == "help":
        print(f"Start - To start a car\n"
              f"Stop - To stop a car\n"
              f"Quit - To quit a game\n")
    elif instruksi.lower() == "start":
        if is_started:
            print("Car is Already started")
        else:
            is_started = True
            print(f"Car is started -- Ready to go")

    elif instruksi.lower() == "stop":
        if not is_started:
            print("Car is Already Stopped")
        else:
            print(f"Car is stopped")
            is_started = False

    elif instruksi.lower() == "quit":
        is_started = False
        break # is_quit = False
    else:
        print("I dont understand that")
