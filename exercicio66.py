n1=int(0)
cont=int(0)
conti=str("")

while(cont!=99999):
    n1=int(input("digite um numero"))
    
    cont=cont+1
    if(n1>0 and n1<25):
        print("primeiros")
    if(n1>26 and n1<50):
        print("segundos")
    if(n1>51 and n1<75):
        print("terceiros")
    if(n1>76 and n1<100):
        print("quartos")
    conti=str(input("desejar continuar? [sim] [nao]")) 
    

       
