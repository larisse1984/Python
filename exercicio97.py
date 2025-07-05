media=int(0)
soma=int(0)
maior=int(0)
menor=int(99999)
cont=int(0)
nota=[1,2,3,4,5,6]

for cont in range(0,6,1):
    nota[cont]=int(input("digite sua nota"))
    soma=soma+nota[cont]
    media=soma/6
    if(nota[cont]>maior):
        maior=nota[cont] 
    if(nota[cont]<menor):
        menor=nota[cont]
print(f"a media e{media} ,a maior nota é{maior} e o menor é{menor}")     