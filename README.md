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

### Terminarz zajęć
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
|13.|	Elementy Human-Robot Interaction	| 16/17.01.25 |	Praca na zajęciach/domowa	|	4	|
|14.|	Elementy Human-Robot Interaction 2	| 23/24.01.25 |	-	|	-	|
|15.|	Poprawka	| 30/31.01.25 |	-	|	-	|
|   |   |   | Wejściówki | 6 |
|   |	  |  	| Projekt | 12 |
|  	|	  |  	| **Suma** | **30** |


### Zadania domowe proszę wysyłać na adres mailowy prowadzącego dane zajęcia. Czas na wykonanie to tydzień. 



### Projekt
Zadaniem projektu jest stworzenie prostego interfejsu offline typu "speller" opartego na mruganiu. Projekt realizuje się w grupach 2-osobowych. 

W ramach projektu wymagane jest:
(1) przygotowanie programu wyswietlającego litery alfabetu, \
(2) zebranie danych osoby, która przy pomocy mrugania sygnalizuje wybór danej litery (powinna zapisać w ten sposób jakiegoś słowo), \
(3) przygotowanie kodu, który odszyfrowuje wybrane litery, oraz \
(4) przygotowanie raportu z projektu. 

Na zajęciach nr 10 i 11 będą Państwo zbierać dane do projektu. Do tego czasu proszę przygotować program wyświetlający litery alfabetu w pętli (warty 2pkt w projekcie). Proszę przesłać program w terminie 3 dni przed datą zbierania danych (8.12, 12.12 lub 15.12). W najprostszej formie mogą to być litery wyświetlane w wierszu poleceń lub w jupyterze (max 1pkt), w bardziej rozbudowanej formie wyświetlanie inferfejsu graficznego (przy pomocy np. tkintera, pygame'a albo psychopy'a). Program (nazwijmy go Wyświetlaczem Liter) powinien wyświetlać kolejno wszystkie litery alfabetu przez wybrany odcinek czasu (np. każda litera przed jedną sekundę). Po skończeniu alfabetu powinien zaczynać od nowa. Muszą Państwo wiedzieć w którym momencie były wyświetlane konkretne litery (np. że litera "F" pojawiała się między 6 a 7 sekundą). Informacja ta będzie potrzebna do odkodowania liter wybranych przez mrugnięcia.

Po zebraniu danych należy przygotować kod (w arkuszu jupyter notebook) który wykrywa mrugnięcia i odszyfrowuje jakie litery zostały "wymrugane" przez osobę oraz raport z projektu zawierający opis zadania, wybrane metody, opis analizy i uzyskanych wyników, opis błędów które się pojawiły i możliwych ulepszeń. Deadline to **13. stycznia**.



### Punktacja projektu
* Interfejs graficzny -- 2pkt
* Kod do wykrywania mrugnięć -- 2pkt
* Synchronizacja zadań -- 1pkt
* Poprawność analizy i wyników -- 3pkt
* Formalna strona raportu -- 2pkt

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




