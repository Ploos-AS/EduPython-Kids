# 09 – Fortsett med while

## 🎯 Oppdrag

Få et program til å fortsette helt til noe bestemt skjer.

## 💻 Kode

```python
svar = ""

while svar != "ja":
    svar = input("Er du klar? ")

print("Da begynner vi!")
```

`while` betyr «så lenge». Løkken kjører så lenge testen er sann.

## 🔧 Endre

Lag et passordprogram som fortsetter å spørre til riktig passord blir skrevet.

## 🔢 Tell med while

```python
tall = 1

while tall <= 5:
    print(tall)
    tall = tall + 1
```

## 🤔 Tenk

Hva skjer hvis vi glemmer `tall = tall + 1`? Da kan løkken fortsette for alltid. Du kan stoppe et program som har satt seg fast med Ctrl+C i en terminal.

## ⭐ Utfordring

Lag en nedtelling fra 10 til 1 og skriv «START!» til slutt.

## 🐞 Bug-jakt

```python
tall = 1
while tall <= 5:
    print(tall)
```

Hvorfor stopper ikke programmet?
