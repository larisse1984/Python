v1=float(input("qual é a velocidade do carro?"))
ex=int(v1-80)
if(v1<=80):
    print("velocidade segura")

if(ex>0 and ex<20):
    m1=150+5*ex
    print("a multa é de"+str (m1))

if(ex>21 and ex<80):
    m1=250+10*ex    
    print("a multa e de"+str(m1))

if(ex>81 and ex<200):
    m1=500+20*ex
    print("a multa e de"+str(m1))    