# class Parfum:
#     def __init__(self, nev, marka, kiszereles):
#         self.setNev(nev)
#         self.setMarka(marka)
#         self.__kiszereles = kiszereles

#     def setNev(self, nev):
#         self.__nev = nev
#     def setMarka(self, marka):
#         self.__marka = marka

#     def getNev(self):
#         return self.__nev
#     def getMarka(self):
#         return self.__marka
#     def getKiszereles(self):
#         return self.__kiszereles

#     def __str__(self):
#         return f"Márka: {self.getMarka()} - Típus: {self.getNev()} - Kiszerelés: {self.getKiszereles()}"
def median(lista):
    osszeg = 0
    for ar in lista:
        osszeg += ar
    return osszeg // 2

maximum = 0
maxnev = None
with open('./PYTHON/keszlet.txt', 'r', encoding='utf-8') as fajl:
    print("Adj meg 3db parfümöt az alábbi példa alapján: (név; márka; kiszerelés)")
    for i in range(1,4):
        parfum_be = input(f"Add meg a(z) {i}. parfümöt a fenti példa alapján: ")
        reszek = parfum_be.split(";")
        if int(reszek[1]) > maximum:
            maximum = int(reszek[1])
            maxnev = reszek[0]
print(f"A legnagyobb parfüm: {maxnev} volt {maximum} ml-es kiszereléssel.")

with open('./PYTHON/legnagyobb_kiszereles.txt', 'w', encoding='utf-8') as fajl:
    print(maxnev, file=fajl)

arak = []
vege = False
print("Adjon meg további parfümöket ENTER-ig az eddig használt minta alapján: (név; márka; kiszerelés)")
while not vege:
    parfum = input("Add meg a parfüm adatait: ")
    if parfum != "":
        reszek = parfum.split(";")
        p_ar = int(input(f"Add meg a {reszek[0]}  nevű parfüm árát: "))
        arak.append(p_ar)
        if int(reszek[1]) > maximum:
            maximum = int(reszek[1])
            maxnev = reszek[0]
        for b in reszek:
            if b[0].lower() == "a":
                with open('./PYTHON/legnagyobb_kiszereles.txt', 'a', encoding='utf-8') as fajl:
                    print(parfum, file=fajl)
        with open('./PYTHON/keszlet.txt', 'a', encoding='utf-8') as fajl:
            print(parfum, file=fajl)
    else:
        vege = True
print(f"A medián összege: {median(arak)}")