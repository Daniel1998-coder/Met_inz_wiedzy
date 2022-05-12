import math as m
import numpy as np
from random import randrange

matrix = []
with open("australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]


def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(max(len(l1), len(l2)) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


def srodek_masy(indeksy: list, lista: list):
    odleglosci = []
    temp_odl = 0
    for ele in indeksy:
        for ele_por in indeksy:
            temp_odl += metryka_euklidesowa(lista[ele], lista[ele_por])
        odleglosci.append(temp_odl)
        temp_odl = 0
    mini = 0
    for i in range(1, len(odleglosci)):
        if odleglosci[mini] > odleglosci[i]:
            mini = i
    return mini


def nauczyciel(lista):
    grupy = dict()
    for ele in lista:
        decyzyjna = ele[14]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(ele)
        else:
            grupy[decyzyjna] = [ele]
    matrix_without_decission = [l[:14] + [float(randrange(len(grupy.keys())))] for l in lista]

    zmiany = True
    while (zmiany):
        zmiany = False
        grupy = dict()
        for i in range(len(matrix_without_decission)):
            decyzyjna = matrix_without_decission[i][-1]
            if decyzyjna in grupy.keys():
                grupy[decyzyjna].append(i)
            else:
                grupy[decyzyjna] = [i]
        new_matrix = []
        for ele in grupy.values():
            new_matrix += ele
        srodki = []
        for lista in grupy.values():
            srodki.append(lista[srodek_masy(lista, matrix_without_decission)])
        odleglosci = []
        for ele in new_matrix:
            for sr in srodki:
                odleglosci.append(metryka_euklidesowa(matrix_without_decission[ele], matrix_without_decission[sr]))
            mini = 0
            ile = 1
            for i in range(1, len(odleglosci)):
                if odleglosci[mini] > odleglosci[i]:
                    mini = i
                    ile = 1
                elif odleglosci[mini] == odleglosci[i]:
                    ile = ile + 1
            if ile == 1:
                if matrix_without_decission[ele][-1] != matrix_without_decission[srodki[mini]][-1]:
                    matrix_without_decission[ele][-1] = matrix_without_decission[srodki[mini]][-1]
                    zmiany = True
            elif ile > 1:
                matrix_without_decission[ele][-1] = None
                zmiany = True
            odleglosci = []
    # for sr in srodki:
    #     print(matrix_without_decission[sr])
    return matrix_without_decission


def matrix_difference(m1, m2):
    ile = 0
    for i in range(len(m1)):
        if (m1[i] != m2[i]):
            ile = ile + 1
    return str((len(m1) - ile) / len(m1) * 100) + " % pokrycia w stosunku do oryginału"


new_matrix = nauczyciel(matrix)
# print(new_matrix)
grupy = dict()
for ele in new_matrix:
    decyzyjna = ele[14]
    if decyzyjna in grupy.keys():
        grupy[decyzyjna].append(ele)
    else:
        grupy[decyzyjna] = [ele]
for key in grupy.keys():
    print("{0}: {1}".format(key, len(grupy[key])))
print(matrix_difference(matrix, new_matrix))
