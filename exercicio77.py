n1=int(0)
par=int(0)
impar=int(0)
somapar=int(0)
somaimpar=int(0)
cont=int(0)
total=int(0)

for cont in range(0,4,1):
    n1=int(input("digite um numero"))
    if(n1%2==0):
        par=par+1
        somapar=somapar+1
        total=(n1+somapar)
    if(n1%2==1):
        impar=impar 
        somaimpar=somaimpar+1 
        total=(n1+somaimpar)
print(f"doram cadastrados numeros{par}")
print(f"foram cadastrados numeros{impar}")
print(f"a soma dos pares e{somapar}")
print(f"a soma dos impares e {somaimpar}")
print(f"a somatotal e{total}")
       
