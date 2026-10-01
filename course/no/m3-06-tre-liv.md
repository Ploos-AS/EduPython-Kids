# M3.6 – Tre liv! ❤️❤️❤️

## 🎯 Oppdrag

Monsteret tok deg! Men spillet er ikke over ennå.

Du får **tre liv**. Hver gang monsteret tar deg, mister du ett.

## ❤️ Spillet husker livene

Sammen med `poeng` lager du:

```python
liv = 3
```

Lag en liten tavle for liv:

```python
livtavle = turtle.Turtle()
livtavle.hideturtle()
livtavle.penup()
livtavle.goto(-250, 160)
```

Og en funksjon som viser dem:

```python
def vis_liv():
    livtavle.clear()
    livtavle.write(f"Liv: {liv}", font=("Arial", 18, "normal"))
```

Kall `vis_liv()` én gang når spillet starter.

## 💥 Når monsteret tar deg

Lag en egen funksjon:

```python
def tatt_av_monster():
    global liv

    liv = liv - 1
    vis_liv()

    spiller.goto(0, 0)
    monster.goto(-200, -100)
```

I monsterfunksjonen kan du nå bruke:

```python
if monster.distance(spiller) < 25:
    tatt_av_monster()
```

Prøv å bli tatt med vilje.

**3 → 2 → 1 ...**

## 🛑 Når livene er brukt opp

Vi trenger én regel til:

```python
def tatt_av_monster():
    global liv

    liv = liv - 1
    vis_liv()

    if liv == 0:
        game_over()
    else:
        spiller.goto(0, 0)
        monster.goto(-200, -100)
```

Så lager vi `game_over()`:

```python
def game_over():
    monster.hideturtle()
    spiller.hideturtle()
    stjerne.hideturtle()

    tavle.goto(0, 0)
    tavle.clear()
    tavle.write(
        "GAME OVER",
        align="center",
        font=("Arial", 28, "bold")
    )
```

Nå har spillet en slutt.

## ⚠️ Stopp monsteret også

Vi vil ikke at et usynlig monster skal fortsette å jage.

Lag:

```python
spillet_er_i_gang = True
```

I `game_over()`:

```python
global spillet_er_i_gang
spillet_er_i_gang = False
```

Og øverst i `flytt_monster()`:

```python
if not spillet_er_i_gang:
    return
```

Det betyr omtrent: **Hvis spillet er slutt, stopp her.**

## 🔧 Endre

Tre liv er bare vår regel.

Prøv:

```python
liv = 5
```

Eller gjør spillet ekstra vanskelig med bare ett liv.

Hvilken regel er morsomst?

## ⭐ Utfordring – spill igjen

Kan du lage en funksjon som starter på nytt?

Her er byggeklossene du trenger:

```python
liv = 3
poeng = 0
spillet_er_i_gang = True

spiller.showturtle()
monster.showturtle()
stjerne.showturtle()

spiller.goto(0, 0)
monster.goto(-200, -100)

vis_liv()
vis_poeng()
```

Prøv først å samle dem i:

```python
def start_pa_nytt():
    ...
```

Når den virker, kan du koble den til `r`:

```python
skjerm.onkey(start_pa_nytt, "r")
```

Hvis restart blir vanskelig, er det helt greit å lukke spillet og kjøre det på nytt. Restart er utfordringen, ikke hovedoppdraget.

## 🤔 Tenk

- Hvorfor flytter vi figurene fra hverandre etter et treff?
- Hva skjer når `liv` blir 0?
- Hvorfor trenger spillet å huske om det fortsatt er i gang?
- Hvor mange liv gjør ditt spill morsomst?

## 🐞 Bug-jakt

Hvis du mister flere liv nesten samtidig, flytt spilleren og monsteret langt nok fra hverandre etter treffet.

Hvis monsteret fortsetter etter GAME OVER, sjekk `spillet_er_i_gang` og testen øverst i `flytt_monster()`.

Hvis restart ikke virker ennå, behold resten av spillet. Restart er ekstra.

## 🧠 Det du lærte

- variabler kan huske både poeng og liv
- et spill kan ha regler for treff og tap
- samme spill kan være i gang eller ferdig
- funksjoner kan samle det som skal skje ved treff og GAME OVER

**Neste oppdrag:** Nå skal spillet bli ditt — farger, figurer, fart og egne regler! 🎨
