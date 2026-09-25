# 11 – Lag egne kommandoer med funksjoner

## 🎯 Oppdrag

Lag en navngitt oppgave som programmet kan bruke flere ganger.

En slik navngitt oppgave kalles en **funksjon**.

## 💻 Kode

```python
def hils():
    print("Hei!")
    print("Velkommen til spillet.")

hils()
hils()
```

`def` lager funksjonen. Koden inni funksjonen kjører når vi **kaller** funksjonen.

## 🎁 Send inn informasjon

```python
def hils(navn):
    print("Hei", navn + "!")

hils("Ada")
hils("Ola")
```

`navn` er en **parameter**. Den lar samme funksjon arbeide med forskjellige verdier.

## 🔙 Få en verdi tilbake

```python
def dobbel(tall):
    return tall * 2

svar = dobbel(7)
print(svar)
```

`return` sender en verdi tilbake fra funksjonen.

Det er forskjell på `print()` og `return`: `print()` viser noe på skjermen, mens en verdi fra `return` kan lagres eller brukes videre i programmet.

## 🔧 Endre

Lag funksjonen `trippel(tall)`.

## 🤔 Tenk

Hva tror du skjer her?

```python
resultat = dobbel(5) + dobbel(2)
print(resultat)
```

Hvorfor kan vi regne videre med verdiene fra `dobbel()`?

## ⭐ Utfordring

Lag en funksjon `kast_terning()` som returnerer et tilfeldig tall fra 1 til 6.

Se [ekstra øvelser](../../exercises/no/11-funksjoner.md) når du vil prøve mer.

## 🐞 Bug-jakt

```python
def hils()
    print("Hei!")

hils()
```

Hva mangler på første linje?

## 🧠 Det du lærte

- En funksjon samler kode under et navn.
- En funksjon kan kalles flere ganger.
- Parametere gjør funksjoner fleksible.
- `return` sender en verdi tilbake.
- `print()` og `return` har forskjellige jobber.
