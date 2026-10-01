# M3.10 – Mitt spill! 🚀

## 🎯 Det store oppdraget

Nå skal du lage **ditt eget spill**.

Du trenger ikke finne opp alt fra ingenting. Du kan bruke delene du allerede har laget, men du bestemmer hva spillet skal være.

Når du er ferdig skal du kunne si:

**Jeg lagde mitt eget spill!**

## 💡 Velg en idé

Velg én av disse, bland dem, eller finn på din egen:

- samle skatter og unngå en drage
- samle energi i verdensrommet
- hjelp et dyr å finne mat
- fang magiske ting før monsteret tar deg
- lag et helt annet spill

Skriv én setning:

**I spillet mitt skal spilleren ____________________.**

## 📜 Velg reglene

Svar kort før du begynner:

- Hva styrer spilleren?
- Hva skal spilleren samle eller gjøre?
- Hva er farlig?
- Hvordan får man poeng?
- Kan man tape?
- Kan man vinne?

Du trenger ikke mange regler. Et lite spill som virker er bedre enn et kjempespill som aldri blir ferdig.

## 🧱 Bygg i milepæler

### Milepæl 1 – Jeg kan bevege meg

Få spilleren på skjermen og få piltastene til å virke.

**Test før du går videre.**

### Milepæl 2 – Jeg kan gjøre noe

Legg inn målet: samle, fange eller nå noe.

**Test igjen.**

### Milepæl 3 – Spillet husker

Legg til poeng, liv eller noe annet spillet skal huske.

### Milepæl 4 – Det blir spennende

Legg til monsteret eller en annen utfordring.

### Milepæl 5 – Spillet har en slutt

Bestem hva som skjer når spilleren vinner eller taper.

### Milepæl 6 – Gjør det ditt

Gi spillet navn, farger og minst én egen regel.

## 🧰 Hjelpekort

Sitter du fast? Finn delen du trenger i de tidligere oppdragene eller i `examples/m3-mini-game.py`.

### Flytt en figur

```python
figur.goto(x, y)
```

### Hvor er figuren?

```python
figur.xcor()
figur.ycor()
```

### Er to ting nær hverandre?

```python
figur.distance(maal) < 25
```

### Tilfeldig sted

```python
random.randint(-250, 250)
```

### Gjør noe litt senere

```python
skjerm.ontimer(funksjon, 100)
```

Hjelpekort er ikke juks. Programmerere slår opp ting hele tiden.

## 🧪 Test som en spillmaker

Spill selv først.

Prøv også å gjøre rare ting:

- hold inne en tast
- løp rett mot kanten
- la monsteret ta deg flere ganger
- prøv å vinne
- prøv å tape

Virker reglene slik du hadde tenkt?

## 👥 La noen andre spille

Finn en testspiller.

Ikke forklar hvert tastetrykk. La personen prøve.

Spør etterpå:

- Hva trodde du at du skulle gjøre?
- Hva var morsomt?
- Var noe vanskelig å forstå?
- Hva ville du forandret?

Velg **én** forbedring og lag den.

## 🐞 Når noe går galt

Ikke start hele spillet på nytt med en gang.

Prøv:

1. Hva var den siste endringen?
2. Hvilken liten del virker ikke?
3. Kan du bruke `print()` for å se et tall eller en verdi?
4. Kan du teste bare den delen?
5. Endre én ting og kjør igjen.

En bug betyr ikke at prosjektet er ødelagt. Det betyr at du har noe å undersøke.

## 🏁 Ferdig?

Spillet ditt er klart når:

- [ ] det starter
- [ ] spilleren kan styre
- [ ] det finnes et mål
- [ ] minst én spillregel virker
- [ ] spilleren får vite hva som skjer
- [ ] du har testet både seier/tap der spillet bruker det
- [ ] en annen person har prøvd spillet
- [ ] du har gjort minst én forbedring etter testing
- [ ] spillet har et navn
- [ ] du kan vise én del av koden og forklare hva den gjør

Det trenger ikke være perfekt.

Det trenger å være **ditt**.

## 🎤 Vis fram spillet

Fortell testspilleren, klassen eller en voksen:

1. Hva heter spillet?
2. Hva skal spilleren gjøre?
3. Hvilken del var morsomst å lage?
4. Hvilken bug fant du?
5. Vis én kodebit du forstår godt.

## 🌟 Hvis du vil fortsette

Du kan senere prøve flere mål, flere monstre, nye brett, en klokke eller egne bilder.

Men ikke legg til alt samtidig. Velg én idé, bygg den og test den.

## 🧠 Se hva du har gjort

Da du startet Python Explorer, skrev du små programmer.

Nå har du brukt variabler, `if`, løkker, funksjoner, tilfeldighet, koordinater, tastetrykk og grafikk til å bygge et spill som reagerer på spilleren.

**Du lagde ditt eget spill.** 🎉
