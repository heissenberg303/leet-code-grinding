a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

def comp(array1, array2):
    # your code
    try:
        sorted([n**2 for n in array1]) == sorted(array2)
    except:
        return False

print(comp(a, b))