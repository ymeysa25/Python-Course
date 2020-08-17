from pathlib import Path
#Absolute Path
path = Path("F:\Iseng")
for file in path.glob('*'): #bisa glob("*.*')
    print(file)

#Relative
path2 = Path() #root of the file means F:\Iseng\Python

for file in path2.glob('*'): #bisa glob("*.java')
    print(file)