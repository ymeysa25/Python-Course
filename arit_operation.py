#aritmatic Operation

a = 10
b = 3

print(a + b) #13 --> Pertambahan
print(a - b) #7  ---> Pengurangan
print(a / b) #3.3333333335 ---> Pembagian dengan hasil floar
print(a // b) #3 ---> Pembagian dengan hasil integer
print(a * b)  #30 ---> Perkalian
print(a ** b) #1000  ---> a pangkat b
print(a % b)  #1 --> modulus 10 mod 3 --> 1

#Augmented Assigment
a += b # a = a + b
a -= b # a = a - b
a /= b # a = a / b
a //= b # a = a // b
a *= b # a = a * b

#Common math function
x = 2.7
round(x) #pembulatan x
abs(-2.1) #nilai mutlak

#import library math
import math as mt
print(mt.ceil(2.7)) #3  --> pembulatan ke atas
print(mt.floor(2.7)) #2 --> pembulatan ke bawah
print(mt.pi) #3.141592653589793