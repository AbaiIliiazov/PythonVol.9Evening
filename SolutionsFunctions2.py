#Task1: 
# option1:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# def square(n):
# 	return n ** 2
# newlist = map(square, numbers)
# print(list(newlist))

# option2 (with lambda:)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# print(list(map(lambda x: x**2,numbers)))

#Task2: 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sum(numbers))

#Task3: 
# a = input("Enter data: ")
# a = list(a.split(","))

# if any(int(x)<0 for x in a):
#     print("False")
# else:
#     print("True")

#Task4: 

# a = input("Enter data: ")
# a = list(a.split(","))

# if any(int(x)<0 for x in a):
#     print("True")
# else:
#     print("False")

#Task5: 

# a = input("Enter data: ")
# a = list(a.split(","))

# a = [x for x in a if int(x) < 0]

# print(a)

#Task6: 
# a = input("Enter data: ")
# a = list(a.split(","))

# a = [x for x in a if int(x)%2==0]

# print(a)

#Task7: 
# a = ["hello", "world", "incapsulation", "inheritance"] 

# a = [s for s in a if len(s)>6]

# print(a)


#Option2 through filter: 
a = ["hello", "world", "incapsulation", "inheritance"]
def filterlist(longwords):
    if len(longwords)>6: 
        return longwords

result = filter(filterlist,a)   
print(list(result))



# Встроенные функции 
# 1) Дан массив с числами. Создайте новый массив, состоящий из квадратов этих чисел. Вход: 
# [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Выход: 
# [1, 4, 9, 16, 25, 36, 49, 64, 81] 
# Требование: 
# Использовать встроенные функции 
# Подсказка: (map, list) 

# 2) Дан массив с числами. Найдите сумму этих чисел. 
# Вход: 
# [1, 2, 3,] 
# Выход: 
# 6 
# Требование: 
# Использовать встроенные функции


# 3) Дан массив с числами. Проверьте то, что все элементы в массиве больше нуля. Вход: 
# [1, 2, 3, 0, -1] 
# Выход: 
# False 
# Вход: 
# [1, 2, 3] 
# Выход: 
# True 
# Требование: 
# Использовать встроенные функции 


# 4) Дан массив с числами. Проверьте то, что в нем есть отрицательные элементы. Вход: 
# [1, 2, 3, 0, -1] 
# Выход: 
# True 
# Вход: 
# [1, 2, 3] 
# Выход: 
# False 
# Требование: 
# Использовать встроенные функции


# 5) Дан массив с числами. Оставьте в нем только отрицательные числа Вход: 
# [1, 2, 3, 0, -1] 
# Выход: 
# [-1] 
# Требование: 
# Использовать встроенные функции 



# 6) Дан массив с числами. Оставьте в нем только четные числа Вход: 
# [1, 2, 3, 0, -1] 
# Выход: 
# [2] 
# Требование: 
# Использовать встроенные функции 


# 7) Дан массив со строками. Оставьте в нем только те строки, длина которых больше 6-ти символов 
# Вход: 
# [“hello”, “world”, “incapsulation”, “inheritance”] 
# Выход: 
# [“incapsulation”, “inheritance”] 
# Требование: 
# Использовать встроенные функции 

# 8) Дан массив с числами. Найдите результат умножения всех этих чисел. Вход: 
# [1, 2, 3, 4] 
# Выход: 
# 10 
# Требование: 
# Использовать встроенную функцию Reduce 
# 9) Напишите программу, которая подсчитывает количество четных и нечетных чисел в списке чисел. (Используйте встроенные функции, чтобы решить эту задачу) 
# Вход: 
# [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Выход: 
# Количество нечетных чисел: 5 
# Количество четных чисел: 4 
# Требование: 
# Использовать встроенные функции
# Подсказка: (map, len, filter, lambda ….) 
# 10) Напишите программу, где исходный список содержит положительные и отрицательные числа. Требуется положительные поместить в один список, а отрицательные - в другой. 
# Вход: 
# [-1, 2, 3, 4, -5, 6, 7, -8, 9] 
# Выход: 
# Положительны: [2, 3, 4, 6, 7, 9] 
# Отрицательные: [-1, -5, -8] 
# Требование: 
# Использовать встроенные функции 
# Подсказка: (map, filter, lambda ….) 
# 11) Напишите программу, в которой указан список целых чисел. Замените отрицательные на -1, положительные на 1, и оставить ноль без изменений. 
# Вход: 
# [-1, 2, 3, 4, -5, 6, 7, -8, 9, 0] 
# Выход: 
# [-1, 1, 1, -1, 1, 1, -1, 1, 0] 
# Требование: 
# Использовать встроенные функции 
# Подсказка: (map, filter, lambda, if, str method replace, ) 
# 12) Аналог “шифра цезаря “. 
# Программа должна запрашивать элементы списка через пробел. После чего пользователь должен ввести значение для сдвига элементов списка. Значение может быть как положительным, так и отрицательным. Если значение положительное, элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести в терминале. Пример: 
# Вход: 
# [1, 2, 3, 4, 5] шаг сдвига=2 
# Выход: 
# [3, 4, 5, 1, 2] 
# 13) https://www.hackerrank.com/challenges/arrays-ds/problem 
# 14) https://www.hackerrank.com/challenges/balanced-brackets/problem?h_r=profile