# 14 – Tegn med Turtle

## 🎯 Oppdrag

Få en liten skilpadde til å tegne en firkant på skjermen.

Turtle følger med Python på mange vanlige installasjoner. Den trenger et grafisk miljø med Tk-støtte.

## 💻 Første tegning

```python
import turtle

penn = turtle.Turtle()

for side in range(4):
    penn.forward(100)
    penn.right(90)

turtle.done()
```

## 🔧 Endre

Hva skjer hvis du endrer 100? Hva skjer hvis du endrer 90?

## 🔺 Tegn en trekant

```python
for side in range(3):
    penn.forward(120)
    penn.right(120)
```

## 🤔 Tenk

En hel runde er 360 grader. For en figur med like store svinger kan vi prøve:

```text
sving = 360 / antall_sider
```

Kan du bruke ideen til å tegne en femkant?

## ⭐ Utfordring

Lag en funksjon `polygon(sider, lengde)` som kan tegne flere forskjellige figurer.

## 🎨 Gjør den din

Prøv forskjellige pennstørrelser og farger. Eksperimenter er en del av oppgaven.
