# Autor: Raúl Beltrán Marco
# Ruta donde se encuentre data.csv
dataPath = "data.csv"
# Ruta donde se generará el resultado de la ejecución del programa
resultPath = "result.csv"


def clearString(reversedString):
    result = ""
    index = len(reversedString) 
    while index > 0: 
        result += reversedString[ index - 1 ] 
        index = index - 1 
    # Ahora tenemos el string en sentido normal
    result = result.replace('\'', '')
    result = result.replace(',', '')
    result = result.replace(']', '')
    result = result[1:]
    if result == "Sin opiniÃ³n":
        result = "Sin opinión"

    return result

def processLine(line):
    # Array con los resultados de los SUS
    result = []
    i = 0
    for character in line:
        if character == ']':
            index = i
            reversedString = ""
            while line[index] != ',': 
                reversedString += line[ index - 1 ]
                index = index - 1
            result.append(clearString(reversedString))
        i += 1
    # Sobra el último (duplicado)
    if len(result) != 0:
        result = result[:-1]
    return result

def obtainData():
    #Array de arrays con los resultado de los SUS
    data = []

    # Using readlines()
    file = open(dataPath, 'r')
    Lines = file.readlines()
    
    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        if count != 0:
            data.append(processLine(line))
    return data

def createCSV(data):
    cabecera = "SUS1;SUS2;SUS3;SUS4;SUS5;SUS6;SUS7;SUS8;SUS9;SUS10"
    with open(resultPath, 'a') as resultFile:
        resultFile.write(cabecera)
        # Recorremos un resultado de data
        for results in data:
            for result in results:
                resultFile.write(result + ";")
            resultFile.write('\n')
# MAIN
def main():
    data = obtainData()
    createCSV(data)
    # print(data)


main()