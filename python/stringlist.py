text = "Hey fellow warriors"


#longword = [letter for letter in word if len(letter)>=5]

def spin_words(sentence):
    words = sentence.split(" ")
    newWords = []
    for word in words:
        if len(word) >= 5:
            newWords.append(word[::-1]) # "".join(reversed(word))
        else:
            newWords.append(word)

    return " ".join(newWords)


print(spin_words(text))
