# Komunikacja Człowiek-Komputer :walking: :left_right_arrow: :computer:

*Human-Computer Interaction*


Przedmiot prowadzony jest dla studentów 2-ego roku kierunku kognitywistyka na Uniwersytecie Adama Mickiewicza w Poznaniu. :mortar_board:

### :e-mail: Kontakt do prowadzących

 * mgr Agnieszka Smolnicka, agnieszka.smolnicka[at]amu.edu.pl
 * mgr Dawid Ratajczyk, dawid.ratajczyk[at]amu.edu.pl,  dyżur: środa 13:30-14:30, pokój 110
 * mgr Aleksandra Wasielewska, aleksandra.wasielewska[at]amu.edu.pl 
 * dr inż. Marcin Jukiewicz (koordynator), marcin.jukiewicz[at]amu.edu.pl


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
|1.|	Liczby binarne | 3/4.10.24	|	-	|		|
|2.|	Bramki logiczne	| 10/11.10.24 |	Praca domowa	|	2	|
|3.|	HTML	| 17/18.10.24 |	-	|	-	| 
|4.|	CSS	| 24/25.10.24 |	-	|	- |  
|5.|	Analiza sygnałów 1 | 7/8.11.24	|	Arkusz z zajęć	|	2	|
|6.|	Analiza sygnałów 2	| 14/15.11.24 |	Praca domowa	|	2 |
|7.| Wykrywanie sygnału EEG | 21/22.11.24 | - | - |
|8.|	Potencjały wywołane	|28/29.11.24 |	Arkusz z zajęć	|	2	|
|9.| Wykrywanie mrugnięć	| 5/6.12.24 | 	|	-	|
|10.|	Zbieranie danych do projektu	|12/13.12.24 |	-	|	-	|
|11.|	Zbieranie danych do projektu 2	| 19/20.12.24 |	-	| -	|
|12.|	VR	| 9/10.01.25 |	-	| -	|
|13.|	Elementy Human-Robot Interaction	| 16/17.01.25 |	Praca na zajęciach/domowa	|	3	|
|14.|	Elementy Human-Robot Interaction 2	| 23/24.01.25 |	-	|	-	|
|15.|	Poprawka	| 30/31.01.25 |	-	|	-	|
|   |   |   | Wejściówki | 7 |
|   |	  |  	| Projekt | 12 |
|  	|	  |  	| **Suma** | **30** |


### Zadania domowe proszę wysyłać na adres mailowy prowadzącego dane zajęcia. Czas na wykonanie to tydzień. 


<hr/>

## Projekt
Zadaniem projektu jest stworzenie prostego interfejsu offline typu "speller" opartego na mruganiu, realizowanego w grupach 2-osobowych.

Wymagania projektu:
1. Przygotowanie programu wyświetlającego litery alfabetu.
2. Zbieranie danych osoby, która przy pomocy mrugania sygnalizuje wybór danej litery (osoba powinna zapisać w ten sposób jakieś słowo). Kod do zbierania danych dostarcza prowadzący.
3. Przygotowanie kodu, który odszyfrowuje wybrane litery na podstawie zebranych danych z mrugnięć (detekcja skurczów mięśni czoła przy użyciu elektrody).
4. Przygotowanie raportu z projektu zawierającego typowe elementy raportu: opis zadania, wybrane metody, opis analizy i uzyskanych wyników, opis błędów, które się pojawiły, oraz możliwych ulepszeń.

### Szczegóły dotyczące projektu:
Na zajęciach nr 10 i 11 będą Państwo zbierać dane do projektu. Do tego czasu proszę przygotować program wyświetlający litery alfabetu w pętli (warty 2 punkty). Program należy przesłać na 4 dni przed datą zbierania danych.

W najprostszej formie litery mogą być wyświetlane w wierszu poleceń lub w Jupyterze (max 1 pkt), a w bardziej rozbudowanej formie można zastosować interfejs graficzny przy użyciu np. Tkintera, Pygame'a albo Psychopy (max 2 pkt). Program (Wyświetlacz Liter) powinien wyświetlać kolejno wszystkie litery alfabetu przez określony czas (np. każda litera przez 1 sekundę) i po zakończeniu alfabetu rozpoczynać od nowa. Pętla musi działać do momentu ręcznego wyłączenia programu. 

Kluczowe wymaganie: Program musi rejestrować momenty, w których były wyświetlane konkretne litery (np. że litera "F" była wyświetlana między 6 a 7 sekundą), ponieważ informacje te będą potrzebne do zsynchronizowania z czasami wykrycia mrugnięć w trybie offline. W programie musi znaleźć się linijka kodu, która zapisuje literę oraz jej czas wyświetlenia do pliku litery_czas.txt w następujący sposób:

```litera = 'A'
with open("litery_czas.txt", "a") as myfile:
    myfile.write(litera + ', ' + str(time.time()) + '\n')
```

Po zebraniu danych należy przygotować kod (w arkuszu Jupyter Notebook), który wykrywa mrugnięcia i odszyfrowuje, jakie litery zostały "wymrugane" przez osobę. Ważne jest, aby kod działał poprawnie, natomiast nie ma wymogu poprawnego zdekodowania całego słowa.

Deadline: **12 stycznia**

### Punktacja projektu
* Interfejs graficzny -- 2pkt
* Kod do wykrywania mrugnięć -- 2pkt
* Synchronizacja zadań -- 1pkt
* Poprawność analizy i wyników -- 4pkt
* Raport -- 3pkt

### Kryteria oceny z przedmiotu

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
W konsoli:
```
 pip install jupyterlab
 pip install notebook
```
Aby uruchomić notebook wpisujemy w konsoli:
```
jupyter notebook
```




