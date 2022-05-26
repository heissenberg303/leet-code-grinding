def solution(inputString):

    # inputString = "aabb" -> "abba" -> True
    # inputStrin = "abbcabb" ->
    # Create a listt
    listt = []

    # For each character in input strings,
    # remove character if listt contains
    # else add character to listt
    for i in range(len(inputString)):
        if (inputString[i] in listt):
            listt.remove(inputString[i])
        else:
            listt.append(inputString[i])

    # if character length is even
    # list is expected to be empty
    # or if character length is odd
    # listt size is expected to be 1
    if (len(inputString) % 2 == 0 and len(listt) == 0 or
            (len(inputString) % 2 == 1 and len(listt) == 1)):
        return True
    else:
        return False