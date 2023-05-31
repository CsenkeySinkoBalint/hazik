n = int(input("Hanyadik szam"))
a = 1
b = 1
if n == 1 or n == 2:
    fib = 1
else:
    for i in range(n-2):
        fib = a+b
        a = b
        b = fib
print(fib)


