#Function
def greet_user():
    print("hi there")
    print("Welcome")

print("Start")
greet_user()
print("Finish")

#Function with Parameter
def greet_user2(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("I am Here")

print("------------")
greet_user2("Yogi", "Meysa") #namanya positional argument
greet_user2(last_name="Meysa", first_name="Yogie") #keyword Argumenr

#return statement

def square(number):
    return number * number

type(square(3))

def emoji_converter(message):
    # Emoji Converter
    words = message.split(' ')
    emojis = {
        ":)": "😁",
        ":(": "😢",
        ":p": "😜",
        "love": '❤'
    }
    # print(words) #['Hello', 'i', 'am', 'yogi']
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converter(message))
