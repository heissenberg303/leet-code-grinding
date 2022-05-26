def find_max_length(arr):
    return len(max(arr, key=len))


def solution(inputArray):
    maxLength = find_max_length(inputArray)
    words = []
    for word in inputArray:
        if len(word) == maxLength:
            words.append(word)

    return words
