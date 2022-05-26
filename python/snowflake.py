# first aproach break down to smaller problem

def identify_identical(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] == arr[j]:
                print("Twin integers found")
                return
    print("Not found")

def main():
    a = [1, 2, 3, 1, 5]
    identify_identical(a)


if __name__ == "__main__":
    main()