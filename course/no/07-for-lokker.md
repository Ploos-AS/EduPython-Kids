# 07 – Gjør det flere ganger med for

## 🎯 Oppdrag

Få Python til å gjøre en jobb flere ganger uten å skrive samme kode om igjen.

## 💻 Kode

```python
for nummer in range(5):
    print("Runde", nummer)
```

En **løkke** gjentar kode. En `for`-løkke passer godt når vi vet hvor mange repetisjoner vi vil gjøre.

Koden som hører til løkken har innrykk.

## 🔧 Endre

Hva skjer hvis du bytter `5` med `10`?

Prøv også:

```python
for nummer in range(1, 11):
    print(nummer)
```

## 🎲 Fem terningkast

```python
import random

for runde in range(5):
    kast = random.randint(1, 6)
    print("Kast", runde + 1, "ble", kast)
```

## 🤔 Tenk

Hva tror du første verdi av `runde` er?

`range(5)` gir 0, 1, 2, 3 og 4. Derfor bruker vi `runde + 1` når vi vil skrive «Kast 1» til «Kast 5».

## ⭐ Utfordring

Lag et program som kaster en terning 10 ganger og teller hvor mange seksere du får.

Se [ekstra øvelser](../../exercises/no/07-for-lokker.md) når du vil prøve mer.

## 🐞 Bug-jakt

```python
for i in range(5):
print(i)
```

Python bryr seg om innrykk. Kan du reparere programmet?

## 🧠 Det du lærte

- En løkke gjentar kode.
- `for` passer når vi vil gå gjennom et kjent antall repetisjoner eller verdier.
- `range()` lager en rekke tall som løkken kan gå gjennom.
- Python begynner ofte å telle fra 0.
- Koden inni løkken må ha riktig innrykk.
