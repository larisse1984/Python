import random
jogador=random.randint(0,2)
print(jogador)
a=int(0)

a=("pedra","papel","tesoura")
a=str(input("o que vc quer jogar? [0]pedra [1]papel [2]tesoura"))

if(jogador==0 and a=="pedra"):
    print("empate")
if(jogador==0 and a=="papel"):
    print("vitoria do papel")
if(jogador==0 and a=="tesoura"):
    print("vitoria da tesoura") 
if(jogador==1 and a=="pedra"):
    print("empate")
if(jogador==1 and a=="papel"):
    print("vitoria do papel") 
if(jogador==1 and a=="tesoura"):
    print("vitoria da tesoura")
if(jogador==2 and a=="pedra"):
    print("empate")
if(jogador==2 and a=="papel"):
    print("vitoria do papel") 
if(jogador==2 and a=="tesoura"):
    print("vitoria da tesoura")   

           


