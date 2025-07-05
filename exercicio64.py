n1=str("")
id=int(0)
sex=str("")
cont=int(0)
hvelho=str("")
mnova=str("")
maior=int(0)
menor=int(999999)

while(cont!=5):
    cont=cont+1
    n1=str(input("digite seu nome"))
    id=int(input("digite sua idade"))
    sex=str(input("qual seu sexo"))
    if(id>maior):
        maior=id
        hvelho=n1
    if(id<menor):
        menor=id
        mnova=n1




print(f"o homem mais velho é{hvelho} e a mulher mais nova é{mnova}")        