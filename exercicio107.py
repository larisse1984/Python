v1=int(0)
pg=int(0)
total=int(0)
desconto=int(0)
aumento=int(0)
p1=int(0)

v1=int(input("digite o valor de sua compra"))
pg=str(input("escolha forma de pagamento->[a vista ou pix] [cartão de credito em 3 vezes] [ou débito]"))

if(pg=="a vista" or pg=="pix"):
    desconto=v1*0.10
    total=v1-desconto
if(pg=="cartaodedebito"):
    desconto=v1*0.05
    total=v1-desconto 
if(pg=="cartaodecredito"):
    p1=int(input("quantas parcelas"))
    if(p1<=3):
        aumento=v1*0.05
        total=v1+aumento 
    if(p1>=4):
        aumento=v1*0.10
        total=v1+aumento
print(f"sua compra de {v1} parcelada em{pg} sendo um total de{total}")

