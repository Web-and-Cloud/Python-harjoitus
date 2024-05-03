# [13:48] Pauli Laine
# Tehtävä 1
# Luo lista numerot, joka sisältää satunnaisia kokonaislukuja väliltä 1-50. Listan pituuden tulee olla 50. Tämän jälkeen, luo toinen lista suodatettu. Käy läpi lista numerot ja lisää listaan suodatettu kaikki parilliset luvut.
# Tehtävä 2
# Luo tyhjä lista merkit. Käytä silmukkaa lisätäksesi siihen merkkijonoja "A", "B", ..., "Z" käyttäen chr()-funktiota. ASCII-koodissa 'A':n koodi on 65 ja 'Z':n koodi on 90.
# Tehtävä 3
# Lataa random-kirjasto ja luo lista satunnaiset, joka sisältää 30 satunnaista liukulukua väliltä 0.0-1.0. Luo sitten lista suuremmat ja lisää siihen kaikki satunnaiset-listan arvot, jotka ovat suurempia kuin 0.5.
# Tehtävä 4
# Luo tyhjä lista alkiot ja täytä se silmukassa arvoilla 1-100. Sen jälkeen, luo lista jaolliset ja lisää siihen kaikki arvot listasta alkiot, jotka ovat jaollisia sekä 3:lla että 5:llä.
# Tehtävä 5
# Lataa random-kirjasto ja luo tyhjä lista arvot. Täytä tämä lista 40 satunnaisella kokonaisluvulla väliltä -30 - 30. Luo lista positiiviset ja lisää siihen kaikki positiiviset arvot listasta arvot.
# Tehtävä 6
# Luo lista kaupungit, joka sisältää joukon eri kaupunkien nimiä. Luo sen jälkeen uusi lista pitkät_kaupungit ja lisää siihen kaikki kaupungit listasta kaupungit, joiden nimessä on enemmän kuin 5 kirjainta.
# Tehtävä 7
# Luo lista numerot sisältäen satunnaisia kokonaislukuja väliltä 100-999. Listan pituus olkoon 100. Luo uusi lista uniikit ja käy läpi lista numerot, lisäten listaan uniikit vain ne arvot, jotka ovat uniikkeja (esiintyvät listassa vain kerran).
# Tehtävä 8
# Lataa random-kirjasto ja luo lista pisteet, joka sisältää 50 satunnaista kokonaislukua väliltä 0-100, jotka kuvaavat opiskelijoiden pisteitä kokeesta. Luo uusi lista hyväksytyt ja lisää siihen kaikki arvot listasta pisteet, jotka ovat suurempia tai yhtä suuria kuin 50.
# Tehtävä 9
# Luo tyhjä lista kirjaimet ja käytä silmukkaa lisätäksesi siihen kaikki englannin kielen pienet kirjaimet käyttäen chr()-funktiota ja ASCII-koodiarvoja. Luo sitten lista vokaalit ja lisää siihen kaikki vokaalit listasta kirjaimet.
# Tehtävä 10
# Lataa random-kirjasto ja luo lista lukuja, joka sisältää satunnaisia kokonaislukuja väliltä 1-10. Listan pituus olkoon 100. Luo uusi lista toistot ja laske, kuinka monta kertaa kukin luku esiintyy listassa lukuja. Tulosta sitten jokaisen luvun esiintymiskerrat.
# [13:48] Pauli Laine
# Task 1
# Create a list of numbers that contains random integers between 1-50. The length of the list should be 50. After this, create another list filtered. Go through the list of numbers and add filtered all even numbers to the list.

import random
 
random_numbers = []
count = 0
while count < 50:
    random_numbers.append(random.randint(1, 50))
    count = count + 1

filtered_list = []

for i in random_numbers:
    if i % 2 == 0:
        filtered_list.append(i)

print("Random Numbers: ", random_numbers)

print("Filtered Number: ", filtered_list)

# Task 2
# Create an empty list of characters. Use a loop to add the strings "A", "B", ..., "Z" to it using the chr() function. In ASCII code, the code of 'A' is 65 and the code of 'Z' is 90.

# Create an empty list to store characters
# character_list = []
# 
# 
# for i in range(65, 90 + 1):
#     character_list.append(chr(i))
# 
# 
# print(character_list)

# Create an empty list to store characters
character_list = []


ascii_code = 65

while ascii_code <= 90:
    character_list.append(chr(ascii_code))
    ascii_code += 1


print(character_list)


# 

# Task 3
# Download the random library and create a random list containing 30 random floating-point numbers between 0.0 and 1.0. Then create a list bigger and add all random list values greater than 0.5 to it.

random_list = []
count = 0
while count < 30:
    random_list.append(round(random.uniform(0.0, 1.0),1))
    count = count + 1

bigger_list = []

for i in random_list:
    if i > 0.5:
        bigger_list.append(i)

print("Random List: ", random_list)

print("Bigger List: ", bigger_list)




# Task 4
# Create an empty list of elements and fill it in a loop with values 1-100. After that, create a list divisible and add to it all values from the list elements that are divisible by both 3 and 5.

empty_list = []

count = 1

while count <= 100:
    empty_list.append(count)
    count = count + 1
    
divisible_list = []

for i in empty_list:
    if i % 3 == 0 and i % 5 == 0:
        divisible_list.append(i)
    
print("Empty list: ", empty_list)

print("Divisible list: ", divisible_list)





# Task 5
# Load the random library and create an empty list of values. Fill this list with 40 random integers between -30 and 30. Create a list positive and add all positive values from the list values to it.

list_values = []

count = 0

while count <= 50:
    list_values.append(random.randint(-30, 30))
    count = count + 1
    
positive_list = []

for i in list_values:
    if i >= 0:
        positive_list.append(i)
        
print("List values ", list_values)
print("Positive Values ", positive_list)



# Task 6
# Create a list cities that contains a number of different city names. After that, create a new list long_towns and add to it all the cities from the list cities whose name has more than 5 letters.
city_name = ["Dhaka", "Rajshahi", "Khulna", "Chittagang", "Rangpur", "Barishal", "Shylhet"]

long_towns = []

for i in city_name:
    if len(i) > 5:
        long_towns.append(i)
        
print(long_towns)


# Task 7
# Create a list of numbers including random integers between 100-999. Let the length of the list be 100. Create a new list uniques and go through the list numbers, adding only those values that are unique (occurring in the list only once) to the list uniques.

integer_list = []

count = 1

while count <= 100:
    integer_list.append(random.randint(100, 999))
    count = count + 1
    



unique_list = []

for i in integer_list:
    if integer_list.count(i) == 1:
        unique_list.append(i)




print("Integer list: ", integer_list)
print("Unique list: ", unique_list)


# Task 8
# Download the random library and create a list scores, which contains 50 random integers between 0-100, which describe students'
#scores from the exam. Create a new list accepted and add to it all values from the list with scores greater than or equal to 50.

score_list = []

count = 0

while count < 50:
    score_list.append(random.randint(0, 100))
    count = count + 1

new_list = []
for i in score_list:
    if i >= 50:
        new_list.append(i)
        
print("Score list: ", score_list)
print("New_list: ", new_list)



# Task 9
# Create an empty list letters and use a loop to add all English lowercase letters to it using the chr() function and the ASCII code
#values. Then create a list of vowels and add all the vowels from the list to the letters.


character_list1 = []


ascii_code = 97

while ascii_code <= 122:
    character_list1.append(chr(ascii_code))
    ascii_code += 1

vowels = ["a","e","i","o","u"]
vowel_list= []
for i in character_list1:
    if i in vowels:
        vowel_list.append(i)

print("a to z: ", character_list1)
print("Vowels: ", vowel_list)



# Task 10
# Download the random library and create a list of numbers that contains random integers between 1-10. Let the length of the list be 100.
#Create a new list repetitions and count how many times each number appears in the list of numbers. Then print the occurrences of each number.

num_list = []

count = 0

while count >100:
    num_list.append(random.randint(1, 10))
    count = count + 1
    
repet_list = []

for i in num_list:
    





















