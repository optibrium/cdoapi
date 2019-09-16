Feature: Authentication to the API

Background:
    Given a web application
    And an unauthenticated client

Scenario Outline: I can log in
    When <username> and <password> correspond to a valid user
    And I POST {"username":"<username>","password":"<password>"} to the /login
    Then I receive an x-api-key
    And a matching cookie
    When I GET /authcheck with the token
    Then I receive a 200 status
    When I GET /authcheck with the cookie
    Then I receive a 200 status

    Examples: valid username-password pairs
    | username    | password    |
    | demo        | demo        |
    | catsanddogs | catsanddogs |
    | admin       | admin       |
    | user        | p@55w0rd    |

Scenario: I can log out with a token
    When username and password correspond to a valid user
    And I POST {"username":"username","password":"password"} to the /login
    Then I receive an x-api-key
    When I GET /authcheck with the token
    Then I receive a 200 status
    When I GET /logout with the token
    Then I receive a 403 status
    When I GET /authcheck with the token
    Then I receive a 403 status

Scenario: I can log out with a cookie
    When username and password correspond to a valid user
    And I POST {"username":"username","password":"password"} to the /login
    Then I receive a cookie
    When I GET /authcheck with the cookie
    Then I receive a 200 status
    When I GET /logout with the cookie
    Then I receive a 403 status
    When I GET /authcheck with the cookie
    Then I receive a 403 status

Scenario: The correct error code is returned when incorrect details are supplied
    When I have no valid users
    And I POST {"username":"username","password":"password"} to the /login
    Then I receive a 403 status
    And the error Incorrect Username or Password is returned

Scenario: It handles when correct user and incorrect password is supplied
    When username and password correspond to a valid user
    And I POST {"username":"username","password":"invalid password"} to the /login
    Then I receive a 403 status
    And the error Incorrect Username or Password is returned

Scenario Outline: All of the read data endpoints require authentication
    When I GET <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners        |
    | /owners/1      |
    | /cats          |
    | /cats/1        |
    | /dogs          |
    | /dogs/1        |

Scenario Outline: All of the create data endpoints require authentication
    When I POST {"name":"some name"} to the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners        |
    | /cats          |
    | /dogs          |
    | /owner/1/pet/1 |

Scenario Outline: All of the update data endpoints require authentication
    When I PUT {"name":"some name"} to the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners/1      |
    | /cats/1        |
    | /dogs/1        |

Scenario Outline: All of the delete data endpoints require authentication
    When I DELETE <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners/1      |
    | /cats/1        |
    | /dogs/1        |
    | /owner/1/pet/1 |
