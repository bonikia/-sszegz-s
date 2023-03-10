#szoveg="aranyalma"
#for betu in szoveg:
#print(betu)

#elöltesztelő ciklus
import telnetlib
from this import s
import random

oldjelszo="majom"
jelszo=input("Kérem a jelszot")

while oldjelszo != jelszo:
    jelszo=input("Rossz jelszo! Kérem a jelszot")
print("Sikeres belépés")

#végtelen ciklus megszakítása: ctrl+c

#hátultesztelo ciklus
#while True:
#utasitas
#if feltétel
#break

while True:
    jelszo=input("Kérem a jelszót:")
    if jelszo == oldjelszo:
        break
print("Sikeres belépés")

megfelelo=False
while not megfelelo:
    jelszo =input("Kérem a jelszot:")
    if jelszo == oldjelszo:
        megfelelo = True

#utolso ketto ugyanaz


#eloltesztelo
gondoltSZam=random.random(1,1000)
tipp = int(input("Kérem a tippet:"))
tippekSzama = 1
while tipp != gondoltSZam:
    if tipp<gondoltSZam:
        print("nagyobb számra gondoltam")
    else:
        print("kisebb számra gondoltam")
    tipp = int(input("Kérem a tippet:"))
    tippekSzama +=1
print(f"Gratu,eltalálta! Tppek száma: {tippekSzama}")


#hatultesztelo
gondoltSzam=random.randint(1,1000)
tippekSzama = 0
while True:
    tippekSzama +=1
    tipp=int(input("Kérem a tippet"))
    if tipp == gondoltSzam:
        break
print(f"Gratu,eltalálta! Tippek száma: {tippekSzama}")