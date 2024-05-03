Funktiot
1.1 Kirjoita ohjelma, jossa funktio, jota kutsuessa ohjelma tulosta ”Terve maailma”. Kutsu funktio.
Hello world
def kissa():
    print("Terve maailma")
kissa()

1.2 Kirjoita ohjelma, jossa on kaksi funktiota. Ensimmäinen funktio kirjoittaa haluamasi lauseen. Toinen funktio kutsuu ensimmäisen funktion. Kutsu toinen funktio.
def func1():
    print("Tevetuola")
def func2():
    func1()
def func3():
    print("Hello world")
    
func2()
func3()

1.3 Kirjoita ohjelma, jossa on funktio, joka tulostaa 100 kertaa ”AUTS!”. Kutsu funktio.
def func1():
    luku = 1
    loppu = 101
    while luku < loppu:
        print("AUTS")
        luku+=1
    
func1()
    
or in other way:
    
def print_auts():
    for _ in range(100):
        print("AUTS!")

print_auts()


Parametrit ja Argumentit
2.1 Kirjoita ohjelma, joka tulostaa parametrinä syötetystä arvosta tuplaten suuremman.
4 -> 8
-5 -> -10

def func1(x):
    m=x*2
    print(m)

func1(8)
func1(10)





2.2 Kirjoita ohjelma, joka tulostaa parametrinä syötetystä arvosta yhden suuremman.
6 -> 7
-2 -> -1

def func1(x):
    m = x+1
    print(m)
func1(8)
func1(-2)

# 2.3 Kirjoita ohjelma, joka tulostaa tervehdyksen. Tervehdykseen tulee laittaa argumentiksi sen henkilön nimi, jota tervehditään. Loppuun huutomerkki.
# Aarni -> ”Terve Aarni!”
# Veeti -> ”Terve Veeti!”
def func1(x):
    print(f"Hello {x}!")

func1("Aarni")
func1("Veeti")

2.4 Kirjoita ohjelma, joka tulostaa ”Hello world”, niin monta kertaa kuin on argumentin arvo.
2 -> Hello world

def func1(x):
    m = x * " Hello world "
    print(m)
    
func1(2)

inother way:

def func1(n):
    for _ in range(n):
        print("Hello world")
func1(2)


    
