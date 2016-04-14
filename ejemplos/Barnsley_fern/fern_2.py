#!/usr/bin/env python3

##
##
##
##
## 
##

import random

def iterar(coordenadas,parametros_A,parametros_b):
    resultado=[0,0]
    for i in range(0,len(coordenadas)):
        resultado[i] += parametros_b[i]
        for j in range(0,len(parametros_A[i])):
            resultado[i]+=parametros_A[i][j]*coordenadas[j]
    return resultado

def variarParametros():
    parametros_b = [0.0,0.0]
    matriz_resultado  = [[0,0],[0,0]];
    rand = random.random()
    if (rand < 0.01):
        matriz_resultado[0][0] = 0
        matriz_resultado[0][1] = 0
        matriz_resultado[1][0] = 0
        matriz_resultado[1][1] = 0.16
        parametros_b[0] = 0
        parametros_b[1] = 0
        return matriz_resultado, parametros_b
    if  ((0.01 <= rand) and (rand <= 0.85)):
        matriz_resultado[0][0] = 0.85
        matriz_resultado[0][1] = 0.04
        matriz_resultado[1][0] = -0.04
        matriz_resultado[1][1] = 0.85
        parametros_b[0] = 0.00
        parametros_b[1] = 1.66
        return matriz_resultado, parametros_b
    if  ((0.85 < rand) and (rand <= 0.92)):
        matriz_resultado[0][0] = 0.20
        matriz_resultado[0][1] = -0.26
        matriz_resultado[1][0] = 0.23
        matriz_resultado[1][1] = 0.22
        parametros_b[0] = 0.00
        parametros_b[1] = 1.60
        return matriz_resultado, parametros_b
    if ((0.92 < rand) and (rand < 1.0)):
        matriz_resultado[0][0] = -0.15
        matriz_resultado[0][1] = 0.28
        matriz_resultado[1][0] = 0.26
        matriz_resultado[1][1] = 0.24
        parametros_b[0] = 0.00
        parametros_b[1] = 0.44
        return matriz_resultado, parametros_b


coordenadas_n = [0,0];
matriz_A   = [[0.2,-0.1],[0.4,0.2]];
parametros_b = [0.57,0.036]
coordenadas_n_1 = [0,0]

for i in range(0,50000):
    coordenadas_n_1 = iterar(coordenadas_n,matriz_A,parametros_b)
    matriz_A, parametros_b =  variarParametros()
    coordenadas_n = coordenadas_n_1
    print(coordenadas_n)
