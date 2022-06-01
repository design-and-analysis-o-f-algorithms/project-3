# Camilo Morillo Cervantes (202015224)
# Juan Sebastián Alegría (202011282)
# Proyecto 3

import sys

# Función solución
def decoder(data):
    appear, endIndex = [], 0
    # Se recorre de forma inversa la entrada y se agrega cada caracter nuevo encontrado
    for i in range(len(data)-1, -1, -1):
        c = data[i]
        if c not in appear:
            appear.append(c)
            endIndex = i
    # Los caracteres encontrados se invierten dando el orden en el cual se eliminan
    appear.reverse()
    # Se encuentra la cadena original cifrada usando el orden encontrado
    originalString = coder(data, appear, endIndex)
    if originalString == "NO EXISTE":
        return "NO EXISTE"
    return originalString + " " + "".join(appear)


# Función que cifra diferentes cadenas hasta encontrar una cuyo cifrado concuerde con la entrada
def coder(data, orden, endIndex):
    solution, originalString = "", ""
    while solution != data:  # Mientras la solución no concuerde con la entrada se sigue probando con strings más largos
        if endIndex == len(data):
            return "NO EXISTE"

        endIndex += 1
        originalString = solution = removeString = data[0:endIndex]
        for i in orden:
            removeString = removeString.replace(i, '')
            solution += removeString
    return originalString


def main():
    input = sys.stdin.readline
    numberCases = int(input())  # Número de casos de prueba
    solutions = []
    for _ in range(numberCases):
        data = input().strip()
        # Se llama a la función solución con los datos anteriores
        sol = decoder(data)
        solutions.append(sol)
    for i in solutions:
        print(i)  # Output


main()
