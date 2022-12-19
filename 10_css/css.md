# CSS

CSS (Cascading Style Sheets) - Kaskadowe Arkusze Stylów - tworzony i rozwijany od 1994 roku język służący do programowania wyglądu stron HTML.

Zanim stworzono CSS do opisu wyglądu strony używano specjalnych znaczników (np. `<font size="3" face="arial">` , `<center>`) albo atrybutów (np. color="green"). Programowanie wyglądu strony przy użyciu tych znaczników było:

1. uciążliwe dla dużych stron (poza tym zwiększało ich rozmiar);
2. zaciemniało strukturę treści dokumentu. Poza tym w przypadku, gdy trzeba było zmienić wygląd strony należało przeglądać i zmieniać wszystkie pliki `*.html`, które tą stronę tworzyły.

W przypadku CSS możliwe jest zakodowanie wyglądu strony w jednym pliku (np. style.css), a później w każdym z plików HTML wskazywanie na ten plik jako źródło styli używanych do wyświetlania strony. W ten sposób zmieniając jeden plik, możemy zmieniać wygląd wszystkich dokumentów HTML.

## Arkusze stylów
Reguły stylów mogą być zawarte w zewnętrznym pliku z rozszerzeniem .css (arkuszu stylów).
Arkusze stylów dodajemy do dokumentu HTML przy pomocy znacznika link wewnątrz nagłówka dokumentu. Poniższy kod oznacza, że do kontroli wyglądu danego dokument HTML używane będą style CSS zapisane w pliku style.css (umieszczonym w tym samym katalogu, co dany plik HTML).

```
<head>
    ...
    <link rel="stylesheet" href="style.css" />
</head>
```

Atrybuty:

- rel - definiuje typ relacji między dołączanym dokumentem, a dokumentem HTML — w tym przypadku stylesheet (arkusz stylów)
- href - adres dołączanego elementu (pełny adres URL lub nazwa pliku)

Struktura arkusza stylów jest taka sama jak zawartość omówionego powyżej znacznika style — jest to zbiór reguł opisanych przez selektory i cechy stylów.

Podsumowując - aby formatować wygląd dokumentu HTML przy pomocy CSS trzeba w pliku HTML (w sekcji `<head>`) umieścić `<link rel="stylesheet" href="style.css />`, a poza tym stworzyć plik style.css (nazwa moze byc inna, np. zielonastrona.css, ale nazwa style.css jest powszechnie stosowana).

## Selektory i cechy — definiowanie stylu

Style definiujemy w formie reguł:
```
selektor {
    cecha: wartość;
    inna-cecha: wartość;
}
```
Selektor wskazuje do których elementów dokumentu HTML mają być dodane wymienione między nawiasami style.
Najprostszym selektorem jest podanie nazwy znacznika. Wtedy style będą dodane do wszystkich obiektów danego typu.

Przykładowo:
```
p {
    font-size: 20px;
}
```
- Więcej cech
Oto przykład obrazujący różne cechy dla akapitu:
```
p {
    font-size: 20px;
    font-family: Arial, Verdana, sans-serif;
    color: white;
    background-color: black;
    text-align: right;
    text-decoration: underline;
}
```

### Formatowanie tła:

1. Tło o jednolitym kolorze:
trzy sposoby określania koloru (słowo/wartość RGB w systemie szesnastkowym/wartość składowych RGB)

- background-color: red;
- background-color: #FF9900;
- background-color: rgb(255,0,0);
Składowe RGB to wartości pomiędzy 0 a 255 określające odpowiednio "ilość" koloru czerwonego (Red), zielonego (Green) oraz niebieskiego (Blue). Wartość rgb(255,40,0) oznacza, że barwa składa się z maksymalnej ilości koloru czerwonego (255), 40 koloru zielonego i w jej skład nie wchodzi kolor niebieski.


2. Obrazek jako tło elementu

- background-image: url('obrazek.png');
Domyślnie obrazek będzie się powtarzał. Można to kontrolować: `background-repeat: no-repeat;`

Zamiast no-repeat można wpisać repeat-x albo repeat-y, które mówią, iż obrazek ma się powtarzać tylko wzdłuż osi X albo tylko wzdłuż osi Y.
Jeśli obrazek nie ma się powtarzać można ustawić jego położenie:
`background-position: top right;`

3. Skrótowy zapis
To wszystko można skrótowo zapisać:

```
background: #FE24A3 url('obrazek.png') no-repeat top right;
```

Możemy używać tych cech do określania wyglądu tła elementów - np. Możemy ustawić, żeby tło akapitu było zielone.
```
p {
    background-color: green;
}
```
Możemy również ustawić tło całej strony:
```
body {
    background-color: red;
}
```
### Formatowanie tekstu
```
h1 {
    color: blue;
    text-align: justify; /*tekst justowany, mozna też wpisać: right albo left - wyrównanie do prawej/lewej*/
    text-decoration: underline; /*inne wartości: none, line-through, ...*/
    font-family: arial, verdana, sans-serif;
    font-style: italic; /*moze byc też normal*/
    font-size: 20px;
}
```
## Wyróżnianie i grupowanie elementów

CSS oferuje wiele sposobów na wyróżnienie pojedynczych obiektów lub ich klas, niezależnie od tego, do jakiego typu obiektu należą — umożliwia więc także grupowanie elementów.

### Identyfikator
Można wskazać w stylach element o konkretnym identyfikatorze **id**.

- Szary kolor tła dla elementu z identyfikatorem *important*:
```
#important{
    background-color: #CCCCCC;
}
```
- Usunięcie stylów listy o identyfikatorze *references*:
```
ul#references {
    list-style: none;
    padding: 0;
    margin: 0;
}
```

### Klasa

Identyfikator id ma pewne ograniczenie — w dokumencie może znajdować się tylko jeden element z identyfikatorem o danej wartości. Jeśli chcemy w pewien sposób wyróżnić kilka elementów możemy im nadać klasę (lub klasy) przy pomocy atrybutu **class**

Np.
```
<ul id="mustsee">
    <li class="first">About time</li>
    <li>O autorze</li>
    <li class="new current">Interstellar</li>
    <li class="new last">Mama</li>
</ul>

<p class="new">To jest nowość!</p>
```

Dany element może mieć kilka klas (oddzielonych spacjami). Kolejność wymienionych klas nie ma znaczenia.

Selektory wykorzystujące klasy wyglądają następująco:

- Dowolny element z klasą *new* ma być czerwony:
```
.new {
    color: red;
}
```

- Element li z klasą *current* ma być pogrubiony:
```
li.current {
    font-weight: bold;
}
```

- Element li z klasą *first* ma mieć ramkę z prawej strony:
```
li.first {
    border-right: solid 1px blue;
}
```

- Element li z klasami *last* i *current* ma mieć tekst pochylony i kolor zielony.

```
li.last.current {
    font-style: italic;
    color: green;
}
```

Nazwy klas powinny być związane z semantycznym znaczeniem danych elementów, a nie z ich stylami.

Przykładowo dobre nazwy klas to first, last, new, important itp.

### Hierarchia elementów

W selektorach możemy też wykorzystać wiedzę o strukturze stylowanego dokumentu HTML i odwoływać się do elementów znajdujących się wewnątrz innych elementów.

- Element em wewnątrz paragrafu ma być pogrubiony:
```
p em {
    font-weight: bold;
}
```

- Element em wewnątrz nagłówka ma być pochylony:
```
h1 em {
    font-style: italic;
}
```

- Element li wewnątrz listy o identyfikatorze #menu ma mieć tło żółte:
```
ul#mustsee li {
    background-color: yellow;
}
```

- Element li o klasie *current* wewnątrz listy o identyfikatorze #mustsee ma mieć tło szare:
```
ul#mustsee li.current {
    background-color: #CCCCCC;
}
```

UWAGA!!!
Taki selektor wyznacza wszystkie elementy niżej w hierarchii — nie tylko bezpośrednie dzieci. Może to stwarzać problemy np. przy zagnieżdżonych listach.

### Grupowanie elementów

Jeśli te same style dotyczą różnych elementów, można je pogrupować:

- Wszystkie nagłówki mają być pogrubione:
```
h1, h2, h3, h4, h5, h6 {
    font-weight: bold;
}
```

- Elementy listy o id #mustsee i elementy list o klasie *links* mają być niebieskie:
```
#mustsee li, ul.links li {
    color: blue;
}
```

Grupować możemy dowolne selektory oddzielając je przecinkami.

### Pseudo-klasy dla linków (i nie tylko)

Specyfikacja CSS definiuje pewne pseudo-klasy pozwalające wskazywać elementy o pewnych specyficznych własnościach.

Przykładowo dla linków mamy 4 pseudo-klasy (uwaga na pisownię — używamy dwukropka, a nie kropki):

```
/* link w stanie "spoczynku" ma być niebieski z podkreśleniem */
a:link {
    color: blue;
    text-decoration: underline;
}

/* link odwiedzony ma być szary */
a:visited {
    color: #CCCCCC;
}

/* link nad którym jest kursor myszy ma być pomarańczowy z niebieskim tłem */
a:hover {
    color: orange;
    background-color: blue;
}

/* link który jest klikany ma być pomarańczowy bez tła */
a:active {
    color: orange;
    background-color: transparent;
}
```

Aby wszystko dobrze działało, należy trzymać się kolejności definiowanej przez zasadę LoVe HAte (:link :visited :hover :active).

Pseudo-klasa :hover pozwalająca wskazać elementy nad którymi znajduje się kursor myszy może być używany nie tylko do linków:

```
tr:hover {
    background-color: #CCCCCC;
}
```
###   Zadanie <img src="../images/pencil.png" width="20" align="left">
Stwórz nagłówek, który będzie zmieniał czcionkę na pogrubioną po najechaniu na niego myszką. Wykorzystaj id elementu. 

## Dziedziczenie

Dziedziczenie jest dość naturalną cechą stylów CSS. Polega ono na tym, że elementy dokumentu HTML dziedziczą reguły stylów po elementach, w których się znajdują.

Przykładowo wszystkie elementy em i strong znajdujące się wewnątrz paragrafu dziedziczą po tym paragrafie czcionkę, jej kolor i rozmiar (o ile ich własne style tego nie definiują na nowo).

Należy jednak pamiętać, że nie wszystkie cechy stylów są dziedziczone!

Dziedziczone są wszystkie właściwości czcionki i tekstu, także kolor tekstu color, ale już tło i kolor tła background-color nie są dziedziczone!

### Model "pudełkowy" - box model
Tzw. model pudełkowy służy definiowaniu rozmiarów i odstępów między elementami blokowymi dokumentu HTML.
Rozmiary elementów blokowych opisywane są wysokością i szerokością (width height), odstępem padding, ramką border i marginesem margin.


```
p.wybrane {
    margin-top: 100px;
    margin-bottom: 100px;
    margin-right: 150px;
    margin-left: 80px;
}
```
```
p.wybrane {
    border-style: solid;
}
```
```
p.wybrane {
    padding-top: 50px;
    padding-right: 30px;
    padding-bottom: 50px;
    padding-left: 80px;
}
```


## Znaczniki `<div>` i `<span>`
Własności *block* i *inline*

Przy okazji omawiania dwóch nowych znaczników warto wspomnieć o różnicy między elementami blokowymi (block) i inline:

- Elementy blokowe "zabierają" całą dostępną szerokość (width) i domyślnie "korzystają" z końca linii (line break) przed i po własnym wystąpieniu
przykładowe elementy blokowe to: `<p>`, `<h_z dowolnym numerem>`, `<div>`
- Elementy inline zajmują tylko tyle szerokości ile im potrzeba i nie wymuszają końca linii.
przykładowe elementy: `<a>`, `<span>`
Dodatkowo warto wiedzieć, że można wymusić własność block lub inline na elementach, które jej nie posiadają. Służy do tego cecha display:

```
a {
    display:block;
}
```

### `<div>` i `<span>`
Znacznik `<div>` (skrót od ang. division) pozwala "wydzielić" jakiś fragment naszego kodu XHTML
Pozwala to na grupowanie poszczególnych elementów naszej strony tak, aby móc je następnie "zespołowo" edytować przy użyciu arkuszy stylów:
`<div>` jest elementem blokowym.

Przy pomocy znacznika `<div>` możemy podzielić naszą stronę na stosowne sekcje. Podział ten następnie możemy wykorzystać w celu projektowania układu naszej strony.

Znacznik `<span>` działa analogicznie do `<div>`. Różnica polega na tym, że jest elementem inline

###   Zadanie <img src="../images/pencil.png" width="20" align="left">
Podziel swoją stronę na dwie części przy pomocy divów. Nadaj im różne kolory tła. 


## Co warto przeczytać
Ponieważ opracowywane przez nas zagadnienia są już dobrze opracowane w innych źródłach, dlatego nie wszystkie podstawowe zagadnienia z CSSa zostały tu poruszone. Aby przejść szybki pełny kurs CSSa, proponujemy stronę http://www.w3schools.com/css/default.asp , w menu po lewej pozycje CSS Basic od CSS Introduction do CSS table.
