# Solutions: 
# Task1: 
# a = int(input("Enter a number: "))
# def function(a):
    #     return a%10
# print(function(a))

# Task2: 
# a = int(input("Enter a number: "))
# def function(a): 
#     return f'this is an even number' if a%2 == 0 else 'this is an odd number'
# print(function(a))

# Task3: 
# n = int(input("Enter a number"))
# def function(n):
# 	for i in range(n):
# 	    print(i**2, end = ",")
# function(n)
		
#Task4: 
# a = input("Enter a word")
# def function(a): 
#     if a == a[::-1]: 
#         print("this is palindrome")
#     else: 
#         print("This is not a palindrome")
# function(a)

#Task5: 

# date=input("Enter the date in format 'dd.mm.yyyy':")
# dd,mm,yy=date.split('.')
# dd=int(dd)
# mm=int(mm)
# yy=int(yy)
# if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
#     max1=31
# elif(mm==4 or mm==6 or mm==9 or mm==11):
#     max1=30
# elif(yy%4==0 and yy%100!=0 or yy%400==0):
#     max1=29
# else:
#     max1=28
# if(mm<1 or mm>12):
#     print("False")
# elif(dd<1 or dd>max1):
#     print("False.")
# else: 
#     print("True")


#Task6: 

# number = input("Enter a number: ")
# digitsum = 0

# for digit in number: 
#     digitsum += int(digit)
# print(digitsum)


#Task7:
# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print("The number of digits in the number are:",count)








# 1) Напишите функцию, которая принимает натуральное число и выводит его последнюю цифру.: 
# Вход: 
# 20 
# Выход: 
# 0 
# 2) Напишите программу которая принимает любое число. Если число четное, то программа должна сказать ,что это число четное если нет, то сказать ,что оно нечетное. 
# Вход: 
# 10 
# Выход: 
# Данное число четное! 
# Вход: 
# 9 
# Выход: 
# Данное число не четное! 
# 3) Напишите функцию которая принимает число 'N' и возвращает квадраты всех натуральных чисел кроме числа 'N', в порядке возрастания. 
# Вход: 
# 4 
# Выход: 
# 0,1,4,9 
# 4) Напишите функцию, которая определяет, является ли введенное слово палиндромом 
# (палиндром - слово которая читается пишется одинаково справа налево, и слева направо). 
# Вход: 
# казак 
# Выход: 
# Данное слово палиндром! 
# Вход: 
# сейчас 
# Выход: 
# Данное слово не палиндром! 
# 5) Напишите функцию, которая принимает: день, месяц, год и возвращает 'True' если такая дата есть, если нет то 'False' . 
# Вход: 
# 11.01.2018 
# Выход: 
# True

# 6) Напишите функцию которая принимает 3-значное число и выводит сумму его цифр. Вход: 
# 111 
# Выход: 
# 3 

# 7) Написать функцию, которая определяет количество разрядов введенного целого числа. 
# Вход: 
# Введите число: 65098234 
# Выход 
# Количество разрядов: 8 

# 8) Напишите программу которая будет принимать числа до тех пор, пока пользователь сам не решит остановиться, 
# затем выведите самое максимальное число (нельзя использовать функцию 'max()'). 
# (Дополнительно: напишите Функцию которая принимает 
# уже готовый список чисел(например[22,-3,11]) и выводит минимальное и максимальное 
# значение) 

# 9) Напиши калькулятор используя функции и используйте Try Except во время деления, 
# деление на ноль невозможно. 

# 10) https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=internal-search - Решите эту задачу.

