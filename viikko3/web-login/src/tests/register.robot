*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  harjoitus
    Set Password  harjoitus1234
    Set Password Confirmation  harjoitus1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ha
    Set Password  harjoitus1234
    Set Password Confirmation  harjoitus1234
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  harjoitustesti
    Set Password  harjoitus
    Set Password Confirmation  harjoitus
    Submit Credentials
    Register Should Fail With Message  Password should contain at least 8 characters and not include only letters 

Register With Nonmatching Password And Password Confirmation
    Set Username  testiharjoitus
    Set Password  harjoitus1234
    Set Password Confirmation  harjoitus4321
    Submit Credentials
    Register Should Fail With Message  Passwords does not match

Login After Successful Registration
    Set Username  harjoitusharjoitus
    Set Password  harjoitus123456
    Set Password Confirmation  harjoitus123456
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  harjoitusharjoitus
    Set Password  harjoitus123456
    Login Page Should Be Open

Login After Failed Registration
    Set Username  harjoituss
    Set Password  harjoituss
    Set Password Confirmation  harjoituss
    Submit Credentials
    Register Should Fail With Message  Password should contain at least 8 characters and not include only letters 
    Go To Login Page
    Set Username  harjoituss
    Set Password  harjoituss
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password confirmation}
    Input Password  password_confirmation  ${password confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}