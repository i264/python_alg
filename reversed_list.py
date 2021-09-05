def list_reverser(ltbr):

    if ltbr == []:
        return ltbr

    reversed = []

    i = len(ltbr) - 1

    while i >= 0 :
        
        if type(ltbr[i]) == list:
            ltbr[i] = list_reverser(ltbr[i])

        reversed.append(ltbr[i])
        i -= 1

    return reversed

test_list=[[1, 2], [3, 4], [5, 6, 7]]
print(list_reverser(test_list))
