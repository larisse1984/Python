import random
usu=int(0)
dindin=int(0)


sorte=random.randint(0,2)
print(sorte)
dindin=int(input("quanto em dinheiro em dinheiro vc tem em conta?"))
usu=str(input("escolha cor[vermelho] [preto] [branco]"))
if(usu=="vermelho" and sorte==0):
    dindin=dindin*2
elif(usu=="preto" and sorte==1):
    dindin=dindin*2 
elif(usu=="branco" and sorte==2):
    dindin=dindin*14       
else:
    print("vc perdeu toda aposta") 
print(f"o valor atual de sua conta é{dindin}")       
