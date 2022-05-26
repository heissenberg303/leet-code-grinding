picture = ["abc",
           "ded"]

# for i in range(len(picture)):
#         for j in range(len(picture[i])):
#             if i == 0 and j == 0:
#                 print("*" * len(picture[i]))
#             if j == 0 or j == len(picture[i]):
#                 print("*")

def addBoarder(picture):

    boarder = (len(picture[0])+2) * "*"
    res = []

    for i in range(len(picture)):
        if i == 0 or i == len(picture):
            res.append(boarder)
            res.append("*" + picture[i] + "*")
        else:
            res.append("*" + picture[i] + "*")
    res.append(boarder)

    return res

print(addBoarder(picture))