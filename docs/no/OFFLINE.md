# Offline-pakke

EduPython Kids skal kunne brukes uten elevkontoer, skytjenester eller permanent Internett-forbindelse.

## Bygg
Fra repo-roten:

```bash
python tools/build_offline.py
```

Dette lager `dist/EduPython-Kids-offline/` og `dist/EduPython-Kids-offline.zip`.

Arkivet inneholder begge komplette kursutgaver, øvelser, kjørbare eksempler, lærer/foreldre-materiale, utskriftsark, dokumentasjon, lisensinformasjon og `START-HERE.txt`.

CI, Git-metadata og utviklingsverktøy er ikke nødvendige i elevpakken.

## Klasseromsbruk
Bygg arkivet på en tilkoblet maskin, kopier det til klasseromsmaskinene, pakk ut og åpne `START-HERE.txt`. Python må allerede være installert. Turtle krever lokal Tk/Turtle-støtte.

## Personvern
Ingen konto, analysetjeneste eller nettverksforespørsel kreves av kursmaterialet eller standardeksemplene.
