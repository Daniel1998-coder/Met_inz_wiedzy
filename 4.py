import math
import numpy as np


def func1(x):
    return x

def monte_carlo(func, poziom, pion, ilosc_pkt):
    iloscPodWykresem = 0
    punkty_x = np.random.uniform(0, poziom, ilosc_pkt)
    punkty_y = np.random.uniform(0, pion, ilosc_pkt)
    punkty_y_wyliczone = [func(x) for x in punkty_x]

    for i in range(len(punkty_y)):
        if punkty_y[i] <= punkty_y_wyliczone[i]:
            iloscPodWykresem += 1

    pole = iloscPodWykresem / ilosc_pkt * poziom * pion

    return round(pole, 2)


def metodaProstokatowIlosc(iloscPodzialow, funkcja, poziom):
    suma = 0
    for i in range(1, iloscPodzialow + 1):
        x_0 = poziom / iloscPodzialow * (i - 1)
        x_1 = poziom / iloscPodzialow * i
        y_0 = funkcja(x_0)
        y_1 = funkcja(x_1)
        srednia = (y_0 + y_1) / 2
        suma += srednia
    return suma / iloscPodzialow


def metodaProstokatowEpsilon(epsilon, funkcja, poziom):
    suma1 = 0
    iloscPodzialow = 0
    wynik = math.inf
    while wynik >= epsilon:
        suma = 0
        iloscPodzialow += 10
        for i in range(1, iloscPodzialow + 1):
            x_0 = poziom / iloscPodzialow * (i - 1)
            x_1 = poziom / iloscPodzialow * i
            y_0 = funkcja(x_0)
            y_1 = funkcja(x_1)
            srednia = (y_0 + y_1) / 2
            suma += srednia
        if suma1 == 0:
            suma1 = suma
        else:
            wynik = (suma - suma1) / iloscPodzialow
            suma1 = suma

    return suma / iloscPodzialow


print(f"Epsilon: {metodaProstokatowEpsilon(0.02, func1, 10)}")
print(f"Prostokaty: {metodaProstokatowIlosc(1, func1, 10)}")
print(f"Prostokaty: {metodaProstokatowIlosc(10, func1, 10)}")
print(f"Prostokaty: {metodaProstokatowIlosc(1000, func1, 10)}")
print(f"Prostokaty: {metodaProstokatowIlosc(10000, func1, 10)}")
print(f"Monte Carlo: {monte_carlo(func1, 10, 10, 100)}")