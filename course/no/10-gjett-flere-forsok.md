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

Nå samarbeider `while` og `if`: løkken bestemmer om spillet fortsetter, mens `if` gir hint.

## 🔧 Endre

Bytt området til 1–50 eller 1–100.

## 🤔 Tenk

Hvorfor setter vi `gjett = None` før løkken? Vi trenger en startverdi som ikke allerede er det hemmelige tallet.

## ⭐ Utfordring

Gi spilleren maksimalt fem forsøk. Kan du få spillet til å fortelle når forsøkene er brukt opp?

## 🌟 Ekstra

La spilleren velge vanskelighetsgrad før spillet starter.
