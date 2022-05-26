def solution(statues):
    sortedStatues = sorted(statues)

    count = 0
    for i in range(len(sortedStatues) - 1):
        diff = sortedStatues[i + 1] - sortedStatues[i]
        if diff > 1:
            count = count + diff - 1

    return count