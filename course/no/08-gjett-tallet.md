# 08 – Minispill: Gjett tallet

## 🎯 Oppdrag

Nå kombinerer vi det du har lært og lager et ekte lite spill.

Datamaskinen velger et hemmelig tall fra 1 til 10. Du skal prøve å gjette det.

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

Her bruker vi allerede fire ting du kjenner:

- variabler
- `input()`
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

`elif` betyr omtrent «ellers, hvis ...».

## 🤔 Tenk

Hvordan kunne vi gitt spilleren flere forsøk? Det kommer vi tilbake til når vi lærer `while`.

## ⭐ Utfordring

Endre området til 1–20. Lag din egen melding når spilleren vinner.

Ekstra: Gi spilleren poeng hvis svaret er riktig.

## 🐞 Bug-jakt

Hva er forskjellen på disse?

```python
gjett = hemmelig
gjett == hemmelig
```

Den første lagrer en verdi. Den andre spør om verdiene er like.
