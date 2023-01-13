# Caesar Cipher
def encrypt():

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v",
               "w", "x", "y", "z"]

    encryptionKey = {}

    spacing = int(input("What Is The Spacing Amount? "))
    spacing*=-1
    Input = input("Enter The Message: ")

    NewLetters = []

    for i in range(26):
        NewLetters.append("")

    for i_ in letters:
        newIndex = (spacing + letters.index(i_)) % 26
        NewLetters[newIndex] = i_

    for i in letters:
        encryptionKey[i] = NewLetters[letters.index(i)]
    encryptionKey[" "] = " "
    x = Input
    Input = list(Input)

    for i in range(len(Input)):
        Input[i] = encryptionKey[Input[i]]

    x = ""
    for i in Input:
        x = x + i
    print(x)

def decryption():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v",
               "w", "x", "y", "z"]

    encryptionKey = {}

    spacing = int(input("What Is The Spacing Amount? "))
    spacing*=-1
    Input = input("Enter The Message: ")

    NewLetters = []

    for i in range(26):
        NewLetters.append("")

    for i in letters:
        newIndex = (spacing + letters.index(i)) % 26
        NewLetters[newIndex] = i

    for i in NewLetters:
        encryptionKey[i] = letters[NewLetters.index(i)]
    encryptionKey[" "] = " "
    x = Input
    Input = list(Input)

    for i in range(len(Input)):
        Input[i] = encryptionKey[Input[i]]
    x = ""
    for i in Input:
        x = x + i
    print(x)

encrypt()
decryption()