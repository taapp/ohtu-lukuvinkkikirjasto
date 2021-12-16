*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Delete User And Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  late
    Set Password  lammas123
    Set Password Confirmation  lammas123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  la
    Set Password  lammas123
    Set Password Confirmation  lammas123
    Submit Credentials
    Register Should Fail With Message  Käyttäjätunnuksen pitää olla vähintään 3 merkkiä pitkä

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  123
    Set Password Confirmation  123
    Submit Credentials
    Register Should Fail With Message  Salasanan pitää olla vähintään 5 merkkiä pitkä

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle122
    Submit Credentials
    Register Should Fail With Message  Salasanat eivät täsmää

Login After Successful Registration
    Go To Login Page
    Set Username  late
    Set Password  lammas123
    Submit Logins
    Login Should Succeed

Login After Failed Registration
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle122
    Submit Credentials
    Go To Login Page
    Set Username  nalle
    Set Password  nalle123
    Submit Logins
    Login Should Fail With Message  Väärä tunnus tai salasana!



*** Keywords ***
Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Rekisteröidy

Submit Logins
    Click Button  Kirjaudu

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Delete User And Close Browser
    Delete User  late
    Close Browser

Login Should Succeed
    List Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}