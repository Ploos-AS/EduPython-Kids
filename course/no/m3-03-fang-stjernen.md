# M3.3 – Fang stjernen! ⭐

## 🎯 Oppdrag

Det ligger en stjerne på skjermen. Klarer du å fange den med spillefiguren?

Når du fanger den, hopper den til et nytt sted.

## 💻 Lag spilleren og stjernen

```python
import random
import turtle

skjerm = turtle.Screen()
skjerm.title("Fang stjernen!")
skjerm.setup(600, 400)

spiller = turtle.Turtle()
spiller.shape("turtle")
spiller.penup()

stjerne = turtle.Turtle()
stjerne.shape("circle")
stjerne.penup()
stjerne.goto(150, 80)

STEG = 20
```

Vi bruker en sirkel som mål nå. Senere kan du gjøre spillet mer personlig.

## 🎮 Beveg spilleren

```python
def hoyre():
    spiller.setx(spiller.xcor() + STEG)
    sjekk_fangst()

def venstre():
    spiller.setx(spiller.xcor() - STEG)
    sjekk_fangst()

def opp():
    spiller.sety(spiller.ycor() + STEG)
    sjekk_fangst()

def ned():
    spiller.sety(spiller.ycor() - STEG)
    sjekk_fangst()
```

Etter hvert steg spør vi: **Fanget jeg stjernen?**

## ⭐ Fang den!

Turtle kan måle avstanden mellom to figurer:

```python
def sjekk_fangst():
    if spiller.distance(stjerne) < 25:
        flytt_stjerne()
```

Hvis avstanden er mindre enn `25`, regner spillet stjernen som fanget.

## 🎲 La stjernen hoppe

```python
def flytt_stjerne():
    x = random.randint(-250, 250)
    y = random.randint(-150, 150)
    stjerne.goto(x, y)
```

`random.randint()` velger et tilfeldig heltall. Derfor vet du ikke hvor stjernen dukker opp neste gang.

## ⌨️ Koble til tastene

```python
skjerm.listen()
skjerm.onkey(hoyre, "Right")
skjerm.onkey(venstre, "Left")
skjerm.onkey(opp, "Up")
skjerm.onkey(ned, "Down")

turtle.done()
```

Kjør spillet. Fang målet flere ganger.

## 🔧 Endre

Prøv å endre `25` i fangsttesten.

Hva skjer med `10`? Hva skjer med `60`?

Finn et tall som føles rettferdig.

## 🧪 Eksperiment

Endre området stjernen kan dukke opp i. Hva skjer hvis du bruker:

```python
x = random.randint(-100, 100)
y = random.randint(-50, 50)
```

Er spillet lettere eller vanskeligere?

## ⭐ Utfordring

Gjør målet til ditt eget. Du kan for eksempel endre form og størrelse:

```python
stjerne.shape("square")
stjerne.shapesize(0.7)
```

Hva skal spilleren samle i ditt spill? En skatt? Mat til et monster? En energikule?

## 🌟 Ekstra utfordring

Kan du få stjernen til å starte på et tilfeldig sted allerede når spillet begynner?

Hint: Når kan du kalle `flytt_stjerne()`?

## 🤔 Tenk

- Hvordan vet spillet at figurene er nær hverandre?
- Hvorfor bruker vi tilfeldige steder?
- Hva gjør spillet morsommere: et stort eller lite fangstområde?

## 🐞 Bug-jakt

Hvis ingenting skjer når du treffer målet:

1. prøv et større tall enn `25`
2. sjekk at `sjekk_fangst()` kjøres etter bevegelsen
3. skriv ut avstanden med `print(spiller.distance(stjerne))`

Tallene kan igjen være spor.

## 🧠 Det du lærte

- spillet kan måle avstanden mellom to ting
- `if` kan bestemme når noe er fanget
- tilfeldige tall kan gjøre et spill forskjellig hver gang
- én hendelse kan starte en ny hendelse: fangst → flytt målet

**Neste oppdrag:** Hvor mange stjerner klarer du å fange? Vi lager poeng!
