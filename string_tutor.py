#file ini akan berisi beberapa basic tentang string pada python

#Beberapa cara menyatakan string
course = 'Python Project'
course1 = "Python Project2"
course2 = 'Python project by "Yogi" '
course3 = "My First's Python Project "

print(course)
print(course1)
print(course2)
print(course3)

#index pada string
#index pada string dimulai dari 0

#P y t h o n   P r o j  e  c  t
#0 1 2 3 4 5 6 7 8 9 10 11 12 13
print(course[0]) # P
print(course[-1]) #t --> menampilkan index terakhir

print(course[0:5]) #Pytho --> index 0 -> 4
print(course[0:]) #Python Project --> dari 0 sampai selesai
print(course[0:-2]) #Python Proje --> dari 0 sampai len(course) - 2
print(course[:-2])  # Python Proje

#Formatted string
f_name = 'Yogie'
l_name = 'Meysa'

#We want to print Yogie [Meysa] is a Programmer
#cara concatenation (Merangkai) sama seperti javascript
message = f_name + ' [' + l_name + ']' + ' is a programmer'

#cara yang lebih efisien --> formatted string
msg = f'{f_name} [{l_name}] is a programmer'

print(message)
print(msg)

#String method

print(len(course)) #14  -> banyaknya karakter
print(course.upper()) #PYTHON PROJECT
print(course.lower()) #python project
print(course.find('Project'))  #7 -->index of  first's Character

print(course.replace('Project', 'Hard Project')) #Python Hard Project

print('Pyhton' in course) #True or False
