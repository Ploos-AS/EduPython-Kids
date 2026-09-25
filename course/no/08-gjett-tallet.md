# 08 – Minispill: Gjett tallet

## 🎯 Oppdrag

Nå kombinerer vi det du har lært og lager et lite spill.

Programmet velger et hemmelig tall fra 1 til 10. Du skal prøve å gjette det.

## 💻 Første versjon

```python
import random

hemmelig = random.randint(1, 10)
gjett = int(input("Gjett et tall fra 1 til 10: "))

if gjett == hemmelig:
    print("Riktig! 🎉")
else:
    print("Ikke denne gangen.")
    print("Tallet var", hemmelig)
```

Her bruker vi allerede flere ting du kjenner:

- variabler
- `input()`
- `int()`
- tilfeldighet
- `if`

## 🔧 Gjør spillet smartere

```python
if gjett == hemmelig:
    print("Riktig! 🎉")
elif gjett < hemmelig:
    print("For lavt!")
else:
    print("For høyt!")
```

`elif` betyr omtrent «ellers, hvis ...». Bare én av disse tre veiene blir valgt.

## 🤔 Tenk

Hva tror du vi trenger for å la spilleren gjette igjen og igjen helt til svaret er riktig?

Vi har ikke lært det verktøyet ennå. I neste leksjon møter du `while`.

## ⭐ Utfordring

Endre området til 1–20. Lag din egen melding når spilleren vinner.

Ekstra: Gi spilleren poeng hvis svaret er riktig.

Se [ekstra øvelser](../../exercises/no/08-gjett-tallet.md) når du vil prøve mer.

## 🐞 Bug-jakt

Hva er forskjellen på disse?

```python
gjett = hemmelig
gjett == hemmelig
```

Den første gir `gjett` en verdi. Den andre er en betingelse som spør om verdiene er like.

## 🧠 Det du lærte

- Flere tidligere Python-verktøy kan kombineres til et spill.
- `elif` gir en ekstra betingelse mellom `if` og `else`.
- `<` og `>` kan sammenligne tall.
- Noen problemer gjør at vi trenger et nytt programmeringsverktøy.
