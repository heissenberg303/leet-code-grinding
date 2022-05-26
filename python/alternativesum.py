
# create empty list of 2 index
def findsum(a):
    totweight = [0, 0]

    for i in range(0, len(a)):
        if i % 2:
            totweight[1] += a[i]

        else:
            totweight[0] += a[i]

    return totweight

a = [50, 60, 60, 45, 70]

print(findsum(a))
