id=int(input("digite sua idade"))
id2=int(input("digite uma idade"))
id3=int(input("digite sua idade"))
id4=int(input("digite uma idade"))

maior=int(0)
menor=int(99999999)

if(id>maior):
    maior=id
if(id2>maior):
    maior=id2
if(id3>maior):
    maior=id3
if(id4>maior):
    maior=id4   

if(id<menor):
    menor=id
if(id2<menor):
    menor=id2 
if(id3<menor):
    menor=id3
if(id4<menor):
    menor=id4   

print("o mais jovem"+str(menor)+"anos e o mais velho tem"+str(maior)+"anos")                     