s1=str(input("qual serie que fala sobre fantasmas e lendas"))
s2=int(input("quantas temporadas tem esse serie?"))
s3=str(input("digite dois personagens principais"))
s4=int(input("qual episodio da primeira temporada que fala de um espantalho?"))
s5=str(input("qual dos irmãos tem poder da visão"))

contador=int(0)
if(s1== "supernatural"):
    contador=contador+1

if(s2==15):
    contador=contador+1   

if(s3=="dien e sam"):
    contador=contador+1 

if(s4==11):
    contador=contador+1 

if(s5=="sam"):
    contador=contador+1

    print("o contador tem tantos"+str(contador))
