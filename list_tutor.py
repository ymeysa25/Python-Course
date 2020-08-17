names  = ['Pyhton', 'Java', 'PHP', "C++", 'C+', 'Ruby', 'Golang']

print(names[0]) #Python
print(names[-1]) #Golang
print(names[0:3]) #['Pyhton', 'Java', 'PHP']
print(names[:]) #['Pyhton', 'Java', 'PHP', "C++", 'C+', 'Ruby', 'Golang']
print(names)  #['Pyhton', 'Java', 'PHP', "C++", 'C+', 'Ruby', 'Golang']

names[0] = 'Python3' #change value of index 0 names

#progrm to find the largest number in a list
numbers = [1, 4, 5, 6, 8, 2]
maxnumber = numbers[0]
for number in numbers:
    if number > maxnumber:
        maxnumber = number

print(maxnumber)

#second way
print('Maximum is:', max(numbers))

#2D list
matrix = [ #Matrix 3x3
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][0]) #1
print(matrix[0][2]) #3
print(matrix[2][0]) #7

#menampilkan semua item pada matrix secara terpisah

for row in matrix:
    for item in row:
        print(item)


# List Method
numbers = [5,2,1,7,4]
numbers2 = numbers.copy()  #mengopy
print(f"List Sebelum Di Modif : {numbers}")
numbers.append(20) #menambahkan 20 pada index terakhir list
print(f"List Setelah di append: {numbers}")
numbers.insert(0,9) #insert(x,y) x --> indexnya, y --> nilai yang ingin ditambahkan
print(f"List Setelah di insert(0,9) : {numbers}")
numbers.remove(2) #menghapus nilai 2
print(f"List Setelah di remove(2) : {numbers}")
numbers.pop() #menghapus item pada list terakhir
print(f"List Setelah di pop() : {numbers}")
print(f"Menampilkan index(5) : {numbers.index(5)}") #menampilkan index dari item yang dicari
print(f"List Setelah di count(2) : {numbers.count(2)}") #menampilkan banyaknya item n
numbers.sort() #fungsi untuk mengurutkan list, return None
print(f"List Setelah di sort() : {numbers}")
numbers.reverse()  #membalikan urutan
print(f"List Setelah di reverse() : {numbers}")
numbers.clear() #menghapus semua item pada list
print(f"List Setelah di clear() : {numbers}")


# write a program to remove the duplicate in a list
list_number = [1,3,4,1,3,4]
print("---------")
for item in list_number:
    duplicate = list_number.count(item)
    if duplicate > 1:
        print(item)
        list_number.remove(item)
        print(list_number)


