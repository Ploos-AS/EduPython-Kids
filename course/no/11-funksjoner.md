# 11 – Lag dine egne kommandoer med funksjoner

## 🎯 Oppdrag

Lag en egen Python-kommando som du kan bruke flere ganger.

## 💻 Kode

```python
def hils():
    print("Hei!")
    print("Velkommen til spillet.")

hils()
hils()
```

`def` lager en funksjon. Koden inni funksjonen kjører når vi kaller funksjonen.

## 🎁 Send inn informasjon

```python
def hils(navn):
    print("Hei", navn + "!")

hils("Ada")
hils("Ola")
```

`navn` er informasjon funksjonen får når den blir kalt.

## 🔙 Få et svar tilbake

```python
def dobbel(tall):
    return tall * 2

svar = dobbel(7)
print(svar)
```

`return` sender et resultat tilbake.

## 🔧 Endre

Lag funksjonen `trippel(tall)`.

## ⭐ Utfordring

Lag en funksjon `kast_terning()` som returnerer et tilfeldig tall fra 1 til 6.

## 🐞 Bug-jakt

```python
def hils()
    print("Hei!")

hils()
```

Hva mangler på første linje?
