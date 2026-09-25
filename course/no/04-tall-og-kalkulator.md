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

Hva tror du skjer hvis du skriver et ord når programmet ber om et tall?

Prøv hvis du vil. Feilmeldingen er et spor som forteller at `int()` ikke kunne lage et heltall av teksten.

## ⭐ Utfordring

Lag en kalkulator som skriver både summen, differansen og produktet av to tall.

Se [ekstra øvelser](../../exercises/no/04-tall-og-kalkulator.md) når du vil prøve mer.

## 🐞 Bug-jakt

Hvorfor blir dette `23` i stedet for `5` når du skriver 2 og 3?

```python
a = input("Tall 1: ")
b = input("Tall 2: ")
print(a + b)
```

## 🧠 Det du lærte

- Python kan regne med tall.
- `input()` gir tekst.
- `int()` kan gjøre tekst som `"12"` om til heltallet `12`.
- Feilmeldinger kan hjelpe deg å finne ut hva programmet ikke forstod.
