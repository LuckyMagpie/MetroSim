import generador
from sys import argv
import math

def generarLlegadas(numeros):
    variables = []
    log40 = math.log(40)
    log05 = math.log(0.5)
    for R in numeros:
        variables.append(math.ceil(math.exp(R * (log40 - log05) + log05)))

    return variables

def generarBajadas(numeros):
    variables = []
    for R in numeros:
        variables.append(math.ceil(12.267 + (92.333 - 12.267) * R))

    return variables

