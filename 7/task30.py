#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел


# #todo: Для каждого значения из списка mass получите
# # список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]


max_of_two = lambda a, b: a if a > b else b

# Проверка
print(max_of_two(5, 10))
print(max_of_two(-3, -7))
print(max_of_two(2.5, 2.5))



#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter( lambda val:  val%2 != 0,  list_ )))


list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter( lambda val:  val%2 != 0,  list_ )))

вывод
[11, 25, 33, 101]


#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']

mp3_files = sorted([f for f in files if f.endswith('.mp3')])
print(mp3_files)

вывод
['file2.mp3', 'file3.mp3']


