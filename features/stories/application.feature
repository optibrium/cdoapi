Feature: General webserver functionality

Background:
    Given a web application
    And an unauthenticated client

Scenario: The healthcheck URL returns healthy
    When I get /
    Then I receive a 200 status

Scenario: Incorrect verbs generate a 404
    When I DELETE /
    Then I receive a 404 status
    And the error endpoint not found is returned

Scenario: Page not found generates a 404
    When I get /some/none/existent/url
    Then I receive a 404 status
    And the error endpoint not found is returned

Scenario: Failed logouts have the correct message
    When I POST {} to the /logout
    Then I receive a 403 status
    And the error No User logged out is returned

Scenario: General Errors are handled cleanly
    When a request to /authcheck generates an exception
    Then I receive a 500 status
    And the error please check log is returned
