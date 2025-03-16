class Parfum:
    def __init__(self,marka, kiszereles):
        self.__marka = marka
        self.__kiszereles = kiszereles

    def getMarka(self):
        return self.__marka
    
    def getKiszereles(self):
        return self.__kiszereles

    def __str__(self):
        return f"{self.getMarka()};{self.getKiszereles()}"


def median(lista):
    lista.sort()
    if len(lista) == 0:
        return None
    if len(lista) % 2 == 1:
        return lista[len(lista) // 2]
    return (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2



parfumok = []
with open("parfum.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        reszek = sor.strip().split(";")
        if len(reszek) == 2 and reszek[1].isdigit():
            nev_mark = reszek[0].split(" ", 1)
            if len(nev_mark) == 2:
                parfumok.append(Parfum(nev_mark[0], int(reszek[1])))

uj_parfumok = []

vege = False
print("Adj meg további parfüm adatokat az alábbi módon (Név Márka;Kiszerelés). Üres ENTER-rel kiléphetsz.")
while not vege:
    adat = input("Parfüm adatok: ")
    if adat == "":
        vege = True
        continue

    reszek = adat.split(";")
    if len(reszek) == 2 and reszek[1].isdigit():
        parfumok.append(Parfum(reszek[0], int(reszek[1])))
        uj_parfumok.append(adat)
    else:
        print(f"Hibás formátum!\nPélda: Chanel No.5;50")




print("További 3 parfüm")
for i in range(3):
    adat = input("Parfüm adatok: ")
    if adat == "":
        vege = True
        continue

    reszek = adat.split(";")
    if len(reszek) == 2 and reszek[1].isdigit():
        parfumok.append(Parfum(reszek[0], int(reszek[1])))
        uj_parfumok.append(adat)
    else:
        print(f"Hibás formátum!\nPélda: Chanel No.5;50")

if uj_parfumok:
    with open("parfum.txt", "a", encoding="utf-8") as fajl:
        for adat in uj_parfumok:
            fajl.write(f"\n{adat}")


max_kiszereles = 0
max_parfumok = []

for p in parfumok:
    if p.getMarka().lower().startswith("a") and p.getKiszereles() >= max_kiszereles:
        if p.getKiszereles() > max_kiszereles:
            max_kiszereles = p.getKiszereles()
            max_parfumok = [p.getMarka()]
        elif p.getKiszereles() == max_kiszereles:
            max_parfumok.append(p.getMarka())

with open("legnagyobb_parfum.txt", "w", encoding="utf-8") as fajl:
    for nev in max_parfumok:
        fajl.write(nev + "\n")

print(f"A legnagyobb kiszerelésű 'a' betűs parfüm(ök): {', '.join(max_parfumok)}")

parfum_arak = []
for p in parfumok:
    ar = input(f"Add meg a(z) {p.getMarka()} ({p.getKiszereles()} ml) parfüm árát: ")
    if ar.isdigit():
        parfum_arak.append(int(ar))

if parfum_arak:
    print("A parfümök árának mediánja:", median(parfum_arak))
else:
    print("Nem lehet mediánt számolni, mert nincs megfelelő ár adat.")