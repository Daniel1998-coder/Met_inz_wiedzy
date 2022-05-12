import math as m

with open("australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]



def metryka_euklidesowa(l1, l2):
    suma = 0
    for i in range(max(len(l1), len(
            l2)) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)


print(metryka_euklidesowa(matrix[0],matrix[1]))
print(metryka_euklidesowa(matrix[0],matrix[2]))
print(metryka_euklidesowa(matrix[0],matrix[3]))


def grupowanie_australijczykow(lista, nr_indexu_decyzyjna, od_kogo):
    grupy = dict()
    y = lista[od_kogo]
    for x in range(1, len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(y, lista[x]))
        else:
            grupy[decyzyjna] = [metryka_euklidesowa(y, lista[x])]
    return grupy


# grup_austr = grupowanie_australijczykow(matrix,14,0)
# #print(grup_austr)
# print(metryka_euklidesowa(matrix[0],matrix[5]))
# print(metryka_euklidesowa(matrix[0],matrix[10]))
# print(metryka_euklidesowa(matrix[0],matrix[20]))

def k_nn(lista, nr_indexu_decyzyjna, nowa_osoba):
    grupy = dict()
    for x in range(0, len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(metryka_euklidesowa(nowa_osoba, lista[x]))
        else:
            grupy[decyzyjna] = [metryka_euklidesowa(nowa_osoba, lista[x])]
    return grupy


def k_nn_lista(lista, nr_indexu_decyzyjna, nowa_osoba):
    grupy = []
    for x in range(0, len(lista)):
        decyzyjna = lista[x][nr_indexu_decyzyjna]
        grupy.append((decyzyjna, metryka_euklidesowa(nowa_osoba, lista[x])))
    return grupy


grupowanie = k_nn(matrix, 14, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# print(grupowanie[0][:5])
# print(grupowanie[1][:5])
grupowanie[0].sort()
grupowanie[1].sort()
# print(grupowanie[0][:5])
print(sum(grupowanie[0][:5]))
# print(grupowanie[1][:5])
print(sum(grupowanie[1][:5]))
print("######################################")


def grupujemy(lista, k):
    grupy = dict()
    for element in lista:
        decyzyjna = element[0]
        if decyzyjna in grupy.keys():
            grupy[decyzyjna].append(element[1])
        else:
            grupy[decyzyjna] = [element[1]]
    for klucz in grupy.keys():
        grupy[klucz].sort()
    for klucz in grupy.keys():
        suma = 0
        for ele in grupy[klucz][:k]:
            suma += ele
        grupy[klucz] = suma
    return grupy


grupy = grupujemy(k_nn_lista(matrix, 14, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 5)
print(grupy[0])
print(grupy[1])


def decyzja(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc = 1
        elif minimum == slownik[key]:
            ilosc += 1
    if ilosc > 1:
        return
    return klasa


print("Decyzja:", decyzja(grupy))
print("######################################")
slownik_testowy_null = {0.0: 4, 1.0: 4, 2.0: 6}
slownik_testowy_2 = {0.0: 4, 1.0: 4, 2.0: 3}
print("Decyzja:", decyzja(slownik_testowy_null))
print("Decyzja:", decyzja(slownik_testowy_2))