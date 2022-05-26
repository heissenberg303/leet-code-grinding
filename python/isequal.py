def solution(a, b):
    listA = []
    listB = []
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            listA.append(a[i])
            listB.append(b[i])

    if count == 0:
        return True

    elif count == 2:                    # order does not matter for set
        return set(listA) == set(listB)  # set(listA) == set(listB) return true otherwise false
    else:
        return False


a = [4,7,3,5,8]
b = [7,4,3,5,8]

print(solution(a,b))

