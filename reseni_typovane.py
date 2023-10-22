import json
import requests

"""
Úkol 1: Získání dat z API
Vytvořte funkci v Pythonu nazvanou ziskat_api_odpoved(url),
která má URL jako povinný parametr. Tato funkce provede GET požadavek na tuto URL a vrátí objekt odpovědi.
Zavolejte tuto funkci s URL adresou API JSONPlaceholder (https://jsonplaceholder.typicode.com/posts) a
vypište status odpovědi k ověření, že požadavek byl úspěšný.
Status odpovedi se skryva v atributu odpoved.status_code, kde odpoved je promenna ve ktere se skryva
navratova hodnota metody requests.get(url).

Analogicky udelej podobnou funkci ziskat_api_data(url), ktera nebude vracet status,
ale data nachazejici se na dane url adrese.
"""

# Vraci status
# Pokud te to zajima vic co status znamena, tak se mrkni na https://http.cat/ nebo https://http.dog/
#   200 je OK
#   404 muzes obcas videt jako Not Found
#   cokoli co je 5xx je chyba na strane serveru
def ziskat_api_odpoved(url:str) -> int:
    odpoved = requests.get(url)
    status = odpoved.status_code
    return status

# Vraci json data
def ziskat_api_data(url:str) -> list:
    odpoved = requests.get(url)
    data = odpoved.json()
    return data

"""
Úkol 2: Uložení odpovědi do JSON souboru
Rozšiřte předchozí kód vytvořením funkce nazvané ulozit_do_json_souboru(nazev_souboru, data),
která má jako parametry název souboru a data. Uvnitř funkce uložte data do určeného JSON souboru.

Použijte tuto funkci k uložení odpovědi z API do souboru s názvem "posts.json".
"""

def ulozit_do_json_souboru(nazev_souboru:str, data:list) -> None: #zadny return nemame
    with open(nazev_souboru, 'w', encoding='utf-8') as soubor:
        json.dump(data, soubor, ensure_ascii=False, indent=2)

"""
Úkol 3: Transformace dat s využitím list comprehension
Vytvořte funkci nazvanou ziskat_nazvy_postu(posty: list),která má seznam postů jako parametr.
Uvnitř funkce použijte list comprehension k vytvoření nového seznamu,
který obsahuje pouze názvy postů. Zavolejte tuto funkci s načtenými daty
JSON ze souboru "posts.json".
"""

def ziskat_nazvy_postu(posty: list) -> list:
    vysledek = [post['title'] for post in posty]
    return vysledek

"""
Úkol 4: Filtrace dat s využitím list comprehension
Vytvořte funkci nazvanou filtr_postu_podle_user_id(seznam_postu, user_id=''),
která má seznam postů a user ID jako parametry. Uvnitř funkce použijte list
comprehension k filtrování postů tak, aby obsahovaly pouze ty s danými user ID.
Pokud user ID není specifikováno (parametr má výchozí hodnotu ''), funkce by měla vrátit všechny posty.
Zavolejte tuto funkci s načtenými daty JSON ze souboru "posts.json" z predchoziho cviceni.
"""

# BONUS: Tady je typovani trochu slozite protoze default je string ale user_id je jinak cislo
# v praxi pokud je vic moznosti, pouzila bych Union typ z modulu typing
from typing import Union
# vzdy je ale lepsi delat funkce tak aby pocitali s jednim typem

def filtr_postu_podle_user_id(seznam_postu: list, user_id: Union[str, int]='') -> list:
    if user_id == '':
        return seznam_postu # vratime vsechny puvodni

    vysledek = [post for post in seznam_postu if post['userId'] == user_id]
    # vysledek = []
    # for post in seznam_postu:
    #     if user_id == post['userId']:
    #         vysledek.append(post)
    return vysledek


################################################################################
# KOD - volani funkci definovanych nahore
################################################################################

# Ulozeni dat do souboru
url = 'https://jsonplaceholder.typicode.com/posts'
data = ziskat_api_data(url)
ulozit_do_json_souboru('posts.json', data)

# Otevreni souboru - stazeni nahore uz muzes klidne dat do komentare (pokud mas soubor vytvoreny)
with open('posts.json', 'r', encoding='utf-8') as soubor:
    data = json.load(soubor)


# nazvy postu
print(ziskat_nazvy_postu(data))

# filtrovani podle userId
vysledek = filtr_postu_podle_user_id(data, 132)
print(len(vysledek))

