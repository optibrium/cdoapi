Feature: Authentication to the API

Background:
    Given a web application
    And an unauthenticated client

Scenario: I can log in
    When I POST a valid <username> and <password> to /login
    Then I receive an x-api-key
    And a matching cookie
    When I access the URI / with the token
    Then I receive a 200 status
    When I access the URI / with the cookie
    Then I receive a 200 status

    Examples: valid username-password pairs
    | username    | password    |
    | demo        | demo        |
    | catsanddogs | catsanddogs |
    | admin       | admin       |
    | user        | p@55w0rd    |

Scenario: I can log out with a token
    When I POST a valid <username> and <password> to /login
    Then I receive an x-api-key
    When I access the URI / with the token
    Then I receive a 200 status
    When I access the URI /logout with the token
    Then I receive a 403 status
    When I access the URI / with the token
    Then I receive a 403 status

Scenario: I can log out with a cookie
    When I POST a valid <username> and <password> to /login
    Then I receive a cookie
    When I access the URI / with the cookie
    Then I receive a 200 status
    When I access the URI /logout with the cookie
    Then I receive a 403 status
    When I access the URI / with the cookie
    Then I receive a 403 status

Scenario: All of the read data endpoints require authentication
    When I GET the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners        |
    | /owners/1      |
    | /cats          |
    | /cats/1        |
    | /dogs          |
    | /dogs/1        |
    | /owner/1/pet/1 |

Scenario: All of the create data endpoints require authentication
    When I POST the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners        |
    | /cats          |
    | /dogs          |
    | /owner/1/pet/1 |

Scenario: All of the update data endpoints require authentication
    When I PUT the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners/1      |
    | /cats/1        |
    | /dogs/1        |

Scenario: All of the delete data endpoints require authentication
    When I DELETE the <endpoint>
    Then I receive a 403 status

    Examples: Read Endpoints
    | endpoint       |
    | /owners/1      |
    | /cats/1        |
    | /dogs/1        |
    | /owner/1/pet/1 |
