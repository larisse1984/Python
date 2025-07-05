v1=[0,0,0]
cont=int(0)
v14=int(0)

for cont in range(0,3,1):
    v1[cont]=int(input("digite um valor"))
    if(v1[cont]==14):
        v14=v14+1
print(f"apareceu numero{v14} vezes")        