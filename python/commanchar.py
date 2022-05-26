from collections import Counter

s1 = "aabcc"
s2 = "adcaa"

# Convert string to dictionary
dictOfCharacter1 = Counter(s1) # s1 -> key values of character and values of repeated
dictOfCharacter2 = Counter(s2)

# Find intersection keys
repeatedCharacter = dictOfCharacter1 & dictOfCharacter2 # intersection dictionary

# Sum values
print(sum(repeatedCharacter.values()))