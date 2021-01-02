a = {1, 6, 4, 0, 34, 17, 100, -45}
b = {22, 0, 3, 100, 4}    

#print(a.intersection(b), a.difference(b), a.union(b),sep="\n") 


Aibek = {'Dodo','Imperia','FreshBox'}
Aidai = {'Ojakkebab','FreshBox'}
Azat = {'FreshBox','KFC'}
Gulzana = {'Dodo','Imperia','FreshBox','Ojakkebab','KFC'}

#print(Gulzana.intersection(Aibek,Aidai,Azat))

a = set(list(range(1,31)))
print(a)


John = {5, 7, 11, 10, 28}
Rachel = {29, 2, 6, 12, 3}
Katrin = {1, 5, 14, 8, 22}
Sam = {19, 20, 3, 11, 10}

print(Rachel.intersection(John), Katrin.intersection(John), Sam.intersection(John))


Ingredients = {'сыр', 'чеддар','грибы', 'соус', 'шпинат'}
Ingredients.add('помидор')
#Ingredients.remove('колбаса')
Ingredients.remove('шпинат')
Ingredients.add('базилик')
Ingredients.remove('чеддар')
Ingredients.add('моцарелла')

print(Ingredients)






