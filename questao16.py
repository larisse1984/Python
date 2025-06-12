p1=int(input("qual seu peso?"))
a1=float(input("qual sua altura?"))
imc=float(p1*(a1*a1))
pi=float(21.75*(a1*a1))
if(imc<18.5):
    print("abaixo do peso")
    print("coma carboidrados")
if(imc>=18.5 and imc<=24.9):
    print("peso normal") 
    print("coma verduras e legumes cozidos")
if(imc>=25 and imc<=29.9):
    print("sobre peso") 
    print("comer somente salada e suco de couve no inervalos")
if(imc>=30 and imc<=34.9):
    print("obesidade 1")
    print("comer de 3 em 3 horas")
if(imc>=35 and imc<=39.9):
    print("obesidade 2")
    print("comer somente carne") 
if(imc>=40):
    print("obesidade 3 ou mórbida")
    print("somente cirurgia de redução de estomago") 

print("você precisa ganhar ou perder"+str(pi)+"peso")           
