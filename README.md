# Ohjelmistotuotanto-kurssi, miniprojekti: Lukuvinkkikirjasto

[Miniprojektin yleisohje](https://ohjelmistotuotanto-hy.github.io/miniprojekti/)

[Miniprojektin speksi](https://ohjelmistotuotanto-hy.github.io/speksi/)

[Miniprojektin backlogit](https://docs.google.com/spreadsheets/d/1dgDb1iogv_WNv830mru2iMjrutRrwumTPhakcXey25w/edit#gid=0)

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
Mene omavalintaisella selaimella komentorivillä näkyvään osoitteeseen, jossa sovelluksen nyt pitäisi näkyä.

Ohjelmassa on kaksi käyttäjää, joilla voit kirjautua sisään:

Käyttäjätunnus: "käyttäjä", Salasana: "salasana"

Käyttäjätunnus: "tunnus", Salasana: "passu"


### Definition of Done
User story toimii backlogin hyväksymiskriteereiden mukaan ja sille on toteutettu automaattisia testejä vähintään kyseisen storyn tärkeimmille ominaisuuksille.
