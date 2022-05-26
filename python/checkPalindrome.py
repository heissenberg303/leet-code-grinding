def solution(inputString):
    start = 0
    end = len(inputString)-1

    while start < end:
        if inputString[start] != inputString[end]: return False
        start += 1
        end -= 1

    return True