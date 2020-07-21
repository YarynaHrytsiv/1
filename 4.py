a=int(input("Введіть ліву межу діапазону"))
b=int(input("Введіть праву межу діапазону"))
n=int(input("Введіть крок"))
j=a
for j in range(a,b+1,n):
    p=1
    i=1
    while i<=j:
        p=p*i
        i+=1
    print(p)
    
