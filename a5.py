#Задание А
#Реализуйте функцию с возможностью отрпавить любое количество строк в качестве аргументов
#которая будет их конкатинировать, убирать лишние пробелы, корректировать регистр по умолчанию.
#Или в качестве альтернативы к каждой строке применять callback функцию со своим вариантом обработки строки.
#func("this is", "a    funCtion\'s argUMents", "     simple Example" callback = lambda x: x )
#"This is a funCtion's arguments simple example".


def toStr(*args,word=[]):
  a = list(args)
  for i in args:
    word.append(i.strip(',!@#$%^&*()" '))
  word = ' '.join(word).lower().capitalize()
  word = ' '.join(word.split()) #удалить лишние пробелы между словами a    funCt
  return(word)

#print(toStr(" this is", "a    funCtion\'s argUMents", "     simple Example"))


