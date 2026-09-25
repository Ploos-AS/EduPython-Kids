# 12 – Prosjekt: Monsterkamp

## 🎯 Oppdrag

Bygg et lite tekstspill der du møter et monster.

Nå skal flere av Python-verktøyene du har lært samarbeide i ett program.

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
- variabler og spilltilstand
- `input()`
- `while`
- `if`
- funksjoner og `return`
- regning

`spiller_liv` og `monster_liv` er spilltilstand: verdier som endres mens spillet pågår.

`break` stopper løkken med én gang. Her bruker vi den når monsteret ikke har flere liv igjen.

## 🔧 Endre

Begynn med én liten endring. Prøv for eksempel å gi monsteret mer eller mindre liv.

Kjør spillet flere ganger før du endrer noe mer.

## 🤔 Tenk

Hva tror du skjer med vanskelighetsgraden hvis monsteret starter med 20 liv?

Hva skjer hvis `kast()` bruker `random.randint(1, 10)`?

## ⭐ Gjør spillet ditt

Velg minst to forbedringer:

- Gi monsteret et navn.
- La spilleren velge et kallenavn.
- Lag forskjellige monstre.
- Legg til helsedrikk.
- La spilleren velge mellom angrep og forsvar.
- Lag kritiske treff når terningen viser 6.
- Lag en ny funksjon for monsterets angrep.

Se [ekstra øvelser](../../exercises/no/12-monsterkamp.md) når du vil bygge videre.

## 🧪 Spilltester

Spill minst tre ganger.

Skriv ned:

1. én bug eller overraskelse du oppdaget
2. én regel du endret
3. hva endringen gjorde med spillet

Du er ikke bare spiller nå. Du tester og utvikler ditt eget spill.

## 🧠 Det du lærte

- Et større program kan bygges av små konsepter du allerede kjenner.
- Spilltilstand endres mens spillet kjører.
- Funksjoner kan gjøre deler av programmet enklere å gjenbruke.
- Testing hjelper deg å oppdage både bugs og regler du vil forbedre.
- Det er ofte enklere å forbedre én liten del om gangen.
