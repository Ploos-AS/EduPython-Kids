# 15 – Turtle-utfordring: Robotmonster

## 🎯 Oppdrag

Tegn ditt eget robotmonster av enkle former.

Du trenger ikke tegne perfekt. Målet er å bruke kode som et tegneverktøy.

## 🧱 Bygg med funksjoner

```python
import turtle

penn = turtle.Turtle()
penn.speed(0)

def firkant(storrelse):
    for _ in range(4):
        penn.forward(storrelse)
        penn.right(90)

firkant(100)
turtle.done()
```

## 🔧 Nye deler

Lag funksjoner for minst tre deler:

- kropp
- øye
- antenne
- fot
- munn

Flytt pennen med `penup()`, `goto(x, y)` og `pendown()`.

## 🤔 Tenk

Hvorfor er funksjoner nyttige når roboten skal ha to like øyne eller flere bein?

## ⭐ Utfordring

Lag et helt eget monster. Gi det et navn og skriv navnet med `penn.write()`.

## 🌟 Ekstra

Lag to monstre på samme skjerm. Kan du gjøre dem forskjellige ved å sende størrelse eller andre verdier inn i funksjonene?
