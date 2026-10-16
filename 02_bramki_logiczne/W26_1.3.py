
'''

Uruchom poniższy kod, wpisz w wywołany w nim input swój numer indeksu, a następnie przedstaw otrzymaną formułę logiczną w postaci najbardziej adekwatnego do niej schematu bramkowego.

Zamieść:

- swój numeru indeksu,
- otrzymaną formułę logiczną,
- formułę z nazwami bramek w zamian symboli spójników (1 pkt),
- schemat bramkowy (1 pkt).

'''


indeks = input('Twój nr indeksu: ')

if int(indeks[-1]) % 2 != 0:
    indeks = indeks.translate(indeks.maketrans({'8':'6', '6':'8'}))

rozpiska = {0:'➔ ', 1:'↓', 2:'∧', 3:'v', 4:'⭤ ', 5:'⭤ ', 6:'⊻', 7:'↓', 8:'↑', 9:'v'}

formula = '((p'

for i, num in enumerate(indeks[1:]):
    formula += ' ' + rozpiska[int(num)] + ' '
    if i in [1, 3, 5]:
        formula += '('
    formula += 'p'
    if i in [0, 4]:
        formula += ')'
    elif i == 2:
        formula += '))'
        
print('Twoja formuła:   ' + formula)


