# 13 – Samle ting i lister

## 🎯 Oppdrag

Lag en ryggsekk som kan inneholde flere ting.

## 💻 Kode

```python
ryggsekk = ["kart", "lykt", "eple"]

print(ryggsekk)
print("Første ting:", ryggsekk[0])
```

En **liste** samler flere verdier på ett sted.

Hver plass i listen har et nummer som kalles en **indeks**. Python begynner å telle indeksene fra 0.

I denne listen er:

- `ryggsekk[0]` → `"kart"`
- `ryggsekk[1]` → `"lykt"`
- `ryggsekk[2]` → `"eple"`

## ➕ Legg til noe

```python
ryggsekk.append("nøkkel")
print(ryggsekk)
```

`.append()` legger en ny verdi bakerst i listen.

## 🔁 Se på alt

```python
for ting in ryggsekk:
    print("Du har:", ting)
```

Her går `for`-løkken gjennom én ting om gangen. Vi trenger ikke vite hvor lang listen er.

## 🔧 Endre

Lag din egen liste med fem ting til en oppdiktet eventyrer.

## 🤔 Tenk

Hva tror du `ryggsekk[1]` gir?

Hva tror du skjer hvis du prøver `ryggsekk[99]`?

## ⭐ Utfordring

Lag et lite spillinventar. La spilleren finne en skatt og legg den til med `.append()`.

Se [ekstra øvelser](../../exercises/no/13-lister.md) når du vil prøve mer.

## 🐞 Bug-jakt

```python
dyr = ["hund", "katt"]
print(dyr[2])
```

Listen har to ting. Hvilke indekser finnes?

Les feilmeldingen når du kjører programmet. Kan den hjelpe deg?

## 🧠 Det du lærte

- En liste kan samle flere verdier.
- Hver plass har en indeks.
- Python starter listeindekser på 0.
- `.append()` legger til en verdi.
- En `for`-løkke kan gå gjennom verdiene i en liste.
