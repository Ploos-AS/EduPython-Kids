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

En `while`-løkke betyr omtrent «så lenge». Løkken fortsetter så lenge betingelsen er sann.

Her fortsetter den så lenge `svar` **ikke** er lik `"ja"`.

## 🔧 Endre

Lag et program som spør etter et oppdiktet kodeord helt til riktig ord blir skrevet.

Bruk aldri et ekte passord du bruker andre steder.

## 🔢 Tell med while

```python
tall = 1

while tall <= 5:
    print(tall)
    tall = tall + 1
```

Her endres `tall` hver runde. Til slutt blir betingelsen usann, og løkken stopper.

## 🤔 Tenk

Hva tror du skjer hvis vi glemmer `tall = tall + 1`?

Da endres aldri verdien som skal få betingelsen til å bli usann. Løkken kan fortsette for alltid.

I en terminal kan du vanligvis stoppe et slikt program med Ctrl+C.

## ⭐ Utfordring

Lag en nedtelling fra 10 til 1 og skriv «START!» til slutt.

Se [ekstra øvelser](../../exercises/no/09-while.md) når du vil prøve mer.

## 🐞 Bug-jakt

```python
tall = 1

while tall <= 5:
    print(tall)
```

Hvorfor stopper ikke programmet? Hvilken verdi må endres?

## 🧠 Det du lærte

- `while` gjentar kode så lenge en betingelse er sann.
- Noe må vanligvis endres slik at løkken kan stoppe.
- En løkke som aldri stopper kalles ofte en uendelig løkke.
- `for` passer ofte når antallet repetisjoner er kjent; `while` passer når vi venter på at noe skal skje.
