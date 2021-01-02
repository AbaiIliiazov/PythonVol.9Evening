dict_= {
    'Plov':120,
    'Lag':100,
    'Manty':150,
    'Borsh':80,
    'Ashlamfu':90,
    }

dict_['Beshbarmak'] = 130
dict_['Lag'] = 135
del dict_['Borsh']

print(dict_)


d = dict(ugly = 'disgusting',handsome = 'beautiful',easy = 'light')
print(d['easy'])

ab = ['Moscow','Berlin','Tokio']
cd = ['Russia','Germany','Japan']

e = {
    ab[0]:cd[0],
    ab[1]:cd[1],
    ab[2]:cd[2],
}
print(e)


dog = {'name': 'Bobik', 'color': 'black', 'age': 5}
cat = {'name': 'Barsik', 'color': 'white', 'age': 3}

print(f"""'This is a dog. His name is {dog.get('name')}, He is {dog.get('color')} and he is
already {dog.get('age')} years old.""")
print(f"""'This is a cat. His name is {cat.get('name')}, He is {cat.get('color')} and he is
already {cat.get('age')} years old.""")


a = {
    'b2':['Marina','Tanya','Klim'],
    'c2':['Marat','Ulan','Gulnaz'],
}
b2 = ['Marina','Tanya','Klim']
c = list(a)
d = a.get('b2')

print(type(d))
#print(f"""This is {d[2]}, She is in grade {c[0]}""")
#print(f"This is {a['b2'][1]}, She is in grade {list(a.keys())[0]}")

for key,value in a.items():
    print(f"This is {value[0]}, She is in grade {key[1]}")

Задачи на тему: Словари, Методы словарей

1) Это меню вашего ресторана (ключ -- название блюда, значение -- стоимость):
    • menu = {'Lagman': 120, 'Plov': 120, 'Borsh': 100}
    • Добавьте в меню новое блюдо 'Besh barmak' и установите стоимость 130
    • Вы решили, что лагман слишком дешевый. Установите новую цену для него:
135
    • Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
    • Самостоятельно найдите оператор, который удаляет пару “ключ”:”значение”,
и удалите борщ из меню.
    • Выведите оставшиеся блюда

2) Дан словарь, состоящий из элементов типа: слово-синоним. Все слова в словаре
различны. Выведите синоним для последнего слова.
Пример:
Ввод: {‘hello’: ‘hi’, ‘good’: ‘nice’, ‘price’: ‘cost’}
Вывод:  cost

3) Дан список стран и список городов каждой страны. Для каждого города укажите в какой стране он находится.
Пример:
Ввод: [‘Russia’, ‘USA’, ‘German’]
    [‘New York’, ‘Berlin’, ‘Moscow’]
Вывод: {‘Russia’: ‘Moscow’, ‘USA’: ‘New York’, ‘German’: ‘Berlin’}

4)Создайте словари где будут собраны характеристики некоторых животных, затем выведите краткое описание животных, используя данные из словарей.
Пример:
Ввод: dog = {‘name’: ‘Bobik’, ‘color’: ‘black’, ‘age’: 5}
    cat = {‘name’: ‘Barsik’, ‘color’: ‘white’, ‘age’: 3}
Вывод:  This is a dog. His name is Bobik. He is black and he is           already 5 years old.
      This is a dog. His name is Bobik. He is black and he is           already 5 years old.

5) Создайте словарь в котором будет содержаться информация о классах и учениках, ключом будет класс, а значением список с несколькими учениками. Используйте одно имя из списка, который является значением у словаря, для выведения утверждения об этом ученике.
Пример:
Ввод: {'1a': ['John', 'Jessica', 'Tom'], '2b': ['Ben', 'Adam', 'Elena']}
Вывод: This is Tom. He is in grade 1a.
