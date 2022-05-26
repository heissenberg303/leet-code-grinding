def solution(a):

    # find tree index
    # a = [-1, 150, 190, 170, -1, -1, 160, 180] -> [-1, 150, 160, 170,-1, -1, 160, 180]
    sortPeople = sorted([a[i] for i in range(len(a)) if a[i] != -1]) # [150, 160, 170, 180, 190]
    j = 0

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = sortPeople[j]
            j += 1

    return a