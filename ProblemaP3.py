# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 3

import sys

# Función solución
def decoder(data):# 
    data=data[0:len(data)-1]
    appear=[]
    endIndex=0
    for i in range(len(data)-1, -1, -1):#Se recorre de forma inversa la entrada y se agrega cada char nuevo encontrado
        if not(data[i] in appear):
            appear.append(data[i])
            endIndex=i
    appear.reverse()#Los char encontrados se invierten dando el orden en el cual se eliminan los char
    originalString=coder(data,appear,endIndex)#Se encuentra el string original cifrando usando el orden encontrado
    if originalString=="NO EXISTE":
        return "NO EXISTE"
    return originalString+' '+(''.join(appear))

def coder(data,orden,endIndex):#Funcion que cifra diferentes strings hasta encontrar cuyo cifrado concuerden con la entrada
    solution=""
    originalString=""
    while solution != data:#Mientras que la solucion no concuerde con la entrada se sigue probando con strings mas largos
        if endIndex==(len(data)):
            originalString="NO EXISTE"
            break

        solution=str(data[0:endIndex+1])
        removeString=str(solution)
        for i in orden:
            removeString=removeString.replace(str(i),'')
            solution=solution+removeString
        originalString=str(data[0:endIndex+1])
        endIndex=endIndex+1

    return originalString


def main():
    input = sys.stdin.readline
    numberCases = int(input())  # Número de casos de prueba
    solutions = []
    for c in range(numberCases):
        data = str(input())
        # Se llama a la función solución con los datos anteriores
        sol = decoder(data)
        solutions.append(sol)
    # Output
    for i in solutions:
        print(i)


main()