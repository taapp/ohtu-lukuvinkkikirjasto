*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
#${BROWSER}  chrome
${DELAY}  0.1 seconds
#${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/login
${REGISTER URL}  http://${SERVER}/register
${ADD_SUBJECT URL}  http://${SERVER}/add_subject
${LIST URL}  http://${SERVER}/list
${LOGOUT_URL}  http://${SERVER}/logout
${LOGIN_NAME}  tunnus
${PASSWORD}  passu

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Page Should Contain  Lukuvinkkikirjasto

Add_subject Page Should Be Open
    Title Should Be  Lisää lukuvinkki

List Page Should Be Open
    Page Should Contain  Tyyppi
    Page Should Contain  Otsikko
    Page Should Contain  Tekijä
    Page Should Contain  ISBN

Login Page Should Be Open
    Title Should Be  Kirjaudu sisään

Go To Main Page
    Go To  ${HOME URL}

Go To Add_subject Page
    Go To  ${ADD_SUBJECT URL}

Go To List Page
    Go To  ${LIST URL}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Register Page
    Go To ${REGISTER URL}

Go To Logout Page
    Go To  ${LOGOUT_URL}