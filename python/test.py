inputString = "aaabaaaa"




length = len(inputString)-1

for letter in range(len(inputString)):
    print(inputString[letter])
    print (inputString[length])
    print("==")
    length -= 1


