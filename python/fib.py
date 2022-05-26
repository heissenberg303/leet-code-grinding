

import timeit
import math

mysetup = "from math import sqrt"

# code snippet whose execution time is to be measured
mycode = ''
def fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return sum(fibs)

print(fibonacci(998))

# timeit statement
# def Fibonacci(n):

#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")

#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0

#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1

#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# print(Fibonacci(9))
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))