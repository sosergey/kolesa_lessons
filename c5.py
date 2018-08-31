#Задание С
#Примените к вашей новой функции и фильтр матов котрый вы писали до этого и url генератор из задания B в виде callback функции
#func("на сайте", "http://host.com",  можно найти ахуенные материалы", callback)
#в результате получим
#"На сайте <a href="http://host.com">http://host.com</a> можно найти прекрасные материалы."

import b5
import c2

var = ("на сайте", "http://host.com",  "можно найти ахуенные материалы")
x = lambda a: ' '.join(list(a))
text = x(var)

text = b5.toHref(text)
print(c2.matFilter(text))

