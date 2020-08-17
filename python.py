
import math as mt
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            print(meals[i])
    return False


makanan = ['bakso', 'spageti', 'jeruk', 'jeruk']

menu_is_boring(makanan)

zip_str = 'ssssssss'
def is_valid_zip(zip_str):
    print (len(zip_str) == 5 and zip_str.isdigit())

print(mt.pi)

print("Hello World")
print("FUck off")

