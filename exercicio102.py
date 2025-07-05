import random
n1=[3,8,11,14]
s1=n1[random.randint(0,3)]
soma=int(0)
 
usu=int(input("escolha um numero de 1,20"))
if(s1==usu):
    soma=s1+usu
    print(f"a soma{soma}")
else:
    print("vc não acertou o numero")    