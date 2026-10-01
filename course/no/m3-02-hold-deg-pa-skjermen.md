# M3.2 – Hold deg på skjermen!

## 🎯 Oppdrag

I forrige oppdrag kunne du styre figuren med piltastene. Men hva skjer hvis du fortsetter samme vei?

**Oi. Figuren forsvinner!** Nå skal vi lære spillet hvor kanten er.

## 💻 Start med fire retninger

```python
import turtle

skjerm = turtle.Screen()
skjerm.title("Hold deg på skjermen")
skjerm.setup(600, 400)

spiller = turtle.Turtle()
spiller.shape("turtle")
spiller.penup()

STEG = 20

def hoyre():
    spiller.setx(spiller.xcor() + STEG)

def venstre():
    spiller.setx(spiller.xcor() - STEG)

def opp():
    spiller.sety(spiller.ycor() + STEG)

def ned():
    spiller.sety(spiller.ycor() - STEG)

skjerm.listen()
skjerm.onkey(hoyre, "Right")
skjerm.onkey(venstre, "Left")
skjerm.onkey(opp, "Up")
skjerm.onkey(ned, "Down")

turtle.done()
```

Kjør programmet og prøv å kjøre figuren helt ut av vinduet.

## 🗺 Hvor er figuren?

Python kan spørre hvor figuren er:

```python
print(spiller.xcor())
print(spiller.ycor())
```

`x` forteller hvor langt figuren er mot venstre eller høyre. `y` forteller hvor langt den er ned eller opp. Midten er omtrent `x = 0`, `y = 0`.

Du trenger ikke pugge dette. Flytt figuren og se hva tallene gjør.

## 🧪 Eksperiment

Legg `print(spiller.xcor(), spiller.ycor())` inn i en bevegelsesfunksjon. Kjør og trykk piltastene. Hva skjer med tallene?

## 🧱 Bygg en høyre vegg

```python
def hoyre():
    if spiller.xcor() < 280:
        spiller.setx(spiller.xcor() + STEG)
```

Kjør mot høyre kant igjen. Nå stopper figuren!

`280` er valgt fordi vinduet er 600 piksler bredt og figuren trenger litt plass ved kanten.

## 🔧 Endre

Prøv `250` i stedet for `280`. Hvor stopper figuren? Prøv `100`. Kan du se sammenhengen mellom tallet og den usynlige veggen?

## ⭐ Utfordring

Lag tre vegger til. Disse spørsmålene hjelper:

```python
spiller.xcor() > -280
spiller.ycor() < 180
spiller.ycor() > -180
```

Hvilket passer til venstre, opp og ned? Prøv deg fram.

## 🌟 Ekstra utfordring

Hva om kanten sender spilleren tilbake til midten i stedet for å stoppe den?

```python
spiller.goto(0, 0)
```

Finn på din egen regel.

## 🤔 Tenk

- Hva skjer med `x` når figuren går mot høyre?
- Hva skjer med `y` når figuren går opp?
- Må alle spill stoppe ved kanten?

## 🐞 Bug-jakt

Hvis figuren stopper for tidlig eller fortsatt forsvinner, skriv ut `xcor()` eller `ycor()`, flytt sakte mot kanten og se hvilket tall figuren har. Endre én grense om gangen.

Tallene er spor. De kan hjelpe deg å finne feilen.

## 🧠 Det du lærte

- en figur har en plass på skjermen
- `x` beskriver venstre og høyre
- `y` beskriver ned og opp
- `if` kan lage regler for hvor spilleren får gå
- koordinater hjelper spillet å vite **hvor ting er**

**Neste oppdrag:** Vi legger en stjerne på skjermen. Klarer du å fange den?
