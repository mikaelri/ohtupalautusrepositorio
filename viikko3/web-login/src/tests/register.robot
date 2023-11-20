*** Settings ***
Resource  resource.robot
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
    Set Username  harjoitus
    Set Password  harjoitus
    Set Password Confirmation  harjoitus
    Submit Credentials
    Register Should Fail With Message  Password should contain at least 8 characters and not include only letters 

Register With Nonmatching Password And Password Confirmation
    Set Username  harjoitus
    Set Password  harjoitus1234
    Set Password Confirmation  harjoitus4321
    Submit Credentials
    Register Should Fail With Message  Passwords does not match

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

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}