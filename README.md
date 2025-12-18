# Komunikacja Człowiek-Komputer :walking: :left_right_arrow: :computer:

*Human-Computer Interaction*


Przedmiot prowadzony jest dla studentów 2-ego roku kierunku kognitywistyka na Uniwersytecie Adama Mickiewicza w Poznaniu. :mortar_board:

### :e-mail: Kontakt do prowadzących

 * zaj. 1-4: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mgr Agnieszka Smolnicka, `agnieszka.smolnicka[at]amu.edu.pl`, dyżur: pon. 14:00-15:00, pok. 110
 * zaj. 5-11: &nbsp;&nbsp;&nbsp; mgr Dawid Ratajczyk, `dawid.ratajczyk[at]amu.edu.pl`,  dyżur: śr. 12:00-13:00, pok. 110
 * zaj. 12-14: &nbsp;dr Aleksandra Wasielewska, `aleksandra.wasielewska[at]amu.edu.pl`, dyżur: czw. 13:30-15:30, pok. LBR
 * wykład: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dr inż. Marcin Jukiewicz (koordynator), `marcin.jukiewicz[at]amu.edu.pl`


### :books: Z czego składa się kurs?

Kurs składa się z czterech części:
 1. Elementy Computer Science
 2. Tworzenie stron internetowych
 3. Analiza biosygnałów
 4. Elementy Human-Robot Interaction


Oceny wystawiane są na podstawie **zadań** wykonywanych w trakcie zajęć lub w domu, **wejściówek** oraz na podstawie **projektu** dotyczącego interfejsów mózg komputer.



 **Uwaga** :office: Zgodnie z regulaminem studiów obowiązują dwie nieobecności, niezależnie od tego, czy są one usprawiedliwione, czy nie. :blue_book:


## Terminarz zajęć
| lp. | Temat | Data (czwartek/piątek) | Zadanie | Liczba punktów |						
| --- |	------- | ----- | ------- | ----------- |					
|1.|	Liczby binarne | 2/3.10.25	|	Praca domowa	|	2	|
|2.|	Bramki logiczne	| 9/10.10.25 |	-	|	-	|
|3.|	HTML	| 16/17.10.25 |	-	|	-	| 
|4.|	CSS	| 23/24.10.25 |	-	|	- |  
|5.|	Analiza sygnałów 1 | 6/7.11.25	|	Arkusz z zajęć	|	2	|
|6.|	Analiza sygnałów 2	| 13/14.11.25 |	Praca domowa	|	2 |
|7.| Analiza sygnałów 3 | 20/21.11.25 | - | - |
|8.|	Wykrywanie mrugnięć	|27/28.11.25 |	-	|	-	|
|9.| Zbieranie danych do projektu	| 4/5.12.25 | -	|	-	|
|10.|	Zbieranie danych do projektu 2	|11/12.12.25 |	-	|	-	|
|11.|	Praca nad projektem	| 18/19.12.25 |	-	| -	|
|12.|	Elementy Human-Robot Interaction	| 8/9.01.26 |	Praca na zajęciach/domowa	|	3	|
|13.|	Elementy Human-Robot Interaction 2	| 15/16.01.26 |	-	|	-	|
|14.| Elementy Human-Robot Interaction 3 | 22/23.01.26 | - | - |
|15.|	Poprawka	| 30.01.26 |	-	|	-	|
|   |   |   | Wejściówki | 9 |
|   |	  |  	| Projekt | 12 |
|  	|	  |  	| **Suma** | **30** |


### Zadania domowe proszę wysyłać na adres mailowy prowadzącego dane zajęcia. Czas na wykonanie to tydzień. 


<hr/>

# 🧠 Projekt HCI: Analiza danych EMG (mrugnięcia, offline)

## Opis projektu
Celem projektu jest zrozumienie, jak sygnały mięśniowe związane z mrugnięciem mogą być wykorzystywane w komunikacji człowiek–komputer lub w analizie reakcji użytkownika na bodźce.  
Dane EMG będą zbierane **offline** (oddzielne logi mrugnięć i bodźców), a analiza zostanie wykonana w środowisku **Python / Jupyter Notebook**.  

Pracujecie w **zespołach 2-osobowych** i wybieracie **jeden z dwóch wariantów projektu**.

---

## 🅰️ Wariant 1 — *Speller offline*

### Cel
Odtworzenie słowa wymruganego przez użytkownika na podstawie dwóch plików:
- `litery_czas.txt` – zapis momentów wyświetlania liter  
- `mrugniecia.txt` – zapis momentów wykrycia mrugnięć  

Należy dopasować momenty mrugnięć do liter i sprawdzić, jakie słowo zostało „wymrugane”.  
Projekt koncentruje się na **analizie danych i dekodowaniu offline** (bez synchronizacji online).

### Co przygotować przed zbieraniem danych
Do zajęć **4–5 grudnia 2025 r.** należy przygotować **program do wyświetlania liter**, który:
- wyświetla kolejne litery alfabetu w pętli (np. co 1 sekundę; z uwzględnionymi przerwami na swobodne mruganie) 
- zapisuje literę i czas jej wyświetlenia do pliku `litery_czas.txt`:
```python
with open("litery_czas.txt", "a") as f:
    f.write(f"{litera},{time.time():.6f}\n")
```

---

## 🅱️ Wariant 2 — *Mruganie w odpowiedzi na różne bodźce*

### Cel
Sprawdzenie, czy ludzie mrugają inaczej w zależności od rodzaju prezentowanych bodźców (np. neutralnych, emocjonalnych, zaskakujących).

Podczas zbierania danych program wyświetla bodźce (obrazy, słowa itp.) i zapisuje:
- `bodzce_czas.txt` – czasy wyświetlenia i kategorię bodźca  
- `mrugniecia.txt` – czasy wykrycia mrugnięć, np.:
  
```python
with open("bodzce_czas.txt", "a") as f:
    f.write(f"{kategoria},{bodziec},{time.time():.6f}\n")
```

Analiza offline polega na porównaniu częstości lub rytmu mrugnięć między kategoriami bodźców.

### Co przygotować przed zbieraniem danych
Do zajęć **4–5 grudnia 2025 r.** należy przygotować **program do wyświetlania bodźców**, który:
- wyświetla serię obrazków, słów lub innych bodźców w różnych kategoriach  
- zapisuje nazwę bodźca, jego kategorię i czas wyświetlenia do pliku `bodzce_czas.txt`

---

## 🧾 Punktacja (maks. 12 pkt)

| Element | Punkty | Opis |
|----------|---------|------|
| Wczytanie i wizualizacja danych | 2 | Poprawne wczytanie i podstawowa eksploracja |
| Analiza główna (dekodowanie / porównanie) | 4 | Kluczowa część projektu |
| Analiza błędów lub porównanie wariantów | 3 | W przypadku błędów: próba poprawy, test alternatyw |
| Refleksja i raport | 3 | Interpretacja wyników i wnioski |

---

## 📅 Terminy

- **4–5 grudnia 2025 r.** – przygotowanie programu (liter lub bodźców) na zajęcia z rejestracją danych  
- **11 stycznia 2026 r.** – termin oddania projektu

---

## 📦 Pliki do przesłania

Wysyłacie w jednej spakowanej paczce (`.zip`):

1. `projekt.ipynb` (Jupyter Notebook) **i** `projekt.pdf` (raport)  
2. Dane:  
   - `litery_czas.txt` **lub** `bodzce_czas.txt` (w zależności od wariantu)  
   - `mrugniecia.txt`  
3. Program użyty do prezentacji:  
   - `wyswietlacz_liter.py` **lub** `bodzce.py`  

---

## 💡 Wskazówki

- Do dopasowania czasów mrugnięć i bodźców można użyć funkcji łączenia danych według najbliższego czasu (np. pd.merge_asof()).  
- Do wizualizacji wyników przydadzą się biblioteki: `matplotlib` lub `seaborn`.  
- Raport powinien krótko opisywać przebieg pracy, zastosowane metody, uzyskane wyniki oraz wnioski (plik pdf).


<hr>

# Kryteria oceny z przedmiotu

| Ocena | L. punktów |
|------------------------|:---------:|
| bardzo dobry (5,0)     | ⩾ 27    |
| dobry plus (4,5)       | 24 - 26,5 |
| dobry (4,0)            |  21 - 23,5  |
| dostateczny plus (3,5) | 19,5 - 20,5 |
| dostateczny (3,0)      | 18 - 19 |
| niedostateczny (2,0)   | < 18   |


### Poradnik uzyskania maksymalnej liczby punktów z zadań 
* Przeczytaj polecenie i wykonaj dokładnie to o co jesteś proszony/a
* Ustrukturyzuj kod i odpowiedzi w zadaniach, aby jasne było co miałeś/aś na myśli
* Pamiętaj o opisywaniu osi wykresów - jaka zmienna jest prezentowana oraz w jakich jednostkach
* Podpisz się na arkuszu 

### Instalacja Jupyter notebook:
W wierszu poleceń:
```
 pip install notebook
```
Aby uruchomić notebook wpisujemy w wierszu poleceń:
```
jupyter notebook
```
lub (bardziej skuteczne, jeśli nie mamy polecenia "jupyter")
```
python -m notebook
```

Środowisko Dziobak: http://150.254.90.119 \
Logowanie za pomocą loginu z USOSa i hasła ustalonego przy pierwszym logowaniu.


