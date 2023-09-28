# Komunikacja Człowiek-Komputer :walking: :left_right_arrow: :computer:

*Human-Computer Interaction*


Przedmiot prowadzony jest dla studentów 2-ego roku kierunku kognitywistyka na Uniwersytecie Adama Mickiewicza w Poznaniu. :mortar_board:

### :e-mail: Kontakt do prowadzących

 * dr inż. Marcin Jukiewicz (koordynator), marcin.jukiewicz[at]amu.edu.pl
 * mgr Aleksandra Wasielewska, aleksandra.wasielewska@amu.edu.pl
 * mgr Dawid Ratajczyk, dawid.ratajczyk[at]amu.edu.pl,  dyżur: piątek 11:30-12:30, pokój 110


### :books: Z czego składa się kurs?

Kurs składa się z czterech części:
 1. Analiza biosygnałów
 2. Tworzenie stron internetowych
 3. Elementy Computer Science
 4. Elementy Human-Robot Interaction


Oceny wystawiane są na podstawie **zadań** wykonywanych w trakcie zajęć lub w domu oraz na podstawie **projektu** dotyczącego interfejsów mózg komputer.




 **Uwaga** :office: Zgodnie z regulaminem studiów obowiązują dwie nieobecności, niezależnie od tego, czy są one usprawiedliwione, czy nie. :blue_book:

### Terminarz zajęć
| lp. | Temat | Data | Zadanie | Liczba punktów |						
| --- |	------- | ----- | ------- | ----------- |					
|1.|	Jupyter notebook i przypomnienie pythona | 6/11.10.22	|	-	|	-	|
|2.|	Numpy i Matplotlib	| 13/18.10.22 |	Praca domowa	|	3	|
|3.|	Analiza sygnałów 1	| 20/25.10.22 |	Arkusz z zajęć	|	2	|
|4.|	Analiza sygnałów 2	| 27.10/8.11.22 |	Praca domowa	|	2	|
|5.|	Wykrywanie sygnału EEG | 3/15.11.22	|	Arkusz z zajęć	|	2	|
|6.|	Potencjały wywołane	| 17/22.11.22 |	Arkusz z zajęć	|	2	|
|7.| Wykrywanie mrugnięć | 24/29.11.22 | - | - |
|8.|	Zbieranie danych do projektu	| 1/6.12.22 |	-	|	-	|
|9.|	HTML 	| 8/13.12.22 |	-	|	-	|
|10.|	CSS	| 22/20.12.22 |	Praca domowa	|	3	|
|11.|	Liczby binarne	| 5/10.01.23 |	Praca domowa	|	2	|
|12.|	Bramki logiczne	| 12/17.01.23 |	Praca domowa	|	2	|
|13.|	VR	| 19/24.01.23 |	Praca domowa	|	2	|
|14.|	Dodatkowe	| 26/31.01.23 |	-	|	-	|
|   |	  |  	| Projekt | 10 |
|  	|	  |  	| **Suma** | **30** |


### Zadania domowe proszę wysyłać na adres mailowy *dawid.ratajczyk@amu.edu.pl*. Czas na wykonanie to tydzień. 



### Projekt
Zadaniem projektu jest stworzenie prostego interfejsu offline typu "speller" opartego na mruganiu. Projekt realizuje się w grupach 2-osobowych. 

W ramach projektu wymagane jest:
(1) przygotowanie programu wyswietlającego litery alfabetu, \
(2) zebranie danych osoby, która przy pomocy mrugania sygnalizuje wybór danej litery (powinna zapisać w ten sposób jakiegoś słowo), \
(3) przygotowanie kodu, który odszyfrowuje wybrane litery, oraz \
(4) przygotowanie raportu z projektu. 

Na zajęciach nr 8 (1/6 grudnia) będą Państwo zbierać dane do projektu. Do tego czasu proszę przygotować program wyświetlający litery alfabetu w pętli (warty 2pkt w projekcie). W najprostszej formie mogą to być litery wyświetlane w wierszu poleceń lub w jupyterze (max 1pkt), w bardziej rozbudowanej formie wyświetlanie inferfejsu graficznego (przy pomocy np. tkintera, pygame'a albo psychopy'a). Program (nazwijmy go Wyświetlaczem Liter) powinien wyświetlać kolejno wszystkie litery alfabetu przez wybrany odcinek czasu (np. każda litera przed jedną sekundę). Po skończeniu alfabetu powinien zaczynać od nowa. Muszą Państwo wiedzieć w którym momencie były wyświetlane konkretne litery (np. że litera "F" pojawiała się między 6 a 7 sekundą). Informacja ta będzie potrzebna do odkodowania liter wybranych przez mrugnięcia.

Po zebraniu danych należy przygotować kod (w arkuszu jupyter notebook) który wykrywa mrugnięcia i odszyfrowuje jakie litery zostały "wymrugane" przez osobę oraz raport z projektu zawierający opis zadania, wybrane metody, opis analizy i uzyskanych wyników, opis błędów które się pojawiły i możliwych ulepszeń. Deadline to **8. stycznia**.



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




