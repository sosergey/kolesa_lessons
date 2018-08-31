#Задание Б
#При помощи вашей новой функции из задания А и callback функции сделайте так чтобы ваша функция
#находила все url адреса в тексте и оборачивала их в <a href="{url}">{text}</a>
#func("на сайте http://host.com можно найти полезные материалы", callback)
#В результате получим
#"На сайте <a href="http://host.com">http://host.com</a> можно найти полезные материалы"


def toHref(list):
    result = []
    list = list.split()
    for i in list:
        if 'http:' in i:
            i =  '<a href="{0}">{0}</a>'.format(i)
            result.append(i)
        else:
            result.append(i)
    return(' '.join(result))

#text = "на сайте http://host.com можно найти полезные материалы"
#print(toHref(text))



