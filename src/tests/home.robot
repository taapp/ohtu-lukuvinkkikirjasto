*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Add Book With Valid Parameters
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

See Reading List
    Go To List Page
    See Reading List Should Succeed

*** Keywords ***
#Add Book And Go To Main Page

#Testaa tietojen syöttämistä
Add Book Should Succeed
    List Page Should Be Open
    Page Should Contain  Noksu kulkee ja keksii

See Reading List Should Succeed
    List Page Should Be Open
    Page Should Contain  Sinuhe Egyptiläinen


Submit Details
    Click Button  Lisää

Set Tyyppi
    [Arguments]  ${tyyppi}
    Input Text  tyyppi  ${tyyppi}

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