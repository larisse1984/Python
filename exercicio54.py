humor=int(input("escolha um humorista [1]fabio porchat [2]danilo gentilli [3]rafinha bastos"))
city=str(input("digite sua cidade"))
id=int(input("qual sua idade?"))

match humor:

    case 1:
        if(city=="araxa"and id>18):
            print("tem show do fabio porchat")
    case 2:
        if(city=="sao paulo"):
            print("tem show do danilo gentilli")
    case 3:
        if(city=="rio grande do sul"):
            print("tem show da rafinha bastos")                 
        