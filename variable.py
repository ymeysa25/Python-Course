#Type of Variable

number = 10 #int
f_number = 4.9 #float
nama = "Yogie Meysa Tama" #string
is_existed = True #value is True/False -->boolean

print(number)

#challenge
"""Imagine we checek in a patient name john smith,
   He's 20 years old and is a new patient.
   Define 3 variabel for his name, his age, 
   and another variable for if this is a new patient or an existing patient
"""

name = "John Smith"
age = 20
is_new = True

### INPUT function in python ###
#1. Ask two question : person's name and favourite color
# then print a message like "Mosh like blue"
person_name = input('What is ur name? ')
fav_color = input('what is your fav colors? ')

print(person_name +  " likes " + fav_color)

#2. mencari umur seseorang dengan inputan
tahun_lahir = input('Tahun Lahir: ')
umur = 2019 - int(tahun_lahir) #setiap inputan pada python dalam bentuk string, jadi harus diubah ke int
print(umur)
