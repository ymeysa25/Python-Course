is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")
print("\n enjoy your day")

#simple kalkukaltor
x = int(input("Nilai 1: "))
y = int(input("Nilai 2: "))

print("""Operasi yang ingin digunakan
        1. Pertambahan
        2. Pengurangan
        3. Perkalian
        4. Pembagian
""")

masukan = input("Silahkan pilih dari operasi yang tersedia")

if masukan == "1" or masukan.lower() == "pertambahan":
    print(f"Hasil dari Pertambahan antara {x} dan {y} : {x+y}")
elif masukan == "2" or masukan.lower() == "pengurangan":
    print(f"Hasil dari Pengurangan antara {x} dan {y} : {x-y}")
elif masukan == "3" or masukan.lower() == "perkalian":
    print(f"Hasil dari Perkalian antara {x} dan {y} : {x*y}")
elif masukan == "4" or masukan.lower() == "pembagian":
    print(f"Hasil dari Pembagian antara {x} dan {y} : {x/y}")
else:
    print("Masukan instruksi dengan benar")