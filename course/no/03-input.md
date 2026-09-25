# 03 – Snakk med datamaskinen

## 🎯 Oppdrag

Lag et program som stiller et spørsmål og bruker svaret.

## 💻 Kode

```python
navn = input("Hva skal figuren hete? ")
print("Hei", navn + "!")
```

## ▶ Kjør

Lagre programmet og kjør det. Skriv et navn eller kallenavn når Python spør.

`input()` venter på et svar. Svaret lagres her i variabelen `navn`.

## 🔧 Endre

Bytt spørsmålet til noe annet, for eksempel favorittdyr:

```python
dyr = input("Hva er favorittdyret til figuren? ")
print("Kult valg:", dyr)
```

## 🤔 Tenk

Hva tror du `input()` gjør? Hvor blir svaret lagret?

## ⭐ Utfordring

Få programmet til å stille tre spørsmål og skrive en liten presentasjon til slutt.

Bruk gjerne en oppdiktet figur. Du trenger ikke skrive ekte personopplysninger for å løse oppgaven.

Se [ekstra øvelser](../../exercises/no/03-input.md) når du vil prøve mer.

## 🐞 Bug-jakt

Hva mangler her?

```python
navn = input("Hva skal figuren hete? "
print("Hei", navn)
```

Tips: Se på parentesene.

## 🧠 Det du lærte

- `input()` lar programmet vente på et svar.
- Svaret kan lagres i en variabel.
- Programmet kan bruke svaret senere.
- Du kan bruke oppdiktede data når ekte informasjon ikke er nødvendig.
