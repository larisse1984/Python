print("digite um numero")
print("escolha uma operação")
print("[1]soma [2]subtracao[3]multiplicacao[4]divisao")
op=int(input(""))


match op:
    case 1:
        print("soma")
    case 2:
        print("subtracao")
    case 3:
        print("multiplicacao")
    case 4:
        print("divisao")             
    