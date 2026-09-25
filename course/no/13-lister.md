# 13 – Samle ting i lister

## 🎯 Oppdrag

Lag en ryggsekk som kan inneholde flere ting.

## 💻 Kode

```python
ryggsekk = ["kart", "lykt", "eple"]

print(ryggsekk)
print("Første ting:", ryggsekk[0])
```

En liste kan lagre mange verdier. Python begynner å telle plassene fra 0.

## ➕ Legg til noe

```python
ryggsekk.append("nøkkel")
print(ryggsekk)
```

## 🔁 Se på alt

```python
for ting in ryggsekk:
    print("Du har:", ting)
```

## 🔧 Endre

Lag din egen liste med fem favoritting.

## 🤔 Tenk

Hvorfor er første plass nummer 0 og ikke 1? Hva tror du `ryggsekk[1]` gir?

## ⭐ Utfordring

Lag et lite spillinventar. La spilleren finne en skatt og legg den til med `.append()`.

## 🐞 Bug-jakt

```python
dyr = ["hund", "katt"]
print(dyr[2])
```

Listen har to ting, men hvilke plassnummer har de?
