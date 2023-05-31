

t = list(map(lambda x: list(map(int, x.split("!"))),open("input.txt").read().split("\n")))

print("2. feladat")
from functools import reduce
t4 = reduce(lambda x, y: x * y, t[0])
print(f'A 1. sorban szereplő számok szorzatának nagyságrendje: 10^{len(str(t4))-1}')

print("2. feladat")
print(f'Az 1. sorban szereplő számok átlaga: {sum(t[0])/len(t[0]):0.2f}')

print("3. feladat")
t3 = list(map(lambda x: x**2,sorted(t[1])[-8:]))
print(f'A 2. sorban szereplő 8 legnagyobb szám négyzetének összege: {sum(t3)}')

print("4. feladat")
from functools import reduce
t4 = reduce(lambda x, y: x * y, filter(lambda x: x % 3, t[2]), 1)
print(f'A 3. sorban szereplő 3-mal nem osztható számok szorzatának nagyságrendje: 10^{len(str(t4))}')

from math import sqrt as gy
print("5. feladat")
t50 = sorted(list(filter(lambda x: gy(x) == int(gy(x)),t[4])))
t51 = ", ".join(map(str, t50))
t52 = ", ".join(map(str,map(int, map(gy, t50))))
t5x = reduce(lambda x, y: x + gy(y), filter(lambda x: gy(x) == int(gy(x)), t[4]), 0)
print(f'A 4. sorban szereplő négyzetszámok ({t51}) négyzetgyökeinek ({t52}) összege: {t5x:0.0f}')

print("7. feladat")
print(f'Az inputban szereplő összes szám közül a 12 legkisebb szám maximuma: {max(sorted(sum(t, []))[:12])}')

