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
    Set Kommentit  osta
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
    Set Kommentit  jaa kavereille
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
    Set Kommentit  kuuntele uudestaan
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
    Set Kommentit  katso joskus
    Set Kuvaus  gravitaatio esitys
    Submit Details
    Add Video Should Succeed

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
    
#register ei tee mitään sillä rekisteröitymistä ei ole toteutettu vielä
#Register
#    Go To Register Page
#    Set Nimimerkki  moro
#    Set Salasana  tietoturva
#    Input Text  password_confirmation  tietoturva
#    Click Button  Rekisteröidy

Login
    Go To Login Page
    Set Nimimerkki  tunnus
    Set Salasana  passu
    Click Button  Kirjaudu

Submit Details
    Click Button  Lisää

Set Nimimerkki
    [Arguments]  ${nimimerkki}
    Input Text  username  ${LOGIN_NAME}

Set Salasana
    [Arguments]  ${salasana}
    Input Text  password  ${PASSWORD}

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

Set Kommentit
    [Arguments]  ${kommentit}
    Input Text  kommentit  ${kommentit}

Set Kuvaus
    [Arguments]  ${kuvaus}
    Input Text  kuvaus  ${kuvaus}

Set Kurssit
    [Arguments]  ${kurssit}
    Input Text  kurssit  ${kurssit}
