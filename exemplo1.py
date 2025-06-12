a=int(input("digite um numero"))



if(a>10):
    print("deu certo")
else:
    print("deu errado")

if(a>10 and a<20):
    print("deu errado 1")
elif(a>20 or a <30):#elif equivale a senao se
    print("deu errado")

    
    import random
    a=random.randint(10,20)
    print(a)