# Задачи на тему: String

# 1)Создайте несколько переменных с типом данных str, так, чтобы одна переменная содержала одно слово, затем объедините их в одно предложение, так, чтобы слова были записаны через пробел.
# Пример:
# Ввод:“hello”, “world”, “I’m”, “John”
# Вывод: hello world, I’m John!

# 2)Создайте переменную, поместите туда строку, затем выведите ее 3 раза, через пробел.
# Пример:
# Ввод: “hello”
# Вывод: hello hello hello

# 3)Создайте переменные, которые будут принимать от пользователя строку с его именем и фамилией, затем еще одну переменную в которой будет храниться строка с приветствием, выведите пользователю приветствие.
# Пример:
# Ввод:John, Snow
# Вывод: Hello, John Snow!

# 4)Принимайте от пользователя слово и возвращайте его расположение букв в обратном порядке(используйте срез строк).
# Пример:
# Ввод: “Hello”
# Вывод: olleH




a = "hello "
b = "world, "
c = "I\'m"
d = " John!"
print(a +b+c+d)


a = " hello"
print(a*3)


a = input('Enter your name:')
b = input('Enter your surname:')
print('Hello,', a, b,"!")


a = input("Enter a word:")
print(a[::-1])

