def analisar(v1,v2,v3):
    maior=int(0)
    menor=int(99999)


    if(v1>maior):
        maior=v1
    if(v2>maior):
        maior=v2
    if(v3>maior):
        maior=v3
    if(v1<menor):
        menor=v1
    if(v2<menor):
        menor=v2
    if(v3<menor):
        menor=v3
    print(f"o menor numero e{menor} e o maior e{maior}")                            
