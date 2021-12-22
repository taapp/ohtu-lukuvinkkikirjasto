# Ohjelmistotuotanto-kurssi, miniprojekti: Lukuvinkkikirjasto

[Miniprojektin yleisohje](https://ohjelmistotuotanto-hy.github.io/miniprojekti/)

[Miniprojektin speksi](https://ohjelmistotuotanto-hy.github.io/speksi/)

[Miniprojektin backlogit](https://docs.google.com/spreadsheets/d/1dgDb1iogv_WNv830mru2iMjrutRrwumTPhakcXey25w/edit#gid=0)

[2. sprintin release](https://github.com/taapp/ohtu-lukuvinkkikirjasto/releases/tag/sprint2)

[3. sprintin release](https://github.com/taapp/ohtu-lukuvinkkikirjasto/releases/tag/sprint3)

[Rekisteröitymisen Robot testit](https://github.com/taapp/ohtu-lukuvinkkikirjasto/blob/main/src/tests/register.robot)

[Loput Robot testit](https://github.com/taapp/ohtu-lukuvinkkikirjasto/blob/main/src/tests/home.robot)

[Loppuraportti](https://github.com/taapp/ohtu-lukuvinkkikirjasto/blob/main/raportti.md)

![GitHub Actions](https://github.com/taapp/ohtu-lukuvinkkikirjasto/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/taapp/ohtu-lukuvinkkikirjasto/branch/main/graph/badge.svg?token=FLWIEJ35C8)](https://codecov.io/gh/taapp/ohtu-lukuvinkkikirjasto)

### Ohjelman suorittaminen
Ohjelma tulee olemaan web sovellus, mutta sovelluksella ei ole vielä osoitetta, joten tässä ohje kuinka ajaa se linux ympäristössä.
Kopioi repositorio ja mene sen juurikansiossa olevaan src kansioon ja aja komennot.
```
poetry install
```
```
poetry shell
```
Aja sen jälkeen komento, jolloin sovellus lähtee päälle.
```
flask run
```
Mene omavalintaisella selaimella komentorivillä näkyvään osoitteeseen (tyypillisesti http://127.0.0.1:5000/), jossa sovelluksen nyt pitäisi näkyä.

Ohjelmassa on kaksi käyttäjää, joilla voit kirjautua sisään:

Käyttäjätunnus: "kayttaja", Salasana: "salasana"

Käyttäjätunnus: "tunnus", Salasana: "passu"

Voit myös rekisteröityä sovellukseen omilla tunnuksilla.

### Definition of Done
User story toimii backlogin hyväksymiskriteereiden mukaan ja sille on toteutettu automaattisia testejä vähintään kyseisen storyn tärkeimmille ominaisuuksille.

### Yksikkötestien ajaminen
Yksikkötestit voidaan ajaa komennolla
```
poetry run pytest
```
Testien ajaminen tuhoaa tietokannan taulujen sisällön. Tietokannan sisällön voi alustaa alkuperäiseksi ajamalla komennon (olettaen, että komento ajetaan src-hakemistossa)
```
poetry run python3 initialize_database.py
```

### Robot Framework -testien ajaminen
Robot Framework -testien ajamiseksi tulee ensin alustaa tietokanta ajamalla komento (olettaen, että komento ajetaan src-hakemistossa)
```
poetry run python3 initialize_database.py
```
Tämän jälkeen tulee laittaa sovellus päälle (katso kohta "Ohjelman suorittaminen"). Robot framework -testit voidaan nyt ajaa suorittamalla komento (olettaen, että komento ajetaan src-hakemistossa)
```
poetry run robot tests
```
Testien suorittaminen tuottaa tietokantaan uutta sisältöä, jonka vuoksi voi olla suositeltavaa vielä alustaa tietokanta aiemmin annetulla komennolla.
