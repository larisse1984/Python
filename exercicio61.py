contador=int(0)
somapar=int(0)
somaimpar=int(0)

while(contador!=5):
    contador=contador+1
    n1=int(input("digite um numero"))
    if(n1%2==0):
        somapar=somapar+n1
    if(n1%2==1):
        somaimpar=somaimpar+n1

print(f"a soma dos impares e {somaimpar}e a soma dos pares e {somapar}")
