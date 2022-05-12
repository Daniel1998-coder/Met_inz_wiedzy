import math as m
import numpy as np

a=[[1,2],[3,4]]

def srednia_aryt(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja(lista):
    srednia = srednia_aryt(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie(lista):
    return m.sqrt(wariancja(lista))

print(srednia_aryt(a))
print(wariancja(a))
print(odchylenie(a))