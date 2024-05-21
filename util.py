def filter_space(keyword):
    space = 0
    for char in keyword:
        if char == ' ':
            keyword = keyword.split(' ')
            space+=1
            break

    if space > 0:
        result = ''
        for i in range(len(keyword)):
            if i == len(keyword) - 1:
                result+=keyword[i]
            else:
                result+=keyword[i]
                result+='%20'
        
        return result
    else:
        return keyword
