# M3.4 – Poeng! 🏆

## 🎯 Oppdrag

Du kan fange stjernen. Men hvor mange har du fanget?

Nå skal spillet **huske poengene dine** og vise dem på skjermen.

## 🧠 Et tall spillet husker

Start med:

```python
poeng = 0
```

Du kjenner allerede variabler. Her bruker vi en variabel som spillets hukommelse.

Når du fanger stjernen, skal tallet øke.

## 🏆 Lag en poengtavle

Lag en egen Turtle som bare skriver tekst:

```python
tavle = turtle.Turtle()
tavle.hideturtle()
tavle.penup()
tavle.goto(0, 160)
```

Så lager vi en liten funksjon:

```python
def vis_poeng():
    tavle.clear()
    tavle.write(
        f"Poeng: {poeng}",
        align="center",
        font=("Arial", 18, "normal")
    )
```

Kall `vis_poeng()` én gang før spillet starter.

Nå står det **Poeng: 0** på skjermen.

## ⭐ Få poeng når du fanger stjernen

Endre fangstfunksjonen:

```python
def sjekk_fangst():
    global poeng

    if spiller.distance(stjerne) < 25:
        poeng = poeng + 1
        vis_poeng()
        flytt_stjerne()
```

Kjør spillet og fang stjernen.

**1! 2! 3!**

Spillet husker hva du har gjort.

## 🔍 Hva skjer?

Denne linjen:

```python
poeng = poeng + 1
```

betyr: ta poengtallet du har nå, legg til én, og husk det nye tallet.

Du trenger ikke lære ordet `global` utenat. Det forteller bare funksjonen at vi vil endre den samme `poeng`-variabelen som spillet bruker utenfor funksjonen.

## 🔧 Endre

Hva om hver stjerne er verdt 5 poeng?

Prøv:

```python
poeng = poeng + 5
```

Hva med 10?

Bestem poengregelen i ditt spill.

## ⭐ Utfordring

Kan du få skjermen til å skrive noe spesielt når du når 10 poeng?

```python
if poeng == 10:
    print("SUPERSPILLER!")
```

Kan du finne på din egen melding?

## 🌟 Ekstra utfordring

Lag en rekord du prøver å slå. Du trenger ikke lagre rekorden når programmet lukkes ennå. Bare bestem et mål, for eksempel:

```python
maal = 15
```

Kan spillet fortelle deg når du når målet?

## 🤔 Tenk

- Hvorfor starter `poeng` på 0?
- Når skal poengtallet endres?
- Hva skjer hvis du glemmer `tavle.clear()`?
- Er flere poeng alltid bedre, eller kan et spill ha andre mål?

## 🐞 Bug-jakt

Hvis poengtallet ikke endrer seg:

1. sjekk at `poeng = poeng + 1` ligger inne i fangsten
2. sjekk at `vis_poeng()` kjøres etter at poenget øker
3. bruk `print(poeng)` for å se hva spillet husker

Hvis flere poengtall blir skrevet oppå hverandre, sjekk at `tavle.clear()` finnes i `vis_poeng()`.

## 🧠 Det du lærte

- en variabel kan være spillets hukommelse
- spillet kan endre poeng når noe skjer
- tekst på skjermen kan vise spilleren hva som skjer
- funksjoner kan holde poengtavlen ryddig

**Neste oppdrag:** Det kommer et monster. Ikke la det ta deg! 👾
