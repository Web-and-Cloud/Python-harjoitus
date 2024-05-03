Python-toistolauseet: Tehtävät
Aarni Junkkala
Kirjoita kaikkiin tiedostoihin kommenttina tehtävänanto. Palauta kaikki tiedostot nimillä Toistolauseet_Tehtävänumero_Omanimi.py. Pakkaa kaikki tiedostot zip-tiedostoiksi.
For-toistolause
1.1 Kirjoita for-toistolause, joka kirjoittaa luvut nollasta kahteenkymmeneen.
for i in range(1,21):
    print(i)

1.2 Kirjoita for-toistolause, joka kirjoittaa numerot kymmenestä kahteenkymmeneen.
for i in range(10,21):
    print(i)

1.3 Kirjoita for-toistolause, joka kirjoittaa numerot sadasta nollaan. (100, 99, 98, jne.)
for i in range(100,-1,-1):
    print(i)

1.4 Kirjoita for-toistolause, joka kirjoittaa viiden kertotaulun luvut kymmenen toistoon asti (5,10,15……90,95,100)
for i in range(5,101,5):
    print(i)

1.5 Kirjoita for-toistolause, joka kirjoittaa joka toisen numeron yhdestä yhdeksään. (1,3,5,7,9)
for i in range(1,11,2):
    print(i)


While-toistolause
2.1 Kirjoita while-toistolause, joka tulostaa luvut nollasta kahteenkymmeneen
luku = 0
loppu = 21
while luku < loppu:
    print(luku)
    luku += 1

2.2 Kirjoita while-toistolause, jossa laskuri aloittaa laskemisen luvusta yksi ja tuplaantuu joka toistolla, kunnes laskuri ylittää sadan. Tulosta luku jokaisella toistolla. (1,2,4,8,16,32,64,128)
luku = 1
loppu = 130
while luku < loppu:
    print(luku)
    luku *= 2

2.3 Kirjoita ohjelma, jossa on muuttujat Bensa ja Moottoriöljy, anna niille arvot 50
#ja 5. Kirjoita while-toistolause, joka toistuu niin kauan, kun bensaa ja moottoriöljyä
#on jäljellä. Jokaisella toistolla kasvatetaan muuttujaa kilometrit yhdellä ja vähennetää
#bensaa 0.5:llä ja moottoriöljyä 0.05:llä. Lopuksi tulosta ajetut kilometrit seuraavan
#laisesti: ”Ajettu xxx kilometriä”.
 # Asetetaan alkuarvot
Bensa = 50
Moottoriöljy = 5
kilometrit = 0

# Toistolause, joka toistuu niin kauan kun bensaa ja moottoriöljyä on jäljellä
while Bensa > 0 and Moottoriöljy > 0:
    kilometrit += 1
    Bensa -= 0.5
    Moottoriöljy -= 0.05

# Tulostetaan ajetut kilometrit
print(f"Ajettu {kilometrit} kilometriä.")
Listat
3.1 Kirjoita toistolause, joka kirjoittaa listassa olevien hedelmien nimiä yksi kerrallaan. Kirjoita listaan ainakin viisi hedelmää.
hedelmia = ["apple", "banana", "orange", "pineapple", "lichi"]

for hedelma in hedelmia:
    print(hedelma)

3.2 Kirjoita toistolause, joka toistaa 10 kierrosta. Lisää tyhjään listaan jokaista kierrosta vastaava numero. Lopuksi tulosta koko lista.
lists = []

for i in range(1, 11):
    lists.append(i)
    
print(lists)

in other way
Initialize an empty list
number_list = []

# Repeat 10 cycles
for i in range(1, 11):
    number_list.append(i)

# Print the entire list
print(number_list)
    


3.2 Kirjoita toistolause, joka kirjoittaa listassa olevien lemmikkien nimiä. Nimet tulee kirjoittaa päin vastaisessa järjestyksessä, eli viimeinen nimi ensimmäisenä. Nimi listassa tulee olla ainakin neljä nimeä.
Huom. Pythonissa on valmiina funktio reverse() ja sen käyttö on tässä tehtävässä kielletty.
pets = ["cat","dog","bird","rabbit"]

for i in range(len(pets)-1,-1,-1):
    print(pets[i])


3.3 Kirjoita toistolause, joka käy läpi listaa, jossa on ihmisten ikiä. Listassa tulee olla ainakin kuusi numeroa väliltä 0-100. Jos luku on pienempi kuin 18, niin tulosta ”alaikäinen”, jos toisin niin tulosta ”täysi-ikäinen”.
ages = [22, 14, 35, 8, 45, 19, 65, 10]

for age in ages:
    if age < 18:
        print("minor")
    else:
        print("adult")

