# M3.5 – Pass deg for monsteret! 👾

## 🎯 Oppdrag

Du samler stjerner og får poeng. Nå kommer et monster!

Monsteret prøver å komme nærmere deg. Klarer du å samle stjerner uten å bli tatt?

## 👾 Lag monsteret

Etter at du har laget spilleren og stjernen, legg til:

```python
monster = turtle.Turtle()
monster.shape("square")
monster.penup()
monster.goto(-200, -100)
```

Kjør programmet. Nå står monsteret der, men det gjør ingenting ennå.

## 👣 La monsteret gå

Vi lager en funksjon som flytter monsteret litt mot spilleren:

```python
def flytt_monster():
    monster.setheading(monster.towards(spiller))
    monster.forward(8)

    skjerm.ontimer(flytt_monster, 100)
```

Start monsteret én gang før `turtle.done()`:

```python
flytt_monster()
```

Kjør spillet.

**Nå følger monsteret etter deg!**

## 💥 Tok monsteret deg?

Etter at monsteret har flyttet, kan vi spørre hvor nær det er:

```python
if monster.distance(spiller) < 25:
    print("Monsteret tok deg!")
```

Legg testen inn i `flytt_monster()` før `ontimer()`.

Prøv å bli tatt med vilje.

## 🔧 Endre

Finn denne linjen:

```python
monster.forward(8)
```

Prøv `3`. Er monsteret lettere å rømme fra?

Prøv `15`. Hva skjer nå?

Velg en fart som er morsom, ikke bare vanskelig.

## ⏱ Et nytt lite triks

Denne linjen:

```python
skjerm.ontimer(flytt_monster, 100)
```

ber Turtle kjøre funksjonen igjen litt senere.

Det er derfor monsteret fortsetter å bevege seg selv om du ikke trykker en tast.

Du trenger ikke kunne alt om tidtaking ennå. Tenk på det som: **«Monster, ta et nytt steg om litt.»**

## ⭐ Utfordring

Hvor skal monsteret starte?

Prøv forskjellige steder med:

```python
monster.goto(-200, -100)
```

Kan du finne et startsted som gir spilleren litt tid til å komme i gang?

## 🌟 Ekstra utfordring

Når du fanger en stjerne, kan monsteret bli litt raskere.

Lag først:

```python
monsterfart = 5
```

Bruk så variabelen i stedet for tallet i:

```python
monster.forward(monsterfart)
```

Kan du øke `monsterfart` når spilleren får poeng?

Hvis dette blir vanskelig, hopp over det. Spillet fungerer fint uten.

## 🤔 Tenk

- Hvordan vet monsteret hvilken vei det skal gå?
- Hva skjer hvis monsteret går for fort?
- Hva gjør et spill spennende uten å gjøre det frustrerende?

## 🐞 Bug-jakt

Hvis monsteret bare flytter seg én gang, sjekk at `skjerm.ontimer(flytt_monster, 100)` ligger inne i funksjonen.

Hvis monsteret ikke starter, sjekk at du kaller `flytt_monster()` én gang før `turtle.done()`.

Hvis monsteret ser ut til å treffe deg uten å være nær, prøv å gjøre `25` mindre.

## 🧠 Det du lærte

- en figur kan bevege seg uten tastetrykk
- `towards()` kan peke en figur mot en annen
- spillet kan sjekke om monsteret er nær spilleren
- fart kan gjøre et spill lettere eller vanskeligere

**Neste oppdrag:** Monsteret tok deg — men spillet er ikke over ennå. Du får tre liv! ❤️❤️❤️
