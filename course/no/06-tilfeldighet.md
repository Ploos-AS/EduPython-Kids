# 06 – Tilfeldighet og terninger

## 🎯 Oppdrag

Lag en digital terning som gir et nytt resultat hver gang du kjører programmet.

## 💻 Kode

```python
import random

kast = random.randint(1, 6)
print("Du kastet", kast)
```

`random.randint(1, 6)` velger et helt tall fra 1 til 6.

## 🔧 Endre

Lag en 20-sidet terning ved å endre tallet 6 til 20.

## 🤔 Tenk

Kan du vite på forhånd hvilket tall programmet velger? Hvorfor er tilfeldighet nyttig i spill?

## ⭐ Utfordring

Kast to terninger og skriv summen.

```python
import random

a = random.randint(1, 6)
b = random.randint(1, 6)

print("Terningene:", a, "og", b)
print("Sum:", a + b)
```

Ekstra utfordring: Skriv «Dobbel!» når begge terningene viser samme tall.

## 🐞 Bug-jakt

```python
import random
kast = random.randint(1, 6
print(kast)
```

Finn feilen før du kjører programmet.
