fib_0=0
fib_1=1
fibs=[0,1]
max=int(input("Введіть максимальне число"))
i=0
while i<max:
    fib=fib_0+fib_1
    fib_0=fib_1
    fib_1=fib
    fibs.append(fib_1)
    i=i+1
print(fibs)
