# 12 – Prosjekt: Monsterkamp

## 🎯 Oppdrag

Bygg et lite tekstspill der du møter et monster.

Dette prosjektet bruker mange av verktøyene du allerede har lært.

## 💻 Spillet

```python
import random

def kast():
    return random.randint(1, 6)

spiller_liv = 10
monster_liv = 10

print("Et monster dukker opp!")

while spiller_liv > 0 and monster_liv > 0:
    input("Trykk Enter for å angripe...")

    skade = kast()
    monster_liv = monster_liv - skade
    print("Du gjør", skade, "skade.")

    if monster_liv <= 0:
        break

    skade = kast()
    spiller_liv = spiller_liv - skade
    print("Monsteret gjør", skade, "skade.")
    print("Dine liv:", spiller_liv, "| Monsterets liv:", monster_liv)

if spiller_liv > 0:
    print("Du vant! 🎉")
else:
    print("Monsteret vant denne gangen.")
```

## 🧰 Hva bruker vi?

- `random`
- variabler
- `input()`
- `while`
- `if`
- funksjoner
- regning

## ⭐ Gjør spillet ditt

Velg minst to forbedringer:

- Gi monsteret et navn.
- La spilleren velge navn.
- Lag forskjellige monstre.
- Legg til helsedrikk.
- La spilleren velge mellom angrep og forsvar.
- Lag kritiske treff når terningen viser 6.
- Lag en ny funksjon for monsterets angrep.

## 🧪 Spilltester

Spill minst tre ganger. Skriv ned én ting som var morsom og én ting du vil forbedre.

Du er ikke bare en spiller nå. Du er spillutvikleren.
