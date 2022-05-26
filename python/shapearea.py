def recursive(n):

    if n == 1:
        return 1

    else :
        n = n - 1
        return (4 * n) + recursive(n)


print(recursive(3))
