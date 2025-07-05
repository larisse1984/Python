import random
d1=int(0)
ap=int(0)
m1=float(0)



crash=random.randint(1,10)
print(crash)
d1=int(input("quanto em dinheiro vc tem na conta?"))
ap=int(input("quanto vc vai apostar?"))
if(d1>=ap):
    print("valor suficiente")
else:
    print("insuficiente")    
m1=float(input("em qual multiplicador vc quer parar[1.1][1.3][1.6][2][2.5]"))
if(m1==1.1 and crash >=0 and crash<=9):
    ap=ap*1.1
elif(m1==1.3 and crash>=0 and crash<=8):
    ap=ap*1.3  
elif(m1==1.6 and crash>=0 and crash<=5):
    ap=ap*1.6      
elif(m1==2 and crash>=0 and crash<=4):
    ap=ap*2  
elif(m1==2.5 and crash>=0 and crash<=2):
    ap=ap*2.5   
print(f"sobrou na sua conta{ap}")       

