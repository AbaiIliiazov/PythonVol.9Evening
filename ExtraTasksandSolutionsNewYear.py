
# Solutions: 
# Task1: 
# import math

# r = int(input("Enter radius: "))
# circumference = 2*math.pi*r
# area = math.pi*(r**2)
# print(circumference, area)

#Task2: 
# result = int(input("Enter a number: "))
# if result == 23: 
#     print("Correct")
# else: 
#     print("Incorrect")

#Task3: 
# result = int(input("Enter a number: "))
# if result > 23 and result < 40: 
#     print("Hello")
# else:
#     print("Goodbye")

#Task4: 
# result = int(input("Enter a number: "))
# def function(result): 
#     return "Hello" if result > 23 and result < 40 else "Goodbye"
# print(function(result))

#Task5: 
# 1st option is to solve it via dictionary comprehensions
# i = int(input("Enter a number: "))
# seasons = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
# seasons = {i:value for i,value in seasons.items()}
# print(seasons[i])

# 2nd option is to solve it via if elif constructs (JavaScript's Switch equivalent in Python)
# i = int(input("Enter a number: "))
# seasons = {1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}
# if i == 1: 
#     print(seasons[i])
# elif i == 2: 
#     print(seasons[i])
# elif i == 3: 
#     print(seasons[i])
# elif i == 4: 
#     print(seasons[i])
# else: 
#     raise Exception ("There is no such key")

#Task6:
# a = list(range(0,100))
# for i in a:
#     if i%2 == 0: 
#         print(i, end = ",") 

#Task7: 
# 1st option: 
# res = input("enter name: ")
# if res[0] == 'a': 
#     print("Yes")
# else: 
#     print("No")

#2nd option: 
# res = input("enter name: ")
# def function(res):
#     return "Yes" if res[0] == 'a' else "No"
# print(function(res))

#Task8: 

# a = [8,3,2,1,3,4]
# for i in a: 
#     print(i, end = ',')

#Task9: 
# a = [1,5,2,3] 
# sum =0
# for i in a:
#     sum +=i
# print(sum)

#Task10: 
# list_ = ['а', 'б', 'в']
# b = list_.extend([4,3,5,5])
# print(list_)

#Task11: 
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a+b)

# a = [1, 2, 3]
# b = [4, 5, 6]  
# a.extend(b)
# print(a)


# def result():
#     x = 100
#     def f():
#         nonlocal x 
#         x+=1
#         return x
#     def g():
#         nonlocal x 
#         x-=1
#         return x
#     def h():
#         nonlocal x 
#         x*=2
#         return x
#     def i(): 
#         nonlocal x 
#         x/=2
#         return x
#     return f,g,h,i
# f,g,h,i = result()
# print(f(),g(),h(),i())

# Задание №13
# Напишите функцию которая принимает число и возвращает его двоичный формат 
# (Решать при помощи рекурсии)
# К примеру:

# func(5)///101
# func(6)///110
# func(1234321)///100101101010110010001

#Task13: 
x = int(input("Enter a number: "))
def func(x): 
    if x == 0: 
        return 0
    else: 
        return bin(func(x))
                        break
print(func(x))

# На закрепление
# Задание №1
# Написать программу расчета площади и окружности круга по радиусу.
# Ввести радиус:
# Вывести площадь и окружность

# Задание №sult()2
# Если содержимое переменной result равна 23, то выведите 'Верно', иначе
# выведите 'Неверно'.
# result = int(input('Введите число: ')

# Задание №3
# Если содержимое переменной result больше 23 и меньше 40, выведите ‘Hello’,
# иначе выведите ‘Goodbye’.

# Задание №4
# Сделайте 3-e задание используя Условный (тернарный) оператор.

# Задание №5
# Есть переменная seasons, если пользователь ввел цифру 1, то выведите
# сообщение ‘зима’, если 2-’весна’, если 3-лето, 4-осень. Используйте Конструкцию
# ‘Switch’
# let seasons = +prompt(‘Введите число от 1-4’)

# Задание №6
# Используя цикл for вывести все четные числа от 1 до 100;

# Задание №7
# Есть переменная res, если пользователь вводит текст и первая буква текста
# начинается с ‘a’, то выведите сообщение ‘да’, иначе ‘нет’. Например:
# let res = +prompt(‘наберите текст’) // пример ввода: ‘abcd’
# Сделайте используя if else, затем используя Условный оператор

# Задание №8
# Дан массив с элементами [8,3,2,1,3,4]. С помощью цикла for выведите все
# элементы в консоль.

# Задание №9
# Дан массив с элементами [1,5,2,3]. С помощью цикла найдите сумму этого
# массива.

# Задание №10
# Дан массив ['а', 'б', 'в']. Добавьте ему в конец элементы 4,3,5,5.

# Задание №11
# Даны два массива: [1, 2, 3] и [4, 5, 6]. Объедините их вместе.
# let arr1 = [1, 2, 3];
# let arr2 = [4, 5, 6];

# Задание №12
# Напишите функцию которая возвращает массив из 4 функций; 
# первая увеличивает счетчик( переменная i )  на 1
# вторая уменьшает на 1
# третья умножает на 2
# четвёртая делит на 2

# (**сделать задание при помощи замыкания!!)


# Задание №13
# Напишите функцию которая принимает число и возвращает его двоичный формат 
# (Решать при помощи рекурсии)
# К примеру:

# func(5)///101
# func(6)///110
# func(1234321)///100101101010110010001

