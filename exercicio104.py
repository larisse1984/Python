import random
usu=int(0)
dindin=int(0)


sorte=random.randint(0,15)
print(sorte)
dindin=int(input("quanto em dinheiro em dinheiro vc tem em conta?"))
usu=str(input("escolha cor[vermelho] [preto] [branco]"))

if(usu=="vermelho" and sorte>=0 and sorte<=7):
    dindin=dindin*2
elif(usu=="preto" and sorte>=8 and sorte<=14):
    dindin=dindin*2 
elif(usu=="branco" and sorte==15):
    dindin=dindin*14  
print(f"o valor atual da conta e{dindin}")          