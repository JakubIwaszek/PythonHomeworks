def createPhoneticDict():
    dict = {
        "k": "Kilo",
        "u": "Uniform",
        "b": "Bravo",
        "a": "Alfa"
    }
    return dict

text = input("Entere text: ")
alphabet = createPhoneticDict()
print("Spelled text: ", end="")
for letter in text:
    word = alphabet[letter]
    print(word, end=" ")