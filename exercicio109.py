import random
jogador=random.randint(0,2)
print(jogador)
a=int(0)

a=("pedra","papel","tesoura","lagarto","spock")
a=str(input("o que vc quer jogar? [0]pedra [1]papel [2]tesoura[3]lagarto [4]spock"))

if(jogador==0 and a=="pedra"):
    print("empate")
if(jogador==0 and a=="papel"):
    print("vitoria do papel")
if(jogador==0 and a=="tesoura"):
    print("vitoria da tesoura")
if(jogador==0 and a=="lagarto"):
    print("vitoria do lagarto")
if(jogador==0 and a=="spock"):
    print("vitoria do spock")         
if(jogador==1 and a=="pedra"):
    print("empate")
if(jogador==1 and a=="papel"):
    print("vitoria do papel") 
if(jogador==1 and a=="tesoura"):
    print("vitoria da tesoura")
if(jogador==1 and a=="lagarto"):
    print("vitoria do lagarto")
if(jogador==1 and a=="spock"):
    print("vitoria spock")        
if(jogador==2 and a=="pedra"):
    print("empate")
if(jogador==2 and a=="papel"):
    print("vitoria do papel") 
if(jogador==2 and a=="tesoura"):
    print("vitoria da tesoura") 
if(jogador==2 and a=="lagarto"):
    print("empate")
if(jogador==3 and a=="pedra"):
    print("vitoria do pedra") 
if(jogador==3 and a=="papel"):
    print("vitoria da lagarto") 
if(jogador==3 and a=="tesoura"):
    print("perde para tesoura")   
if(jogador==4 and a=="pedra"):
    print("vitoria do spock") 
if(jogador==4 and a=="papel"):
    print("vitoria da papel") 
if(jogador==4 and a=="tesoura"):
    print("vitoria spock")   

           


