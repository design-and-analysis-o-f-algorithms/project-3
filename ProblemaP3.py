# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 3

import sys

# Función solución
def decoder(data):
    data = data[0:len(data)-1]
    appear, endIndex = [], 0
    # Se recorre de forma inversa la entrada y se agrega cada caracter nuevo encontrado
    for i in range(len(data)-1, -1, -1):
        if not(data[i] in appear):
            appear.append(data[i])
            endIndex = i
    # Los caracteres encontrados se invierten dando el orden en el cual se eliminan
    appear.reverse()
    # Se encuentra la cadena original cifrada usando el orden encontrado
    originalString = coder(data, appear, endIndex)
    if originalString == "NO EXISTE":
        return "NO EXISTE"
    return originalString + ' ' + (''.join(appear))


# Función que cifra diferentes cadenas hasta encontrar una cuyo cifrado concuerde con la entrada
def coder(data, orden, endIndex):
    solution, originalString = "", ""
    while solution != data:  # Mientras que la solución no concuerde con la entrada se sigue probando con strings más largos
        if endIndex == (len(data)):
            originalString = "NO EXISTE"
            break

        solution = data[0:endIndex+1]
        removeString = solution
        for i in orden:
            removeString = removeString.replace(i, '')
            solution = solution+removeString
        originalString = data[0:endIndex+1]
        endIndex = endIndex+1
    return originalString


def main():
    input = sys.stdin.readline
    numberCases = int(input())  # Número de casos de prueba
    solutions = []
    for c in range(numberCases):
        data = input()
        # Se llama a la función solución con los datos anteriores
        sol = decoder(data)
        solutions.append(sol)
    for i in solutions:
        print(i)  # Output


main()
