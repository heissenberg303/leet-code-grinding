
Check first bad index
def bad_pair(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i+1] <= sequence[i]:
            return i
    return -1


def solution(sequence):
    check = bad_pair(sequence)
    if check == -1:
        return True
    # delete earlier element make increasing
    if bad_pair(sequence[check-1:check]+sequence[check+1:]) == -1:
        return True
    # delete later element make increasing
    if bad_pair(sequence[check:check+1]+sequence[check+2:]) == -1:
        return True
    return False



sequence = [1, 2, 3, 4, 3, 6]
# check = 3

j = 3
print(sequence)
leftSequence = sequence[:] ##copy list
rightSequence = sequence[:] ##copy list
copySequence1 = sequence[:]
copySequence2 = sequence[:]
def deleteLeftElement(seq, index):
    del seq[index]
    return seq

def deleteRightElement(seq, index):
    del seq[index+1]
    return seq

print(f"copy: {copySequence2} " )
deleteEarlyElement = [seq for seq in sequence if seq != sequence[j]]
deleteLaterElement = [seq for seq in sequence if seq != sequence[5]]

print(deleteLeftElement(leftSequence, j))
print(deleteRightElement(rightSequence, j))
print(deleteEarlyElement)
print(f"copy: {copySequence2} " )
print(deleteLaterElement)
# # delete earlier element make increasing
# print(sequence[check-1:check]+sequence[check+1:]) #[3, 3, 6]
# # delete later element make increasing
# print(sequence[check:check+1]+sequence[check+2:]) # [4, 6]

