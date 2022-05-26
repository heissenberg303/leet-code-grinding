def solution(inputString):

    # inputString = "(bar)" -> "rab"
    # inputString = "foo(bar)baz" -> "foorabbaz"
    # inputString = "foo(bar)baz(blim)" -> "foorabbazmilb"
    # inputString = "foo(bar(baz))blim"-> "foobazrabblim"

    st = []
    lenn = len(inputString)

    for i in range(lenn):

        # Push the index of the current
        # opening bracket
        if (inputString[i] == '('):
            st.append(i)

        # Reverse the substarting
        # after the last encountered opening
        # bracket till the current character
        elif (inputString[i] == ')'):
            temp = inputString[st[-1]:i + 1]
            inputString = inputString[:st[-1]] + temp[::-1] + \
                   inputString[i + 1:]
            del st[-1]

    # To store the modified string
    res = ""
    for i in range(lenn):
        if (inputString[i] != ')' and inputString[i] != '('):
            res += (inputString[i])
    return inputString


inputString = "foo(bar)baz"

print(solution(inputString))
