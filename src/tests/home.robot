*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Add Book With Valid Parameters
    Login
    Go To Add_subject Page
    Set Tyyppi  kirja
    Set Otsikko  Noksu kulkee ja keksii
    Set Kirjailija  Mikko Kunnas
    Set Isbn  951-0-32245-8
    Set Tagit  tärkeä
    Set Url  https://wsoy.fi
    Set Kommentti  osta
    Set Kuvaus  hyvä tenttikirja
    Set Kurssit  ohtu
    Submit Details
    Add Book Should Succeed

Add Blog Or Article With Valid Parameters
    Login
    Go To Add_subject Page
    Set Tyyppi  artikkeli
    Set Otsikko  jonkin tyyppinen blogi
    Set Kirjailija  Seppo Papunen
    Set Tagit  paras
    Set Url  https://blogit.fi
    Set Kommentti  jaa kavereille
    Set Kuvaus  hauska blogi
    Submit Details
    Add Blog Or Article Should Succeed

Add Podcast With Valid Parameters
    Login
    Go To Add_subject Page
    Set Tyyppi  podcast
    Set Otsikko  joku podcast
    Set Kirjailija  Kari Hietalahti
    Set Tagit  aika hurjia juttuja
    Set Url  https://yle.fi
    Set Kommentti  kuuntele uudestaan
    Set Kuvaus  häröilyä
    Submit Details
    Add Podcast Should Succeed

Add Video With Valid Parameters
    Login
    Go To Add_subject Page
    Set Tyyppi  video
    Set Otsikko  Gravity Visualized
    Set Kirjailija  Los Gatos High School
    Set Tagit  mielenkiintoinen
    Set Url  https://www.youtube.com/watch?v=MTY1Kje0yLg
    Set Kommentti  katso joskus
    Set Kuvaus  gravitaatio esitys
    Submit Details
    Add Video Should Succeed

Add Private Book 
    Login
    Go To Add_subject Page
    Set Tyyppi  kirja
    Set Otsikko  Ajattelu nopeasti ja hitaasti
    Set Kirjailija  Daniel Kahneman
    Set Isbn  ${EMPTY}
    Set Tagit  ${EMPTY}
    Set Url  https://www.terracognita.fi/tuote/ajattelu-nopeasti-ja-hitaasti/
    Set Kommentti  ${EMPTY}
    Set Kuvaus  ${EMPTY}
    Set Kurssit  ${EMPTY}
    Set Yksityinen
    Submit Details
    Go To Logout Page
    Login Other User
    List Page Should Be Open
    Page Should Not Contain  Ajattelu nopeasti ja hitaasti

Add Public Book 
    Login
    Go To Add_subject Page
    Set Tyyppi  kirja
    Set Otsikko  Harry Potter
    Set Kirjailija  J.K. Rowling
    Set Isbn  ${EMPTY}
    Set Tagit  ${EMPTY}
    Set Url  ${EMPTY}
    Set Kommentti  ${EMPTY}
    Set Kuvaus  ${EMPTY}
    Set Kurssit  ${EMPTY}
    Set Julkinen
    Submit Details
    Go To Logout Page
    Login Other User
    List Page Should Be Open
    Page Should Contain  Harry Potter

See Reading List
    Go To List Page
    See Reading List Should Succeed

Data Is Saved
    Login
    Data Is Saved Succeed

User Can Login
    Go To Main Page
    Login
    List Page Should Be Open

User Can Logout
    Go To Main Page
    Login
    Go To Logout Page
    Main Page Should Be Open

User Can Not Login With Invalid Username
    Go To Login Page
    Set Nimimerkki  gorilla
    Set Salasana  passu
    Login Page Should Be Open

User Can Not Login With Invalid Password
    Go To Login Page
    Set Nimimerkki  tunnus
    Set Salasana  passu123
    Login Page Should Be Open

*** Keywords ***
#Add Book And Go To Main Page

#Testaa tietojen syöttämistä
Add Book Should Succeed
    List Page Should Be Open
    Page Should Contain  Noksu kulkee ja keksii

Add Blog Or Article Should Succeed
    List Page Should Be Open
    Page Should Contain  Seppo Papunen

Add Podcast Should Succeed
    List Page Should Be Open
    Page Should Contain  Kari Hietalahti

Add Video Should Succeed
    List Page Should Be Open
    Page Should Contain  Los Gatos High School

See Reading List Should Succeed
    List Page Should Be Open

Data Is Saved Succeed
    List Page Should Be Open
    Page Should Contain  Noksu kulkee ja keksii

Login
    Go To Login Page
    Set Nimimerkki  tunnus
    Set Salasana  passu
    Click Button  Kirjaudu

Login Other User
    Go To Login Page
    Set Nimimerkki  kayttaja
    Set Salasana  salasana
    Click Button  Kirjaudu

Submit Details
    Click Button  Lisää

Set Nimimerkki
    [Arguments]  ${nimimerkki}
    Input Text  username  ${nimimerkki}

Set Salasana
    [Arguments]  ${salasana}
    Input Text  password  ${salasana}

Set Tyyppi
    [Arguments]  ${tyyppi}
    Click Button  ${tyyppi}

Set Otsikko
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Set Kirjailija
    [Arguments]  ${kirjailija}
    Input Text  kirjailija  ${kirjailija}

Set Isbn
    [Arguments]  ${isbn}
    Input Text  isbn  ${isbn}

Set Tagit
    [Arguments]  ${tagit}
    Input Text  tagit  ${tagit}

Set Url
    [Arguments]  ${url}
    Input Text  url  ${url}

Set Kommentti
    [Arguments]  ${kommentti}
    Input Text  kommentti  ${kommentti}

Set Kuvaus
    [Arguments]  ${kuvaus}
    Input Text  kuvaus  ${kuvaus}

Set Kurssit
    [Arguments]  ${kurssit}
    Input Text  kurssit  ${kurssit}

Set Yksityinen
    Select Checkbox  yksityinen

Set Julkinen
    Unselect Checkbox  yksityinen
