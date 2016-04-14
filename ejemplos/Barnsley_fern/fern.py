#!/usr/bin/env python3

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
    if (rand < 0.02):
        matriz_resultado[0][0] = 0
        matriz_resultado[0][1] = 0
        matriz_resultado[1][0] = 0
        matriz_resultado[1][1] = 0.27
        parametros_b[0] = 0.5
        parametros_b[1] = 0
        return matriz_resultado, parametros_b
    if  ((0.02 <= rand) and (rand <= 0.17)):
        matriz_resultado[0][0] = -0.139
        matriz_resultado[0][1] = 0.263
        matriz_resultado[1][0] = 0.246
        matriz_resultado[1][1] = 0.224
        parametros_b[0] = 0.57
        parametros_b[1] = -0.036
        return matriz_resultado, parametros_b
    if  ((0.17 < rand) and (rand <= 0.3)):
        matriz_resultado[0][0] = 0.17
        matriz_resultado[0][1] = -0.2150
        matriz_resultado[1][0] = 0.2220
        matriz_resultado[1][1] = 0.160
        parametros_b[0] = 0.408
        parametros_b[1] = 0.0893
        return matriz_resultado, parametros_b
    if ((0.3 < rand) and (rand < 1.0)):
        matriz_resultado[0][0] = 0.7810
        matriz_resultado[0][1] = 0.0340
        matriz_resultado[1][0] = -0.0320
        matriz_resultado[1][1] = 0.7390
        parametros_b[0] = 0.1075
        parametros_b[1] = 0.27
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
