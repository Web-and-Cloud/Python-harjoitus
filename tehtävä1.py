#1.1
#Kirjoita ohjelma, joka asettaa muuttujaan arvon ”Terve maailma” ja tulostaa sen muuttujan.
var = "Terve maailma"
print(var)

1.2
Kirjoita ohjelma, jossa asetetaan kahteen muuttujaan arvoiksi haluamasi luvut. Tulosta niiden muuttujien summa.

a = 2
b = 3

print(a+b)

1.3
Kirjoita ohjelma, jossa lasketaan kolmen muuttujan keskiarvo. Tulosta lopputulos
a = 3
b = 4
c = 3

d = a+b+c
print(d/3)

1.4
Kirjoita ohjelma, jossa muuttujaan asetetaan luku arvo, tulosta muuttuja. Sitten aseta muuttujan arvoksi, jokin toinen luku ja tulosta se.

num = 10

print(num)

num = 20

Muuttujan arvon muuttaminen
2.1
Kirjoita ohjelma, jossa on muuttuja ja se tulostetaan. Sitten muuta muuttujan arvoa niin, että sen arvo kasvaa kaksin kertaiseksi. Tulosta muuttuja.

num1 = 10
print(num1)

num1 = num1 * 2 / num1 *=2

print(num1)


2.2
Kirjoita ohjelma, jossa on kaksi muuttujaa. Kasvata ensimmäistä muuttujaa toisen muuttujan arvolla. Tulosta kasvatettu muuttuja.

num1 = 10
num2 = 20

num1 += num2

print(num1)

2.3
Kirjoita ohjelma, jossa on kaksi muuttujaa, joiden arvoina on itse valitsemasi numerot. Laske ensimmäisen muuttujan arvoa kahdella ja sitten laske ensimmäisen muuttujan arvoa toisen muuttujan arvolla.

num1 = 20
num2 = 10

num1 -= 2

num1 -= num2

print(num1)


2.4
Kirjoita ohjelma, jossa on kaksi muuttujaa, joiden arvoina on itse valitsemasi numerot. Kasvata molempia lukuja niiden summalla. Kokeile esimerkin arvoilla, jolloin sinun tulisi saada esimerkin mukainen lopputulos.
Esimerkki:
muuttuja1 = 5
muuttuja2 = 10
muuttuja1 -> 20
muuttuja2 -> 25

num1 = 20
num2 = 30

sum1 = num1+num2

num1 *=sum1
num2 *=sum1

print("num1 -> " , num1)

print("num2 -> " , num2)

other rule

num1 = 20
num2 = 30

sum1 = num1 + num2

num1 *= sum1
num2 *= sum1

print("num1 -> " + str(num1))
print("num2 -> " + str(num2))


Datatyypin muunnos ja input
3.1
Kirjoita ohjelma, jossa käyttäjä kirjoittaa oman nimensä ja ohjelma tervehtii käyttäjää muodossa:
"Terve Aarni"
user_input = input("Enter your name: ")

print( "Hello " + str(user_input))

result

Enter your name: Arni
Hello Arni
3.2
Kirjoita ohjelma, johon käyttäjä syöttää luvun. Ohjelma tulostaa luvusta kaksin kertaisen arvon.
user_input = input("Enter a number ")

print(int(user_input) * 2)

output
Enter a number 4
8

3.3
Kirjoita ohjelma, joka laskee käyttäjän syöttämän arvon vähennyksen sadasta. Ohjelma tulostaa:
”Sadasta vähennettynä jää xxx”, korvaa xxx vähennyksellä.
user_input = input("Enter a number ")

output = 100 - int(user_input)

print(f"Sadasta vähennettynä jää {output}" )

Enter a number 50
Sadasta vähennettynä jää 50

3.4
Kirjoita ohjelma, joka muuttaa luvun 12.53 kokonaisluvuksi. Tulosta muutettu luku

var = int(12.53)

print(var)

12

Ehtolauseet
4.1
Kirjoita seuraavanlainen ohjelma. Muuttuja faarao on arvoltaan 100. Kirjoita ehto, joka tulostaa ”Faarao on nuori”, jos faaraon arvo on alle tuhat.

faarao = 100

if faarao < 1000:
    print("Faarao on nuori")

4.2
Kirjoita ohjelma, joka kysyy käyttäjän ikää. Täysi-ikäiselle tulostetaan ”Tervetuloa” ja alaikäiselle ”Poistukaa”.
user_input = int(input("Enter your age "))

if user_input >= 18:
    print("Tervetuloa")
else:
    print("Poistukaa")

4.3
Kirjoita ohjelma, joka kysyy pin-koodia. Pin-koodin arvo on 1234. Käyttäjälle tulostetaan, että onko vastaus oikein.

pincode = int(input("Enter your pincode: "))
if pincode == 1234:
    print("Oikein pincode")
    
    output
    Enter your pincode: 1234
Oikein pincode

4.4
Kirjoita ohjelma, johon käyttäjä syöttää iän. Määrittele itse ala- ja ylärajat. Jos ikä on rajojen sisällä, niin ohjelma tulostaa ”Rajojen sisällä”. Jos ikä on liian nuori, niin tulostaa ”Liian nuori” ja jos liian vanha, niin ”Liian vanha”.
lower_age = 18
upper_age = 50
user_age = int(input("Enter your age: "))

if user_age < lower_age:
    print("Liian nuori")
elif user_age > upper_age:
    print("Liian vanha")
else:
    print("Rajojen sisällä")
    
output
Enter your age: 22
Rajojen sisällä


4.5
Kirjoita ohjelma, johon käyttäjä syöttää auton värin ja iän. Jos auto on nuorempi kuin 5 vuotta tai punainen, niin tulosta ”Ostetaan”, muulloin ”Ei osteta”
color = "red"
inputcolor = str(input("Enter color "))

age = 5
inputage = int(input("Enter age "))

if inputcolor == color or inputage > age:
    print("Buying")
else:
    print("Not buying")


