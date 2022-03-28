import numpy as np
from numpy import linalg as la

def newVec(tam):
    vec=[]
    for i in range(tam):
        print("Pos ", i)
        a=float(input("Real ?"))
        b=float(input("Img ?"))
        vec.append(complex(a,b))
    #print(vec)
    return vec

def newMatriz(tam):
    mt=[]
    for i in range(tam):
        mt.append(newVec(tam))
    return mt

def hemitiana(matriz):
    her=matriz.getH()
    for i in range(len(matriz)):
        if la.norm(matriz[i])!=la.norm(her[i]):
            return False
    return True

def menu():
    print("1. Sistema de la posición de la partícula en una recta. Usuario especifica el número de puntos posibles y un vector ket y el sistema calcula las probabilidades de encontrar partícula en una posición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación")
    print("2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.")
    print("3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.")
    print("4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.")

def programOne(pos,numVec,tamano):
    print("Vector ket 1\n")
    protoVec=np.array(newVec(tamano))
    norm = la.norm(protoVec)
    normPos=la.norm([protoVec[pos]])
    res=(normPos**2)/(norm**2)
    print("Probabilidad de encontrarlo en una posición en particular ", res)
    if numVec==2:
        print("Vector ket 2\n")
        otroVec=np.array(newVec(tamano))
        gfg=np.matrix(otroVec)
        adM=gfg.getH()
        adM=np.transpose(adM)
        print(protoVec)
        print(adM)
        trans=adM.dot(protoVec)**2
        print("Probabilida de transitar ",la.norm(trans))


def programTwo(tamano):
    print("Vector ket\n")
    vecKet=np.array(newVec(tamano))
    print("Observable\n")
    observable=np.matrix(newMatriz(tamano))
    if hemitiana(observable):
        bra=observable.dot(vecKet)
        gfg=np.matrix(bra)
        adM=gfg.getH()
        adM=np.transpose(adM)
        media=la.norm(adM.dot(vecKet))
        print("Media: ",media)
        mI=np.identity(tamano)
        sub=mI*media
        delta=observable-sub
        delta=delta.dot(delta)
        gfg = np.matrix(vecKet)
        adM = gfg.getH()
        adM = np.transpose(adM)
        varianza=la.norm(adM[0].dot(np.transpose(delta.dot(vecKet))))
        print("Varianza: ",varianza)
    else:
        print("Matriz no hermitiana")

def programThree(tamano):
    print("Vector ket\n")
    vecKet = np.array(newVec(tamano))
    print("Observable\n")
    observable = np.array(newMatriz(tamano))
    if hemitiana(np.matrix(observable)):
        valoresPropios, vectoresPropios=la.eigh(observable)
        print("Valores Propios: ", valoresPropios)
        probabilida=0
        for i in range(len(vectoresPropios)):
            gfg = np.matrix(vecKet)
            adM = gfg.getH()
            adM = np.transpose(adM)
            # print(adM[0:2])
            # print(vectoresPropios[-i,:])
            # print(valoresPropios[i])
            # print(la.norm(adM.dot(vectoresPropios[-i,:]))**2)
            probabilida+=(la.norm(adM.dot(vectoresPropios[-i,:]))**2)*valoresPropios[i]
            # print(probabilida)
        print("Probabilidad",probabilida)
    else:
        print("Matriz no hermitiana")

def programFour(tamano,clicks):
    print("Vector ket\n")
    vecKet = np.array(newVec(tamano))
    print("Observable\n")
    observable = np.array(newMatriz(tamano))
    if hemitiana(np.matrix(observable)):
        aux=observable.dot(vecKet)
        if clicks>=10:
            clicks=10
        for i in range(1,clicks):
            aux=observable.dot(aux)
        print("Un: ",aux)


