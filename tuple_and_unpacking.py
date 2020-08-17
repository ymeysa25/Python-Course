#Tuple
#sama dengan list cuman, di tuple ga bisa mengubah data didalamnya

tuple_number = (1,2,4)
tuple_number[0] #1
tuple_number.count(1)
tuple_number.index(4)

#Unpacking --> salah satu fitur pada python
#pada bahasa pemrograman lain
#assume we have

coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x, y, z) #1 2 3

#pada python, fitur ini juga bisa digunakan pada list
a , b , c = coordinates
print(a, b, c) #1 2 3