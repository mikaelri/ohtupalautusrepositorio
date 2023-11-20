*** Settings ***
Resource  resource.robot
Resource  login.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  testi  testi123

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  harjoitus  harjoitus123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testi  testi123
    Output Should Contain  User with username testi already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  testi123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  abcd!?  abcdef123
    Output Should Contain  Username should contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  harjoitus  harjoi
    Output Should Contain  Password should contain at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  harjoitus  harjoitusharjoitus
    Output Should Contain  Password should contain at least 8 characters and not include only letters
