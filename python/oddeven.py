test = [0, 1, 4]
test1 = [0, -1, -5]

def odd_or_even(arr):
    sumElement = sum(arr)
    if sumElement % 2 == 0:
        print("even")
    else:
        print("odd")


odd_or_even(0)