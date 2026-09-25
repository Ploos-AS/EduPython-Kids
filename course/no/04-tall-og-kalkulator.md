# 04 – Tall og mini-kalkulator

## 🎯 Oppdrag

Lag en kalkulator som kan legge sammen to tall.

## 💻 Først: Python kan regne

```python
print(2 + 3)
print(10 - 4)
print(3 * 5)
```

## 💻 Din kalkulator

`input()` gir oss tekst. `int()` gjør teksten om til et helt tall.

```python
a = int(input("Første tall: "))
b = int(input("Andre tall: "))

svar = a + b
print("Svaret er", svar)
```

## 🔧 Endre

Prøv `-` og `*` i stedet for `+`.

## 🤔 Tenk

Hva skjer hvis du skriver et ord når programmet ber om et tall? Feilmeldingen er et spor, ikke en katastrofe.

## ⭐ Utfordring

Lag en kalkulator som skriver både summen, differansen og produktet av to tall.

## 🐞 Bug-jakt

Hvorfor blir dette `23` i stedet for `5` når du skriver 2 og 3?

```python
a = input("Tall 1: ")
b = input("Tall 2: ")
print(a + b)
```
