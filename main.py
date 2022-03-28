import lib as lb
def main():
    pick=1
    while pick>0:
        lb.menu()
        pick=int(input("? "))
        if pick==1:
            numPos=int(input("Digite el numero de posiciones: "))
            numVectores=int(input("1 o 2 vectores ket"))
            tamano = int(input("Tamano vector ?"))
            lb.programOne(numPos,numVectores,tamano)
        if pick==2:
            tamano=int(input("Tamano matriz: "))
            lb.programTwo(tamano)
        if pick==3:
            tamano=int(input("Tamano matriz: "))
            lb.programThree(tamano)
        if pick>=4:
            tamano = int(input("Tamano matriz: "))
            clicks=int(input("Clicks: "))
            lb.programFour(tamano,clicks)

main()


