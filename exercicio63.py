n1=int(0)
cont=int(0)

while(cont!=7):
    n1=int(input("digite um numero"))
    cont=cont+1

    if(n1%5==0): 
        cont=cont+1
    if(n1%3==0):
        cont=cont+1  

print(f"foram identificados {n1} numeros que são multiplos de cinco e{n1}números que sao multiplos por 3")          
