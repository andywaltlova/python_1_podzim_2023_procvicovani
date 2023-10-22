# Procviceni - funkce, json, api, list comprehension

Tyto úkoly zahrnují konkrétní URL adresu (https://jsonplaceholder.typicode.com/posts) pro API JSONPlaceholder. **Ukoly na sebe navazuji**, smyslem je stavet znalosti na sebe.

Doporucuji si prohlednout co vraci API a ukoly vypracovavat od 1 po 4, vzdy si postupne zkousejte a overujte ze vas kod funguje (treba pomoci printu) nez se posunete dal.

Procvicena latka:

* Vse se pro trenink zapisuje do samostatnych funkci
  * [Vlastni funkce na kodim](https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/vlastni-funkce/)
* Ziskani dat z API
  * [API na kodim](https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/json/json-api)
* Ulozeni do json souboru
  * [JSON na kodim](https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/json/)
* Filtrace dat s list comprehension
* Tranformace s list comprehension
  * [List comprehension na kodim](https://kodim.cz/programovani/uvod-do-progr-2/bonusy/cykly-2/list-comprehension)

---

### Úkol 1: Získání dat z API

Vytvořte funkci v Pythonu nazvanou `ziskat_api_odpoved(url)`, která má URL jako povinný parametr. Tato funkce provede GET požadavek na tuto URL a vrátí objekt odpovědi. Zavolejte tuto funkci s URL adresou API JSONPlaceholder (https://jsonplaceholder.typicode.com/posts) a vypište status odpovědi k ověření, že požadavek byl úspěšný. Status odpovedi se skryva v atributu `odpoved.status_code`, kde odpoved je promenna ve ktere se skryva navratova hodnota metody `requests.get(url)`.

### Úkol 2: Uložení odpovědi do JSON souboru

Rozšiřte předchozí kód vytvořením funkce nazvané `ulozit_do_json_souboru(nazev_souboru, data)`, která má jako parametry název souboru a data. Uvnitř funkce uložte data do určeného JSON souboru. Můžete parametr `data` predelat i na voliteny s výchozí hodnotou `''`, který umožní uložení prázdného souboru, pokud data nejsou zadána. Použijte tuto funkci k uložení odpovědi z API do souboru s názvem `"posts.json"`.

### Úkol 3: Filtrace dat s využitím list comprehension

Vytvořte funkci nazvanou `filtr_postu_podle_user_id(seznam_postu, user_id='')`, která má seznam postů a user ID jako parametry. Uvnitř funkce použijte list comprehension k filtrování postů tak, aby obsahovaly pouze ty s danými user ID. Pokud user ID není specifikováno (parametr má výchozí hodnotu `''`), funkce by měla vrátit všechny posty. Zavolejte tuto funkci s načtenými daty JSON ze souboru `"posts.json"` z predchoziho cviceni.

### Úkol 4: Transformace dat s využitím list comprehension

Vytvořte funkci nazvanou `ziskat_nazvy_postu(posty: list)`, která má seznam postů jako parametr. Uvnitř funkce použijte list comprehension k vytvoření nového seznamu, který obsahuje pouze názvy postů. Zavolejte tuto funkci s načtenými daty JSON ze souboru `"posts.json"`.
