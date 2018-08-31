def matFilter(text2):
    dictionary = {'убегать':'канать','ахуенные':'прекрасные','ограбление':'гоп-стоп','подлец':'редиска'}
    text2=text2.lower().split(' ') #к нижнему регистру и разбить в список
    result2=[]
    for word in text2:
        if word in dictionary:
            result2.append(dictionary[word])
        else:
            result2.append(word)
    result2 = ' '.join(result2)
    return(result2)

