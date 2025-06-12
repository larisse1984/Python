v1=int(input("qual o valor da casa?"))
s1=int(input("digite seu salário"))
m1=int(input("quantos meses você deseja pagar"))

f1=int(v1/m1)
d1=int(0.30*s1)
if(d1>f1):
    print("deu certo")
else:
    print("emprestimo negado")    