p1=int(input("qual o preço do produto?"))
escolha=int(input("escolha em que epoca estamos?[1]carnaval [2]ferias [3]dcriancas[4]black [5]natal"))

if(escolha==1):
    total = p1+(p1*0.10)
    print(total)
if(escolha==2):
    total=p1+(p1*0.20) 
    print(total) 
if(escolha==3):
    
    p1+(p1*0.05) 
    print(total) 
if(escolha==4):
    p1+(p1*0.30)
    print(total)  
if(escolha==5):
    p1+(p1*0.05)
    print(total)         

print("o preco final e"+str(total))