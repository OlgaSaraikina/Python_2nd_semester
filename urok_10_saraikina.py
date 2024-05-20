
print("Task 1")
pets = dict()
print("Введите имя питомца")
name_p = input()
pets[name_p] = k = dict()
t = 'вид питомца'
a = 'возраст питомца'
name = 'имя владельца'
k[t] = input("Введите вид питомца:")
k[a] = int(input("Введите возраст питомца:"))
k[name] = input("Введите имя владельца:")
for i in pets.keys():
    for j in k.values():
        if j == k[t]:
            jt = j
        elif j == k[a]:
            ja = j
        elif j == k[name]:
            m = j
print(f"Это {jt}, по кличке {i}.Возраст питомца: {ja} лет. Имя владельца {m}")

print("Task 2")

dick = {x:x**x for x in range(10, -6, -1)}
print(dick)


# методы keys() и values() возвращают все значениия, т. е. все ключи или все занчения. При попытке вывести это в принт, рапаковку сделать не возможно
#print(f"Это {pets[name_p][t]}, по кличке {}. Возраст питомца: {pets[name_p][a]} лет. Имя владельца {pets[name_p][name]}")