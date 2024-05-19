def filter_space(keyword):
    for char in keyword:
        if char == ' ':
            keyword = keyword.split(' ')
            break

    result = ''

    for i in range(len(keyword)):
        if i == len(keyword) - 1:
            result+=keyword[i]
        else:
            result+=keyword[i]
            result+='%20'

    return result