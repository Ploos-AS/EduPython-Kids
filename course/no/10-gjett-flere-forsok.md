# 10 – Gjett tallet med flere forsøk

## 🎯 Oppdrag

Oppgrader gjetteleken slik at spilleren får prøve helt til svaret er riktig.

## 💻 Kode

```python
import random

hemmelig = random.randint(1, 20)
gjett = None
forsok = 0

while gjett != hemmelig:
    gjett = int(input("Gjett et tall fra 1 til 20: "))
    forsok = forsok + 1

    if gjett < hemmelig:
        print("For lavt!")
    elif gjett > hemmelig:
        print("For høyt!")

print("Riktig! Du brukte", forsok, "forsøk.")
```

Nå samarbeider `while` og `if`: løkken bestemmer om spillet fortsetter, mens betingelsene gir hint.

Variablene `hemmelig`, `gjett` og `forsok` beskriver hva som skjer i spillet akkurat nå. Dette kan vi kalle **spilltilstand**.

## 🔧 Endre

Bytt området til 1–50 eller 1–100.

## 🤔 Tenk

Hvorfor setter vi `gjett = None` før løkken?

Vi trenger en startverdi før Python kan teste `gjett != hemmelig`. `None` betyr her at vi ennå ikke har et gjett.

## ⭐ Utfordring

Gi spilleren maksimalt fem forsøk. Kan du få spillet til å fortelle når forsøkene er brukt opp?

Se [ekstra øvelser](../../exercises/no/10-gjett-flere-forsok.md) når du vil prøve mer.

## 🌟 Ekstra

La spilleren velge vanskelighetsgrad før spillet starter.

## 🐞 Bug-jakt

Hvis spillet stopper for tidlig eller aldri stopper, skriv midlertidig ut `gjett`, `hemmelig` og `forsok`.

Hva forteller verdiene deg?

## 🧠 Det du lærte

- `while` kan drive en spillrunde som fortsetter til en betingelse endres.
- En teller kan holde styr på antall forsøk.
- Flere variabler kan sammen beskrive spilltilstanden.
- Midlertidige `print()`-linjer kan hjelpe når du leter etter en bug.
