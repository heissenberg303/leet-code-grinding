def solution(inputArray):

    #listProduct = [inputArray[i] * inputArray[i+1] for i in range(len(inputArray) - 1)]
    listProduct = []

    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        listProduct.append(product)

    return max(listProduct)
