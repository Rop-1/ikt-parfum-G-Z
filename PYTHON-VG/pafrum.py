class Parfum:
    def __init__(self, nevmarka, kiszereles):
        self.setNevmarka(nevmarka)
        self.__kiszereles = kiszereles

    def setNevmarka(self, nevmarka):
        self.__nevmarka = nevmarka

    def getNevmarka(self):
        return self.__nevmarka
    
    def getKiszereles(self):
        return self.__kiszereles

    def __str__(self):
        return f"Név és márka: {self.getNevmarka()} - Kiszerelés: {self.getKiszereles()}"
    
def median(lista):
    lista.sort()
    if len(lista) % 2 == 1:
        return lista[len(lista) // 2]
    return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2

parfum_arak = []

parfumok = []
maximum = 0
maxnev = None

for i in range(3):
    parfum = input("Add meg a parfüm adatait az alábbi módon (Név Márka;Kiszerelés): ")

    reszek = parfum.split(";")
    parfum_ar = int(input(f"Add meg a {reszek[0]} nevű parfüm árát: "))
    parfum_l = Parfum(reszek[0], reszek[1])
    parfumok.append(parfum_l)

    if int(reszek[1]) > maximum:
        maximum = int(reszek[1])
        maxnev = reszek[0]

print(f"A legnagyobb kiszerelésű parfüm neve: {maxnev} volt {maximum} ml-es gyártással.")

with open("./PYTHON-VG/legnagyobb_kiszereles.txt", "a", encoding="utf-8") as legnagyobb_parfum:
    print(maxnev, file=legnagyobb_parfum)

with open("./PYTHON-VG/keszlet.txt", "r", encoding="utf-8") as parfumok_fajl:
    for parfum_adat in parfumok_fajl:
        reszek = parfum_adat.split(";")
        parfum_l = Parfum(reszek[0], reszek[1])


vege = False
print("Adj meg további parfüm adatokat ENTER-ig!")

maximuml = []
maximum = 0
maxnevl = []

while not vege:
    parfum = input("Add meg a parfüm adatait az alábbi módon (Név Márka;Kiszerelés): ")

    if parfum == "":
        if len(maximuml) > 0 and len(maxnevl) > 0:
            uj_maximuml = []
            uj_maxnevl = []
            i = 0
            while i < len(maximuml):
                if maximuml[i] == maximum:
                    uj_maximuml.append(maximuml[i])
                    uj_maxnevl.append(maxnevl[i])
                i += 1
            maximuml = uj_maximuml
            maxnevl = uj_maxnevl
        vege = True
    else:
        with open("./PYTHON-VG/keszlet.txt", "a", encoding="utf-8") as bekert_parfum:
            print(parfum, file=bekert_parfum)

        reszek = parfum.split(";")
        parfum_ar = int(input(f"Add meg a {reszek[0]} nevű parfüm árát: "))

        if int(reszek[1]) > maximum:
            maximum = int(reszek[1])
            maximuml = [int(reszek[1])]
            maxnevl = [reszek[0]]
        elif int(reszek[1]) == maximum:
            maximuml.append(int(reszek[1]))
            maxnevl.append(reszek[0])

with open("./PYTHON-VG/legnagyobb_kiszereles.txt", "a", encoding="utf-8") as legnagyobb:
    for parfing in maxnevl:
        print(parfing, file=legnagyobb)

print("A parfümök árának mediánja:", median(parfum_arak))