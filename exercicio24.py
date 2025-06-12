n1=int(input("digite um numero"))
n2=int(input("digite outro numero"))
s1=int(input("escolha uma opção [1] soma [2]media"))

if(s1==1):
    soma=float(n1+n2)
    print("a soma e"+str(soma))

if(s1==2):
    media=int(n1+n2/2)   
    print(" a media e"+str(media)) 
