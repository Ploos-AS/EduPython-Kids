# 06 – Tilfeldighet og terninger

## 🎯 Oppdrag

Lag en digital terning som gir et tilfeldig resultat hver gang du kjører programmet.

## 💻 Kode

```python
import random

kast = random.randint(1, 6)
print("Du kastet", kast)
```

`random` er en modul med verktøy for tilfeldighet.

`random.randint(1, 6)` velger et tilfeldig heltall fra og med 1 til og med 6.

## 🔧 Endre

Lag en 20-sidet terning ved å endre 6 til 20.

## 🤔 Tenk

Kan du vite nøyaktig hvilket tall programmet velger før du kjører det?

Du kan ikke vite det nøyaktige kastet, men du vet hvilke verdier som er mulige.

Hvorfor kan tilfeldighet være nyttig i spill?

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

Se [ekstra øvelser](../../exercises/no/06-tilfeldighet.md) når du vil prøve mer.

## 🐞 Bug-jakt

```python
import random
kast = random.randint(1, 6
print(kast)
```

Finn feilen før du kjører programmet.

## 🧠 Det du lærte

- `import` kan hente inn flere Python-verktøy.
- `random` gir oss verktøy for tilfeldighet.
- `randint()` kan velge et tilfeldig heltall i et bestemt område.
- Et tilfeldig resultat kan være ukjent selv om de mulige resultatene er kjente.
