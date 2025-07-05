import exercicio110funcoes

a=int(input("digite um valor"))
b=int(input("digite outro valor"))
usu=str(input("qual a operacao vc deseja?"))

if(usu=="adicao"):
    exercicio110funcoes.adicao(a,b)
if(usu=="subtracao"):
    exercicio110funcoes.subtracao(a,b) 
if(usu=="multiplicacao"):
    exercicio110funcoes.multiplicacao(a,b)       
if(usu=="divisao"):
    exercicio110funcoes.divisao(a,b)    