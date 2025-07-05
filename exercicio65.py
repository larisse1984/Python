n1=int(0)
cont=int(0)
soma=int(0)
contap=int(0)
mediap=int(0)

while(cont!=1):
    n1=int(input("digite um numero"))
    cont=cont+1

    if(n1>0):
        soma=soma+n1
        contap=contap+1
        mediap=soma/contap
    c1=str(input("deseja continuar? [sim] [nao]"))

    