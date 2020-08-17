#dictionary ini mirip seperti JSON

customer = {
    "name":"John Smith",
    "age" : 30,
    "is_verified" : True
}

print(customer["name"]) #dictionary[key]
print(customer.get("name")) #sama dengan diatas, tapi jika key tidak ditemukan, tidak akan menampilkan error

customer["name"] = "Yogie Meysa Tama"
print(customer.get("name"))

customer["birthday"] = "25 Mei 1998"
print(customer.get("birthday"))

print(customer)

#challenge change input number into a word like 1 --> one
phone = input(f"Phone: ")
digit_mapping = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five"
}

for ch in phone:
    ch_int = int(ch)
    print(digit_mapping.get(ch_int) , end= " ")
print("!")

#Emoji Converter
message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "😁",
    ":(" : "😢",
    ":p" : "😜",
    "love" : '❤'
}
# print(words) #['Hello', 'i', 'am', 'yogi']
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
