# for item in "Python":
#     print(item)
#
# for item in ["Python", "Java", "C++", "Javascript"]:
#     print(item)
#
# for item in range(10):
#     print(item)
#
# for item in range(5, 10):
#     print(item)
#
# for item in range(5, 10, 2):  #range(x, y,z) --> x : nilai awal, y: nilai akhir - 1, z: jaraknya
#     print(item)
#

price = [10, 20, 30]

#mencari total price
#cara pertama
total = 0
for harga in price:
    total += harga

print(total)

#cara kedua
total = sum(price)
print(total)

#nested lop
#we want to print ccoordinate

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers =[5,2,5,2,2]

for item in numbers:
    print("X" * item)

#another way, assume we dont have python fiture above

for x_count in numbers:
    output = ''

    for count in range(x_count):
        output += 'x'
    print(output)