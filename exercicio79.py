cont=int(0)
n1=str("")
sexo=str("")
homem=int(0)

for cont in range(0,3,1):
    n1=str(input("qual seu nome?"))
    sexo=str(input("digite seu sexo"))
    if(sexo=="masculino"):
        homem=homem+1
print(f"tantos {homem}foram cadastrados")    
 

