v1=[0,0,0,0]
cont=int(0)
par=int(0)
soma=int(0)
impar=int(0)

for cont in range(0,4,1):
    v1[cont]=int(input("digite um valor"))
    if(v1[cont]%2==0):
        soma= soma+v1[cont]   
    if(v1[cont]%2==1):
        print(f" o {v1[cont]} é impar")
print(f"a soma dos pares e{soma}")         

