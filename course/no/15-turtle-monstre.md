# 15 – Turtle-utfordring: Robotmonster

## 🎯 Oppdrag

Tegn ditt eget robotmonster av enkle former.

Du trenger ikke tegne perfekt. Målet er å bruke kode som et tegneverktøy og dele en større idé opp i mindre deler.

## 💻 Start med én byggestein

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

Funksjonen `firkant()` er én byggestein. Nå kan du lage flere.

## 🧱 Bygg med funksjoner

Lag funksjoner for minst tre deler, for eksempel:

- kropp
- øye
- antenne
- fot
- munn

Flytt pennen mellom delene med `penup()`, `goto(x, y)` og `pendown()`.

Test én funksjon om gangen før du setter sammen hele monsteret.

## 🔧 Endre

Gjør én funksjon fleksibel med en parameter, for eksempel:

```python
def oye(storrelse):
    ...
```

Prøv to forskjellige verdier.

## 🤔 Tenk

Hvorfor er funksjoner nyttige når roboten skal ha to like øyne eller flere bein?

Hva kan du gjenbruke hvis du vil tegne monster nummer to?

## ⭐ Utfordring

Lag et helt eget monster. Gi det et navn og skriv navnet med `penn.write()`.

Se [ekstra øvelser](../../exercises/no/15-turtle-monstre.md) når du vil prøve mer.

## 🌟 Ekstra

Lag to monstre på samme skjerm. Gjør dem forskjellige ved å sende størrelse eller andre verdier inn i funksjonene.

## 🐞 Bug-jakt

Hvis hele tegningen blir vanskelig å feilsøke, kommenter midlertidig bort funksjonskall og test én kroppsdel alene.

Spør:

- Tegner funksjonen riktig form?
- Starter pennen på riktig sted?
- Er pennen oppe eller nede når den flyttes?

## 🧠 Det du lærte

- Et større problem kan deles i mindre funksjoner.
- Samme funksjon kan gjenbrukes.
- Parametere kan lage variasjoner av samme byggestein.
- Det er enklere å finne feil når du tester små deler hver for seg.
