---
# nagłówek YAML - ustawienia dokumentu
author: 'Imię Nazwisko'
title: 'Raport z badania'
date: 2025-10-16
---


Nowy wiersz w markdownie można utworzyć przez backslash\
lub dwie  
spacje.

Nowy akapit tworzymy pozostawiając pusty wiersz.

W taki sposób robimy w markdownie:

*kursywę*,          _też kursywę_, \
**pogrubienie**,    __też pogrubienie__, \
~~przekreślenie~~.

> Gdy chcemy wyróżnić jakiś tekst, np. cytat,
>
> możemy go wyeksponować przez znak ">".

Trzy kreski 

---

lub trzy gwiazdki

***

albo trzy podkreślenia

___

pozwalają zrobić poziomą linię.



Rozdział 1
===========

Podkreślenie znakami "=" daje nagłówek najwyższego poziomu.

Podrozdział 1.1
----------------

Podkreślenie znakami "-" daje nagłówek niższego poziomu.

Podrozdział 1.2
----------------

[Jakiś tekst.]


# Rozdział 2

Jeden znak "#" daje ten efekt co "=" - nagłówek najwyższego poziomu.

## Podrozdział 2.1

Dwa znaki "#" dają ten efekt co "-" - nagłówek niższego poziomu.

### Podpodrozdział 2.1.1
 
Trzy znaki "#" pozwalają na nagłówek jeszcze niższego poziomu.\
liczba znaków "#" = poziom zagłębienia nagłówka (nie jego rozmiar)
 
### Podpodrozdział 2.1.2

Nagłówki wykonane przez znaki "=" i "-" oraz przez znak "#" można bez problemu łączyć.


---

# Elementy możliwe do dodawania

**Listę numerowaną**

1. dodajemy
1. wypisując
4. kolejne
3. liczby

A **listę nienumerowaną**

- dodajemy
  + poprzez
+ znaki takie jak:
  - myślniki
  + plusy
  * i gwiazdki
- oraz
  * odpowiednią
      * do poziomu
        * liczbę
  * tabulacji

Możemy

1. dowolnie 
    - łączyć
      * oba
        1. typy
2. list


Myślniki ("-") oraz pionowe linie ("|") pozwalają na

| utworzenie | tabelki. |
|------------|----------|
| komórka    | komórka  |
| komórka    | komórka  |


Możemy też dodać tekst sformatowany jako kod, np. **pseudokod**. Pozwala na to 

    wcięcie
    z dwoma
    tabulacjami.
    
Będzie on jedynie sformatowany jako kod, więc nie będzie wykonywał się podczas kompilacji pliku.
    
Taki sam efekt uzyskamy umieszczając treść pomiędzy

```
trzema backtickami
z obu stron.
```

Pojedynczy `backtick` z obu stron pozwala na umieszczenie kodu w wierszu, pomiędzy tekstem.


Adres strony internetowej zostanie automatycznie przekonwertowany na **link**: https://bookdown.org/yihui/rmarkdown-cookbook/.
Ale możemy też dodać link do jakiegoś [słowa](https://bookdown.org/yihui/rmarkdown-cookbook/).

Żeby wstawić **obrazek** ze strony internetowej wystarczy dodać na początku wykrzyknik:

![Podpis obrazka](https://as2.ftcdn.net/v2/jpg/02/95/62/09/1000_F_295620903_viY99jOBVqnHczjrIiUEOY1vXSHG2gOo.jpg)


Jeśli obrazek jest na naszym dysku, to zamiast linku podajemy do niego ścieżkę:

![Podpis obrazka](Gdańsk.jpg)


# Integracja języka markdown z innymi językami

## Latex

Integracja z językiem LaTeX pozwala m.in. na pisanie **symboli i wzorów matematycznych**, w tekście: $T(23) = 4,21$; $p = 0,02$
oraz w trybie eksponowanym:

$$Z = \frac{U - \frac{n_1 n_2}{2}}{\sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12} - \frac{n_1 n_2 \sum_{i=1}^k (t_i^3 - t_i)}{12 (n_1 + n_2) (n_1 + n_2 - 1)}}}$$

Dzięki narzędziu pandoc, możliwe jest także korzystanie z pojedynczych komend języka LaTeX, jak i włączanie całych **bloków kodu** w tym języku.

## HTML 

Znaczniki HTML bez problemu:

<ol>
  <li>integrują
      <ul>
          <li>się</li>
          <li>z</li>
      </ul>
  </li>
  <li>kodem
      <ul>
          <li>Markdown</li>
      </ul>
  </li>
</ol>

Integracja markdowna z językiem HTML pozwala na dodatkowe elementy, np.

<p style="text-indent: 2em;">
na wcięty <b>akapit</b> oraz <b>twarde</b>&nbsp;<b>spacje</b> (ang. *non-breaking space*) albo indeksy<sub>dolne</sub> i <sup>górne</sup>

</p>

<!-- a także na komentarze -->
<!-- (poza nagłówkiem YAML, gdzie komentarze dodajemy przez "#"). -->

## CSS 

W szczególności, Markdown pozwala na użycie znacznika `style` w celu dodania do dokumentu formatowania. Alternatywą dla tego znacznika jest kompilacja pliku z powiązanym plikiem CSS przy pomocy narzędzia pandoc.

<!--
<style>                             
body {
  max-width: 850px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

h1, h2, h3 {
  color: orange;
}

p {
  margin-bottom: 20px;
}
</style>
-->

---

# Kompilacja

Jeśli chcesz zapisać swój plik w innym formacie, a na Twoim komputerze jest zainstalowany pandoc, najprostszym kodem kompilującym Twój plik do pliku HTMl jest:
```
pandoc plik.md -s -o plik.html
```
Modyfikując opcje tego wywołania możesz dopasować kompilację do swoich potrzeb. Na przykład, możesz powiązać plik z plikiem CSS:
```
pandoc plik.md -s --css style.css -o plik.html
```
Zzamiast tej opcji możesz też dodać do nagłówka YAML następujący kod:
```
output:
  html_document:
    css: style.css 
```

Jeśli nie zamierzasz swojego pliku wiązać z innymi plikami, możesz skorzystać z dodatku VS Code/VSCodium o nazwie ,,Markdown PDF''. Po wciśnięciu `CTRL+Shift+P`, wpisz `Markdown PDF: Export (html)` lub  `Markdown PDF: Export (pdf)` w zależności od formatu, który potrzebujesz.

---

# ZADANIE

### 1. Na podstawie pliku `do odtworzenia.html`, odtwórz go w Markdownie tak, żeby uzyskać taki sam plik HTML.

### 2. Jeśli na zajęciach z HTMLa nie zrealizowałeś wszystkich trzech ćwiczeń, dopisz odpowiedni kod HTMLa do pliku z zadania 1.





