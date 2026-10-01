# M3.7 – Gjør spillet ditt! 🎨

## 🎯 Oppdrag

Spillet virker. Nå skal det slutte å være **vårt** spill og begynne å bli **ditt**.

Du bestemmer tema, figurer, fart og noen av reglene.

## 🎭 Velg et tema

Hva handler spillet ditt om?

Eksempler:

- en rompilot samler energi og unngår et rommonster
- en katt samler mat og unngår en robot
- en ridder samler skatter og unngår en drage
- en skilpadde samler kaker og unngår ... en veldig sulten firkant

Eller finn på noe helt annet.

Skriv én setning:

**Mitt spill handler om ____________________.**

## 🎨 Endre figurene

Turtle har flere innebygde former:

```python
spiller.shape("turtle")
stjerne.shape("circle")
monster.shape("square")
```

Prøv også `"triangle"` eller `"arrow"`.

Du kan endre størrelse:

```python
monster.shapesize(1.5)
```

Og farge:

```python
spiller.color("blue")
stjerne.color("gold")
monster.color("red")
```

Velg selv. Det finnes ikke én riktig kombinasjon.

## 🌌 Endre verden

Bakgrunnen kan også være en del av temaet:

```python
skjerm.bgcolor("lightblue")
```

Prøv en annen farge.

Kan du gi spillet et nytt navn?

```python
skjerm.title("Mitt superspill")
```

## 🎮 Finn riktig spillfølelse

Du har flere tall som forandrer spillet:

```python
STEG = 20
monsterfart = 8
liv = 3
```

Endre **ett tall om gangen** og spill litt.

Spør deg selv:

- Er spilleren for treg?
- Er monsteret for raskt?
- Har jeg for mange eller for få liv?
- Er det morsomt å samle målet?

Et godt spill trenger ikke være vanskeligst mulig.

## 📜 Lag din egen regel

Velg minst én regel du vil forandre.

Du kan for eksempel bestemme:

- målet gir 2 poeng
- monsteret blir raskere ved 5 poeng
- spilleren får et ekstra liv ved 10 poeng
- målet dukker opp i et mindre område
- spillet er vunnet ved 15 poeng

Velg én idé først. Få den til å virke før du lager flere.

## 🏁 Eksempel: vinn ved 10 poeng

Etter at poenget øker kan du teste:

```python
if poeng == 10:
    print("DU VANT!")
```

Hva skal skje i **ditt** spill når spilleren vinner?

## 🧪 Spilltest

La en annen person prøve spillet uten at du styrer for dem.

Se på mens de spiller.

Etterpå spør du:

- Var det lett å forstå hva du skulle gjøre?
- Var monsteret for lett eller for vanskelig?
- Var det morsomt?
- Hva ville du endret?

Du bestemmer hvilke råd du vil bruke.

## ⭐ Utfordring

Gjør **tre ting** som gjør spillet tydelig til ditt eget:

1. endre utseendet
2. endre én spillregel
3. gi spillet et eget navn

Vis det til noen og fortell hvilken endring du liker best.

## 🌟 Ekstra utfordring

Lag to forskjellige versjoner:

- **rolig**
- **turbo**

Hvilke tall må endres for at de skal føles forskjellige?

## 🐞 Bug-jakt

Når du lager mange endringer samtidig, kan det bli vanskelig å finne ut hva som gikk galt.

Bruk denne regelen:

**Endre → kjør → test → behold eller angre.**

Én liten endring om gangen.

## 🧠 Det du lærte

- de samme Python-byggesteinene kan lage mange forskjellige spill
- tall og regler bestemmer hvordan et spill føles
- testing med andre kan gi nye ideer
- kode er noe du kan forme, eksperimentere med og gjøre til ditt eget

**Neste oppdrag:** Kan spillet gi deg et lite jubel-signal når du fanger noe? 🔔
