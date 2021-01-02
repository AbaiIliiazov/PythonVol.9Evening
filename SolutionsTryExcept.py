
#Solutions:
#Task1:

# a = int(input("Enter a number"))
# b = int(input("Enter another number"))
# c = a+b

# if b == 0:
#     raise ValueError ("The input expects only integers")
# else:
#     print(c,"\noperation is complete")

#Task2:

# try:
#     a = int(input("Enter a number"))
#     b = int(input("Enter another number"))
#     c = a+b
#     print(c)
# except ValueError:
#     print("you entered wrong type, input expects numbers")
# finally: 
#     print("operation is complete")

#Task3:
# try:
#     key = input("Enter key: ")
#     a = {'a':'value1', 'b':'value2', 'c':'value3', 'd':'value4', 'e':'value5'}
#     value = a[key]
   
# except KeyError:
#     print("There is no such key")
# else: 
#     print(value)

#Task4: 


# task1_input = input("write down a list ")
 
# if task1_input.startswith('[') and task1_input.endswith("]"): 
#     print("GJ fella")
# else: 
#     raise Exception('Input accepts only a list')

    


#Task5: 
# index = int(input("Enter index: "))
# a = ['Abai','Nabil','Askat']
# try: 
#     b = a[index]
# except IndexError: 
#     print("wrong index")
# else:
#     print(b)

# Try Except 
# 1) Напишите программу которая будет получать два числа через input и будет их делить, пайтон знает, 
# что на ноль делить нельзя и выводит ZeroDivisionError 
# ваша задача обработать исключение и выдать через raise свою кастомную понятную ошибку. 
# Вход: 
# 2, 0 
# Выход: 
# Exception: к сожалению на ноль делить нельзя 
# Требование: 
# Использовать try except 

# 2) Напишите программу которая будет получать через input два числа и будет возвращать сумму данных чисел. 
# Так как мы знаем, что input всегда возвращает строку, необходимо ее сразу поменять в тип данных integer, 
# во время конвертации, если пользователь вместо числа отправил букву, то возникнет ошибка, 
# ваша задача обработать и выдать свое исключение . 
# Вход: 
# 2 
# a 
# Выход: 
# Exception: Вы задали неправильный параметр, инпут ожидает число 
# Требование: 
# Использовать try except 


# 3) Напишите программу, которая будет обрабатывать ошибку KeyError в словаре Вход: 
# dict_ = {“key1”: “value1”, “key2”: “value2”} 
# dict[“key3”] ---> KeyError 
# Выход: 
# Exception: Нет такого ключа 
# Требование: 
# Использовать try except 

# 4) Напишите программу, которая от пользователя должна получать только list, 
# но если к нему приходит другой тип данных, то должны выдать свою кастомную ошибку 
# Вход: 
# “hello” 
# Выход: 
# Exception: Данная программа принимает только тип данных list 


# 5) Напишите скрипт, который будет обрабатывать ошибку IndexError (list index out of range), если индекс за пределом списка, то мы должны выдавать последний индекс в списке 
# Вход: 
# lists = [1, 2, 3, 4]
# lists[5] --- > IndexError 
