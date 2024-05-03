Python: Satunnaisluku Tehtävä
Aarni Junkkala
Satunnaisluku
1.1 Kirjoita ohjelma, joka tulostaa satunnaisluvun väliltä 0.0 ja 10.0.
import random

satunnaisluku = random.random() * 10.0

print(satunnaisluku)


1.2 Kirjoita ohjelma, joka tulostaa satunnaisluvun väliltä -1.0 ja 1.0.
import random

luku = random.uniform(-1.0 ,1.0)

print(luku)



1.3 Kirjoita ohjelma, joka tulostaa koodaus taitosi prosenttina. Luo prosentin arvo satunnaisluvulla väliltä 0.0 ja 100.0
-> Taitosi on 66.6462466246%
import random

def skill():
    skill_per = random.uniform(0.0,100.0)
    return skill_per

random_skill = skill()
print(f"Your skill is {random_skill}%")

1.4 Kirjoita ohjelma, jossa käyttäjä arvaa joko nolla tai yksi. Luo oikea vastaus satunnaisluvulla väliltä 0.0 ja 1.0, ja tulosta ”voitit”, jos satunnaisluku on lähempänä arvattua kuin toista vaihto ehtoa. Muulloin tulosta ”Hävisit!”.
import random

def guess_game():
 user_input = int(input("Enter 0 or 1: "))
 random_number = random.uniform(0.0, 1.0)

 if abs(user_input - random_number) < 0.5:
    print("You won!")
 else:
    print("You lost!")

guess_game()
Satunnaiset kokonaisluvut
2.1 Kirjoita ohjelma, tulostaa satunnaisluvut väliltä 1-100.
import random

def satunnaisluku(num):
    for _ in range(num):
        random_number = random.randint(1,100)
        print(random_number)
        
satunnaisluku(5)

2.2 Kirjoita ohjelma, joka simuloi noppaa. Jos ohjelma saa silmäluvun kuusi, niin ohjelma tulostaa ”Voitit”, muulloin ”Hävisit”
import random

def play_dice_game():
    result = random.randint(1, 6)
    if result == 6:
        print("You won!")
    else:
        print("You lost.")

# Play the dice game
play_dice_game()


2.3 Kirjoita ohjelma, joka aloittaa laskemisen numerosta yksi. Ohjelma kasvattaa numero satunnaisluvulla väliltä 1-6. Lopuksi ohjelma tulostaa, että kuinka monta kertaa lukua kasvatettiin, ennen kuin se saavutti arvon 100.
import random

def count_number():
    current_number = 1
    step = random.randint(1, 6)
    for _ in range(101):
        current_number += step

        if current_number >= 100:
            print(f"Lukua kasvatettiin {_ + 1} kertaa ennen kuin se saavutti arvon 100.")
            break

count_number()

in other way

import random

def count_number():
    number_of_steps = 0  # Muuttuja pitää kirjaa kasvatuskertojen määrästä
    current_number = 1   # Alustetaan laskuri arvoon 1
    
    while current_number < 100:
        step = random.randint(1, 6)
        current_number += step
        number_of_steps += 1
    
    print(f"Lukua kasvatettiin {number_of_steps} kertaa ennen kuin se saavutti arvon 100.")

count_number()


2.4 Kirjoita ohjelma, jossa luku on nolla. Lukua kasvatetaan ja vähennetään vuorotellen satunnaisluvulla väliltä 1-6. Jos luku on -10 tai vähemmän, tulosta ”Pelaaja 1 voitti”, jos luku on 10 tai enemmän, tulosta ”Pelaaja 2 voitti”.
import random

def play_game():
    number = 0
    
    while True:
        step = random.randint(1,6)
        number += step
    
        if number <= -10:
            print("Player 1 won")
            break
        elif number >= 10:
            print("Player 2 won")
            break
    
play_game()
        
        
        
        
        
Listat
3.1 Kirjoita ohjelma, jossa tulostetaan sattumanvaraisesti listasta valittu alkio.
import random

x= ['cat','dog','snake','rat'] 
a = random.choice(x)

print(a)


3.2 Kirjoita ohjelma, jossa listasta poistetaan sattumanvaraisesti valittuja alkioita, kunnes jäljellä on vain yksi alkio. Tulosta jäljelle jäänyt alkio.

import random

x= ['cat','dog','snake','rat'] 
a = random.choice(x)
x.remove(a)

print(x)