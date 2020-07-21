import random
a=int(input("Введіть ліву межу  діапазону"))
b=int(input("Введіть праву межу  діапазону"))
A=random.randint(a,b)
i=int(input("Введіть довільне число"))
while i!=A:
    if i<A:
        print("Ви ввели число, менше задуманого")
        i=int(input("Введіть довільне число"))
    else:
        print("Ви ввели число, більше задуманого")
        i=int(input("Введіть довільне число"))
print("Ви вгадали!")
