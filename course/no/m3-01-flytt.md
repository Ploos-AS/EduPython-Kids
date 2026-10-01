# M3.1 – Flytt!

## 🎯 Oppdrag

Lag et lite spillvindu og styr figuren med piltastene.

Du har allerede brukt Turtle til å tegne. Nå skal skilpadden bli en **spillefigur**.

## 💻 Start her

```python
import turtle

skjerm = turtle.Screen()
skjerm.title("Mitt første spill")

spiller = turtle.Turtle()
spiller.shape("turtle")
spiller.penup()

def hoyre():
    spiller.forward(20)

def venstre():
    spiller.backward(20)

skjerm.listen()
skjerm.onkey(hoyre, "Right")
skjerm.onkey(venstre, "Left")

turtle.done()
```

Kjør programmet. Klikk én gang i spillvinduet hvis det trengs, og prøv **høyre** og **venstre** piltast.

Du har laget styring!

## 🔧 Endre

Finn tallet `20`. Hva tror du skjer hvis du gjør det til `50`? Prøv. Hva med `5`? Velg farten du liker best.

## 🚀 Fire retninger

Kan du få figuren til å gå opp og ned også?

```python
def opp():
    spiller.sety(spiller.ycor() + 20)

def ned():
    spiller.sety(spiller.ycor() - 20)
```

Koble dem til `"Up"` og `"Down"` på samme måte som høyre og venstre.

## 🤔 Tenk

Når du trykker en tast, kjører Python en funksjon. Hvilken funksjon kjører når du trykker høyre? Hva må du endre hvis figuren skal ta større steg?

## ⭐ Utfordring

Gjør figuren til din: velg en annen form, velg en annen fart, gi vinduet et morsomt navn, eller finn på en liten regel.

## 🐞 Bug-jakt

Hvis tastene ikke virker: klikk i Turtle-vinduet, sjekk store bokstaver i tastnavnene, og sjekk at funksjonsnavnet er skrevet likt begge steder. Endre én ting om gangen og prøv igjen.

## 🧠 Det du lærte

- et tastetrykk kan starte en funksjon
- en figur kan flyttes med Python
- små endringer i tall kan forandre hvordan et spill føles

**Neste oppdrag:** Kan vi hindre figuren i å forsvinne ut av skjermen?
