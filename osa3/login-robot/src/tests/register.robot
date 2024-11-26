*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Register New User With Credentials  testuser  testpassword123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Register New User With Credentials  testuser  testpassword123
    Register New User With Credentials  testuser  newpassword!
    Output Should Contain  User with username testuser already exists

Register With Too Short Username And Valid Password
    Register New User With Credentials  us  validpassword2000
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Register New User With Credentials  tes7us3r  validpassword2000
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Register New User With Credentials  testuser  shortpw
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only letters
    Register New User With Credentials  testuser  badpassword
    Output Should Contain  Password must contain at least 1 special character or number

*** Keywords ***
Register New User With Credentials
    [Arguments]  ${username}  ${password}
    Input Register Command
    Input Credentials  ${username}  ${password}