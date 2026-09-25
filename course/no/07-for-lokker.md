# 07 – Gjør det flere ganger med for

## 🎯 Oppdrag

Få Python til å gjøre en jobb flere ganger uten å skrive samme kode om igjen.

## 💻 Kode

```python
for nummer in range(5):
    print("Runde", nummer)
```

En løkke gjentar kode. Koden som hører til løkken har innrykk.

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

Hvorfor bruker vi `runde + 1` i utskriften?

## ⭐ Utfordring

Lag et program som kaster en terning 10 ganger og teller hvor mange seksere du får.

## 🐞 Bug-jakt

```python
for i in range(5):
print(i)
```

Python bryr seg om innrykk. Kan du reparere programmet?
