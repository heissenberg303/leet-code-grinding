def find_shortest_index(line):
    shortest = 0
    for n in range(1, len(line)):
        if line[n] < line[shortest]:
            shortest = n
    return shortest

def solve(newPeople, line):
    for people in range(newPeople):
        shortest = find_shortest_index(line)
        print(line[shortest])
        line[shortest] += 1

def main():
    n = int(input("number of line: "))
    m = int(input("number of new people: "))
    print(f"line : {n}\nnew people : {m}")
    # {number of line : number of people in line}
    p = []
    for i in range(n):
        numberPeople = int(input("number of people in line: "))
        p.append(numberPeople)

    solve(m, p)
    # print(find_shortest_index(p))


if __name__ == "__main__":
    main()