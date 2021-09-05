def list_flatter(ltbf):
    if ltbf == []:
        return ltbf

    flatten = []
    for i in ltbf:

        if type(i) == list:
            flatten.extend(list_flatter(i))
        else:
            flatten.append(i)

    return flatten

# if ltbf == [] :
#    return ltbf
# if type(ltbf[0]) == list :   # isinstance(ltbf[0], list)
#    return list_flatter(ltbf[0]) + list_flatter(ltbf[1:])
# return ltbf[:1] + list_flatter(ltbf[1:])

test_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(list_flatter(test_list))
