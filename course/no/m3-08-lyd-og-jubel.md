# M3.8 – Lyd og jubel! 🔔

## 🎯 Oppdrag

Når du fanger målet, skal spillet **feire**.

Vi starter med noe som virker uten lyd: målet blinker. Deretter kan vi prøve et lite lydsignal hvis maskinen støtter det.

## ✨ La målet blinke

Lag denne funksjonen:

```python
def jubel():
    gammel_farge = stjerne.color()[0]
    stjerne.color("yellow")

    def ferdig():
        stjerne.color(gammel_farge)

    skjerm.ontimer(ferdig, 150)
```

Kall `jubel()` når spilleren fanger målet:

```python
if spiller.distance(stjerne) < 25:
    poeng = poeng + 1
    vis_poeng()
    jubel()
    flytt_stjerne()
```

Fang målet. Nå får du et lite blink som sier: **Ja! Du fikk den!**

## 🔔 Valgfri lyd

Noen datamaskiner kan også lage et enkelt signal med Turtle-vinduet:

```python
def pip():
    try:
        skjerm.getcanvas().bell()
    except Exception:
        pass
```

Legg `pip()` inn i `jubel()` hvis du vil prøve.

Hvis du ikke hører noe, er det helt greit. Spillet skal virke like godt uten lyd.

## 🧠 Hvorfor er lyd valgfritt?

Datamaskiner er forskjellige. Noen har lyd slått av. Noen miljøer spiller ikke dette signalet. Noen elever vil heller spille uten lyd.

Derfor bruker vi lyd som **ekstra feedback**, ikke som noe du må høre for å kunne spille.

## 🔧 Endre

Prøv å endre tiden:

```python
skjerm.ontimer(ferdig, 300)
```

Hvordan føles et lengre blink?

Prøv en annen jubelfarge.

## 🎉 Feir noe større

Kanskje vanlig fangst bare skal blinke, mens 10 poeng skal få en større feiring.

Du kan for eksempel skrive:

```python
if poeng == 10:
    tavle.goto(0, 0)
    tavle.write(
        "SUPER!",
        align="center",
        font=("Arial", 28, "bold")
    )
```

Finn på din egen melding.

## ⭐ Utfordring

Lag to forskjellige signaler:

- ett når du fanger målet
- ett når monsteret tar deg

Signalene kan være farge, tekst, lyd eller en kombinasjon.

Kan spilleren forstå hva som skjedde selv med lyden avslått?

## 🌟 Ekstra utfordring

Lag en liten feiring når spilleren vinner. Kanskje bakgrunnen skifter farge, figuren snurrer eller teksten sier noe morsomt.

Bruk ting du allerede kan.

## 🤔 Tenk

- Hvorfor er det fint at spillet reagerer med én gang?
- Trenger et spill lyd for å være morsomt?
- Kan en spiller forstå signalene dine uten å høre dem?

## 🐞 Bug-jakt

Hvis blinket ikke forsvinner, sjekk at `skjerm.ontimer(ferdig, 150)` finnes.

Hvis lyden ikke virker, fortsett uten den. Det er ikke en feil som stopper oppdraget.

Hvis jubelteksten dekker poengene, bruk en annen Turtle til stor melding eller flytt teksten til et annet sted.

## 🧠 Det du lærte

- et spill kan gi tydelig feedback når noe skjer
- visuelle signaler virker også uten lyd
- lyd kan være en valgfri bonus
- små detaljer kan gjøre et spill morsommere å spille

**Neste oppdrag:** Nå bygger vi delene sammen til et helt mini-spill! 🎮
