n1=int(input("digite um número"))
n2=int(input("digite outro número"))
n3=int(input("digite um número"))
n4=int(input("digite outro número"))

par=int(0)
maior=int(0)
soma=int(0)
if(n1%2==0):
    soma=soma+n1
if(n2%2==0):
    soma=soma+n2
if(n3%2==0):
    soma=soma+n3
if(n4%2==0):
    soma=soma+n4 


if(n1>maior):
    maior=n1
if(n2>maior):
    maior=n2
if(n3>maior):
    maior=n3
if(n4>maior):
    maior=n4  

if(n1%2==0):
    par=par+1
if(n2%2==0):
    par=par+1
if(n3%2==0):
    par=par+1
if(n4%2==0):
    par=par+1        
print("foram digitados"+str(par)+"pares") 
print("a soma desse números pares é"+str(soma))   
print("o maior número par é"+str(maior))                         