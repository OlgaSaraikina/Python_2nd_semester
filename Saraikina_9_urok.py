 #Task 1
print("Ведите количество чисел от 1 до 100000:")
n = int(input())
if 1 <= n <= 100000:
    print("Ведите числа через пробел, каждое из которых не превышает 20000000000")
    res = list(map(int, input().split(' ')))
    tmp = set()
    for i in range(len(res)):
        if res[i] < 20000000000:
            tmp.add(res[i])
else:
    print("Число меньше 1 или больше 100000")
print(len(tmp))
 #Task 2
a = set(map(int, input('Ввод числа через пробел: ').split()))
b = set(map(int, input('Ввод числа через пробел: ').split()))
ser = a & b
print(len(ser))

 #Task 3
used = set()
spi = list(map(int, input('Ввод числа через пробел: ').split(' ')))
for i in range(len(spi)):
    if spi[i] in used:
        print(f"{spi[i]} - YES")
    else:
        used.add(spi[i])
        print(f"{spi[i]} - NO")
