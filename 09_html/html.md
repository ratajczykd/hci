# HTML

## Czym jest HTML5 i co znaczą znaczniki?

HTML (HyperText Markup Language) jest językiem opisu struktury zawartości strony internetowej. Opisywanie struktury oznacza, że mając daną treść strony, umieszczamy jej fragmenty między odpowiednimi znacznikami, przekazującymi przeglądarce internetowej informację, że dany fragment treści jest np. nagłówkiem, paragrafem tekstu, odnośnikiem itp. Używając tej informacji przeglądarka odpowiednio wyświetla poszczególne elementy strony.

Dla przykładu: dany tekst...

```
Oficjalna strona zrzeszenia Mrówki 110

Strona jest poświęcona działalności mrówek ,,Lasius niger'' znajdujących się w pokoju 110 na Wydziale Psychologii i Kognitywistyki. Zapewnia aktualności z ich życia oraz nowinki z błądzenia wśród traw.

Aktualności można śledzić również na witrynie https://www.facebook.com/Mr%C3%B3wki-110-104455090995866

Najnowsze zdjęcia [ZOBACZ ZDJĘCIA]

Działalność prowadzona jest od września 2019 roku.

```

…przepisujemy używając znaczników opisujących treść strony, która składa się z nagłówka i czterech akapitów.

```
<h1> Oficjalna strona zrzeszenia Mrówki 110 </h1>

<p> Strona jest poświęcona działalności mrówek ,,Lasius niger'' znajdujących się w pokoju 110 na Wydziale Psychologii i Kognitywistyki. Zapewnia aktualności z ich życia oraz nowinki z błądzenia wśród traw. </p>

<p> Aktualności można śledzić również na witrynie <a href="https://www.facebook.com/Mr%C3%B3wki-110-104455090995866">Mrówki 110</a> </p>

<p> Najnowsze zdjęcia [ZOBACZ ZDJĘCIA] </p>

<p> Działalność prowadzona jest od września 2019 roku. </p>

```

Znacznik `<h1>` oznacza, że następujący po tym znaczniku tekst jest nagłówkiem aż do znacznika `</h1>` (h jak header, cyfra oznacza ważność nagłówka `<h1>` to nagłówek najważniejszy, `<h2>` mniej ważny, …. , `<h6>` to nagłówek najmniej ważny).

Znacznik `<p>` oznacza, że następująca po tym znaczniku treść - aż do znacznika `</p>` - jest akapitem tekstu (p jak paragraph).

### Szablon prostej strony internetowej
Niestety samo oznaczenie znacznikami fragmentu tekstu i zapisanie go jako dokument o rozszerzeniu HTML nie czyni z niego poprawnie napisanej strony internetowej. Poza informacjami dotyczącymi struktury przekazanej treści należy podać jeszcze dodatkowe informacje o wersji języka HTML, którą stosujemy, kodowaniu znaków, jakiego używamy itp...

UWAGA: należy pamiętać, że edytor, w którym piszemy kod strony musi mieć to samo kodowanie, co strona (UTF-8 w naszym przypadku; patrz: `<meta charset="UTF-8">`)

A oto kompletny i poprawny (składniowo) dokument HTML.
```
<!DOCTYPE html>
<html lang="pl">
   <head>
       <title> Mrówki 110 </title>
       <meta charset="UTF-8">
   </head>
   <body>

   <h1> Oficjalna strona zrzeszenia Mrówki 110 </h1>

   <p> Strona jest poświęcona działalności mrówek ,,Lasius niger'' znajdujących się w pokoju 110 na Wydziale Psychologii i Kognitywistyki. Zapewnia aktualności z ich życia oraz nowinki z błądzenia wśród traw. </p>

   <p> Aktualności można śledzić również na witrynie <a href="https://www.facebook.com/Mr%C3%B3wki-110-104455090995866">Mrówki 110</a> </p>

   <p> Najnowsze zdjęcia [ZOBACZ ZDJĘCIA] </p>

   <p> Działalność prowadzona jest od września 2019 roku. </p>


    </body>
</html>
```
Wcięcia widoczne w powyższym kodzie są także ważne: czynią one kod przejrzystszym, łatwiejszym do zrozumienia i edytowania.

Skopiujmy powyższy kod do notatnika lub Atoma. Zapiszmy plik pod nazwą index.html i otwórzmy plik przy pomocy przeglądarki.

### Struktura
Cały dokument oznaczony jest znacznikiem <html>, wewnątrz tego znacznika znajduje się znacznik <head> zawierający różne informacje o treści strony internetowej, następnie jest znacznik <body> w którym umieszczamy ciało (treść) dokumentu. Na ogół znaczniki mają strukturę określającą "zasięg". Działa to w ten sposób, że oprócz znacznika otwierającego (np. <html>), należy podać znacznik zamykający (w tym przypadku - `</html>`):

```
<html>
    <head>
        <title> ... </title>
         ....
    </head>
    <body>
        ...
    </body>
</html>
```

- `<!DOCTYPE html>`
nie jest znacznikiem HTML, przekazuje informacje przeglądarce internetowej dotyczące rodzaju dokumentu.

- `<html> treść </html>`
tekst znajdujący się pomiędzy tymi znacznikami jest dokumentem HTML.

- `<head> treść </head>`
między tymi znacznikami umieszczamy informacje dotyczące dokumentu takie jak:

- `<title> treść </title>`
tekst umieszczony między tymi znacznikami będzie widoczny w pasku na górze okna przeglądarki

- `<meta charset="UTF-8">`
Opisuje system kodowania znaków. Używamy rekomendowanego systemu kodowania UTF-8. Na tej stronie umieszczone są informacje o zapisywaniu dokumentów używając systemu kodowania UTF-8.

- `<body> treść </body>`
W tej części wpisujemy treść dokumentu.

## Dodatkowe znaczniki

- Znak końca linii (line break). Po znaku `<br>` tekst przechodzi do kolejnego wiersza. Ten znacznik nie ma zamknięcia - nie istnieje `</br>`

- Pogrubienie: `<strong>coś ważnego</strong>` (również występuje znacznik `<b>`)

- Kursywa: `<em>coś charakterystycznego</em>`

- Hiperłącze: `<a href="hiperłącze"> Wyświetlany tekst </a>`

Analogicznie możemy tworzyć również postrony naszej strony głównej! Jednak wcześniej musimy oczywiście stworzyć nowy plik HTML reprezentujący tę podstronę.

Następnie dodajemy na naszej stronie głównej kod:

`<a href="gallery.html">Galeria</a>`

- Obraz: `<img src="ścieżka do obrazu" alt="Tekst wyświetlany gdy obraz nie może się załadować"
title="tekst wyświetlany przy najechaniu na obrazek kursorem" width="szerokość" height="wysokość">`
Jako grafiki wstawiać możemy na przykład pliki typu: gif, jpg, png.

- Komentarz: ` <!-- Tekst lub dowolna treść dokumentu HTML w komentarzach jest ignorowana --> `

- Tematyczna przerwa. Znak `<hr>` który wyświetlany jest najczęsciej jako pozioma linia. Tak jak w przypadku `<br>`, nie posiada zamknięcia.

### Tabele

Tabele tworzy się za pomocą znacznika:
`<table></table>`

Poszczegolne wiersze tabeli:
`<tr></tr>`

Komórki:
`<td></td>`

Przykład:

```
<table>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
</table>
```

Który wygląda tak:
<table>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><td>treść</td><td>treść</td><td>treść</td></tr>
</table>

Nagłówek tabeli:
`<caption>nagłówek</caption>`

Nagłówek kolumny lub wiersza:
`<th>nagłówek kolumny</th>`

Przykład:

```
<table>
<caption>nagłówek</caption>
<tr><td></td><th>nagłówek kolumny 1</th><th>nagłówek kolumny 2</th><th>nagłówek kolumny 3</th></tr>
<tr><th>nagłówek wiersza 1</th><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><th>nagłówek wiersza 2</th><td>treść</td><td>treść</td><td>treść</td></tr>
<tr><th>nagłówek wiersza 3</th><td>treść</td><td>treść</td><td>treść</td></tr>
</table>
```

Formatowanie elementów na stronie (tabeli, obrazków, akapitów, etc.) zaleca się przeprowadzać za pomocą języka CSS.

Łączenie komórek tabeli w pionie:
`<td rowspan="x">treść</td>`

Analogicznie dla nagłówków:
`<th rowspan="x">nagłówek wiersza</th>`
gdzie x oznacza liczbę komórek, które mają zostać połączone

Łączenie komórek tabeli w poziomie:
`<td colspan="x">treść</td>`

Analogicznie dla nagłówków:
`<th colspan="x">nagłówek kolumny</th>`
gdzie x oznacza liczbę komórek, które mają zostać połączone

   ###   Zadanie <img src="../images/pencil.png" width="20" align="left">
   
   Stwórz tabelę zgodną z poniższą. Do wyświetlenia obrysu możesz użyć artybutu tabeli `border="1"`.\
   
   ![](../images/tabela1.png)

### Listy/wykazy

Nieuporządkowany (unordered list) - elementy poprzedzane są dużymi kropkami:
`<ul>…</ul>`

Uporządkowany (ordered list) - elementy są numerowane:
`<ol>…</ol>`

Elementy wykazu:
`<li>element</li>`

Wykazy można zagnieżdżać.

Przykład:

```
<ul>
    <li>coś</li>
    <li>drugie coś</li>
    <li>wykaz zagnieżdżony
        <ol>
            <li>element</li>
            <li>element</li>
            <li>element</li>
        </ol>
    </li>
    <li>i jeszcze coś</li>
</ul>
```

###   Zadanie <img src="../images/pencil.png" width="20" align="left">
   
   Stwórz listę zgodną z poniższą. 
   
   ![](../images/lista1.png)
   
## Formularze

Formularze służą do pobierania danych od użytkowników odwiedzających naszą stronę internetową.

Struktura ogólna: Formularz zawierający *różne pola* tworzy się za pomocą znacznika:
`<form> różne pola </form>`

### Pole tekstowe
- Pola tekstowe w formularzu umieszcza się za pomocą znacznika:
`<input type="text">`

* nazwa pola:
name="pole1"

* zawartość domyślna (wpisana w polu początkowo):
value="costam"

* rozmiar pola - liczba znaków:
size="50"

Przykładowy formularz:
```
<form>
  <label for="name">Imię i Nazwisko:</label><br>
  <input type="text" id="name" name="name"><br>
</form>
```

- Znacznik `<label>` definiuje etykiety w formularzu. Atrybut **for** znacznika ``<label>`` powinien być taki sa jak **id** elementu `<input>`, aby powiązać je ze sobą.


### Pole opcji
Możemy również stworzyć pole opcji, do którego służy znacznik `<input type="radio">`

Na przykład:

```
<form>
  <input type="radio" id="m" name="plec" value="m">
  <label for="ma">Mężczyzna</label><br>
  <input type="radio" id="k" name="plec" value="k">
  <label for="k">Kobieta</label><br>
  <input type="radio" id="i" name="plec" value="i">
  <label for="i">Inna</label>
</form>
```

Innym rodzajem pola wyboru, który możemy zastosować to checkboxy. Na przykład:

```
<form>
  <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
  <label for="vehicle1"> I have a bike</label><br>
  <input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
  <label for="vehicle2"> I have a car</label><br>
  <input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
  <label for="vehicle3"> I have a boat</label>
</form>
```

- Do wysyłania danych wpisanych w formularzu służy przycisk:
`<input type="submit">`

- Co się dzieje dalej z informacjami z formularza definiuje atrybut **action**.

Na przykład dla `<form action="/action_page.php">` dane zostaną wysłane do podstrony **action_page.php**.

   
   
###   Zadanie <img src="../images/pencil.png" width="20" align="left">
   
   Stwórz formularz zgodny z poniższym. 
   
   ![](../images/checkboxs.png)

## Pomoce naukowe
Samouczek: http://www.w3schools.com/html

Lista i opis znaczników HTML:
http://www.w3schools.com/tags/
