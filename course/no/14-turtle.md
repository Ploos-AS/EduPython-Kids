# 14 – Tegn med Turtle

## 🎯 Oppdrag

Få en liten skilpadde til å tegne en firkant på skjermen.

Turtle følger med mange Python-installasjoner og trenger et grafisk miljø med Tk-støtte.

## 💻 Første tegning

```python
import turtle

penn = turtle.Turtle()

for side in range(4):
    penn.forward(100)
    penn.right(90)

turtle.done()
```

Her bruker du allerede en løkke. I stedet for fire nesten like kodeblokker gjentar programmet de samme to bevegelsene fire ganger.

## 🔧 Endre

Hva tror du skjer hvis du endrer 100?

Prøv.

Hva tror du skjer hvis du endrer 90?

Prøv igjen.

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

Lag en funksjon:

```python
def polygon(sider, lengde):
    ...
```

Den skal kunne tegne flere forskjellige mangekanter.

Se [ekstra øvelser](../../exercises/no/14-turtle.md) når du vil prøve mer.

## 🎨 Gjør den din

Eksperimenter med pennstørrelse, farger, lengder og vinkler.

Det finnes ikke én riktig tegning.

## 🐞 Bug-jakt

Hvis Turtle-vinduet ikke åpner i det hele tatt, kan problemet være Python/Tk-miljøet og ikke koden din. Be en voksen sjekke [installasjonsguiden](../../docs/INSTALL.md).

Hvis vinduet åpner, men figuren ser rar ut, test én verdi om gangen.

## 🧠 Det du lærte

- Kode kan styre grafikk og bevegelse.
- Løkker er nyttige når en figur har gjentatte sider.
- Vinkler endrer retningen pennen beveger seg i.
- Funksjoner kan gjøre tegnekode gjenbrukbar.
