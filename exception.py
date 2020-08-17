try :
    age = int(input("Age: "))
    print(age)
except ZeroDivisionError:  #Only handle for ZeroDivisionError
    print("Age Cannot be Zero")
except ValueError: #Only handle for ValueError
    print("Invalid Value")
