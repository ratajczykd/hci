# Komunikacja Człowiek-Komputer :walking: :left_right_arrow: :computer:

*Human-Computer Interaction*


Przedmiot prowadzony jest dla studentów 2-ego roku kierunku kognitywistyka na Uniwersytecie Adama Mickiewicza w Poznaniu. :mortar_board:

### :e-mail: Kontakt do prowadzących

 * zaj. 1-5: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; mgr Agnieszka Smolnicka, `agnieszka.smolnicka[at]amu.edu.pl`, dyżur: wt. 15:15-16:15, pok. 110
 * zaj. 6-8: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dr Aleksandra Wasielewska, `aleksandra.wasielewska[at]amu.edu.pl`, dyżur: czw. 12:00-14:00, pok. LBR
 * zaj. 9-15: &nbsp;&nbsp;&nbsp; dr Dawid Ratajczyk, `dawid.ratajczyk[at]amu.edu.pl`,  dyżur: n.d., pok. LBR
 * wykład: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dr inż. Marcin Jukiewicz (koordynator), `marcin.jukiewicz[at]amu.edu.pl`


### :books: Z czego składa się kurs?

Kurs składa się z czterech części:
 1. Elementy Computer Science
 2. Tworzenie stron internetowych
 3. Elementy Human-Robot Interaction
 4. Analiza biosygnałów


Oceny wystawiane są na podstawie **zadań** wykonywanych w trakcie zajęć lub w domu, **wejściówek** oraz na podstawie **projektu** dotyczącego interfejsów mózg komputer.



 **Uwaga** :office: Zgodnie z regulaminem studiów obowiązują dwie nieobecności, niezależnie od tego, czy są one usprawiedliwione, czy nie. :blue_book:


## Terminarz zajęć
| lp. | Temat | Data (czwartek/piątek) | Zadanie | Liczba punktów |						
| --- |	------- | ----- | ------- | ----------- |					
|1.|	Liczby binarne | 2/5.10.26	|	Praca domowa	|	2	|
|2.|	Bramki logiczne	| 9/13.10.26 |	-	|	-	|
|3.|	HTML	| 16/20.10.26 |	-	|	-	| 
|4.|	CSS	| 23/27.10.26 |	-	|	- |  
|5.| Markdown | 30.10/3.11.26 | Praca na zajęciach/domowa | 2 |
|6.|	Elementy Human-Robot Interaction	| 6/10.11.26 |	Praca na zajęciach/domowa	|	3	|
|7.|	Elementy Human-Robot Interaction 2	| 13/17.11.26 |	-	|	-	|
|8.| Elementy Human-Robot Interaction 3 | 20/24.11.26 | - | - |
|9.|	Analiza sygnałów 1 | 27.11/1.12.26	|	- |	-	|
|10.|	Analiza sygnałów 2	| 4/8.12.26 |	Praca na zajęciach/domowa	|	2 |
|11.| Analiza sygnałów 3 | 11/15.12.26 | - | - |
|12.|	Wykrywanie mrugnięć	|18/22.12.26 |	-	|	-	|
|13.| Zbieranie danych do projektu	| 8/12.01.27 | -	|	-	|
|14.|	Praca nad projektem	| 15/19.01.27 |	-	| -	|
|15.|	Poprawka	| 22/26.01.27 |	-	|	-	|
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


