# !5 = 5*4*3*2*1
import timeit
import math

mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''
def fact(n):

    # if n == 1:
    #     return 1
    # return n*fact(n-1)

    #return math.factorial(n)

    # res = 1
    # for i in range(2, n+1):
    #     res *= i
    # return res

    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return sum(fibs)

print(fact(998))

# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))