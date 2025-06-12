p1=float(input("digite seu peso aqui na terra"))
print("escolha um planeta")
print("[1]mercurio [2]venus [3]marte [4]jupiter [5]saturno [6]urano")
planet=int(input(""))
total=float(0)

match planet:
    case 1:
        total = (p1*0.37)
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   
    case 2:
        total=(p1*0.88)  
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   
    case 3:
        total=(p1*0.38)
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   
    case 4:
        total=(p1*2.64)
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   
    case 5:
        total=(p1*1.15) 
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   
    case 6:
        total=(p1*1.17)  
        print("se vc estivesse no planeta"+str(planet)+"vc pesaria"+str(total))                   





  
          