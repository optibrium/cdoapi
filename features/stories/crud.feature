Feature: The Create, Read, Update and Delete API

    The CRUD API allows us to list, create, read, update and delete
    Owners, Cats and Dogs.

Background:
    Given a web application
    And a client with a valid authentication token

Scenario Outline: We can create Owners, Cats and Dogs
    When I POST {"name":"<name>"} to the /<type>
    Then a <type> has been created called <name>
    And I receive an id
    
    Examples: names and types
    | name   | type    |
    | test   | owners  |
    | test   | cats    |
    | bob    | dogs    |
    | bob    | owners  |
    | alice  | cats    |
    | alice  | dogs    |

Scenario Outline: The create API rejects invalid names
    When I POST {"name":"<name>"} to the /<type>
    Then I receive a 400 status

    Examples: names and types
    | name | type   |
    | $ %' | owners |
    | $ %' | cats   |
    | $ %' | dogs   |
    | &()- | owners |
    | &()- | cats   |
    | &()- | dogs   |

Scenario Outline: The API rejects requests that do not contain the correct parameters
    When I POST {} to the /<type>
    Then I receive a 400 status

    Examples: Types
    | type   |
    | owners |
    | cats   |
    | dogs   |

Scenario Outline: The create API rejects duplicate names
    When I POST {"name":"<name>"} to the /<type>
    Then a <type> has been created called <name>
    And I receive an id
    When I POST {"name":"<name>"} to the /<type>
    Then I receive a 409 status
    And the error Name exists is returned
    
    Examples: names and types
    | name | type    |
    | test | owners  |
    | test | cats    |
    | test | dogs    |
    | bob  | owners  |
    | bob  | cats    |
    | bob  | dogs    |

Scenario Outline: We can list Owners, Cats and Dogs
    Given <type> contains ["alice", "bob", "charlotte"]
    When I GET /<type>
    Then I receive a 200 status
    And a list of names containing ["alice", "bob", "charlotte"] is returned

    Examples: Types
    | type   |
    | owners |
    | cats   |
    | dogs   |

Scenario Outline: We can create, read, update and delete Owners, Cats and Dogs
    When I POST {"name":"<name>"} to the /<type>
    And I receive an id
    And I GET /<type>/id with the id
    Then the object returned has a name of <name>
    When I PUT {"name": "<new_name>"} to the /<type>/id with the id
    And I GET /<type>/id with the id
    Then the object returned has a name of <new_name>
    When I DELETE /<type>/id with the id
    Then I receive a 202 status
    When I GET /<type>/id with the id
    Then I receive a 404 status
    
    Examples: names and types
    | name | type    | new_name  |
    | test | owners  | something |
    | test | cats    | something |
    | test | dogs    | something |
    | bob  | owners  | alice     |
    | bob  | cats    | alice     |
    | bob  | dogs    | alice     |

Scenario Outline: We can allocate and remove ownerships
    When I POST {"name":"<owner>"} to the /owners
    And I receive an owner id
    And I POST {"name":"<pet>"} to the /<type>
    And I receive a pet id
    And I POST to the /owner/%d/pet/%d with the ids
    Then I receive a 201 status
    When I DELETE /owner/%d/pet/%d with the ids
    Then I receive a 202 status
    When I DELETE /owner/%d/pet/%d with the ids
    Then I receive a 404 status

    Examples: Owners and their pets
    | owner  | pet       | type |
    | bob    | alice     | cats |
    | claire | charlotte | cats |
    | claire | charlotte | cats |
    | bridge | charlotte | dogs |
    | bob    | alice     | dogs |

Scenario: Every Owner in the list contains a list of pets
    Given owners contains ["alice", "bob", "charlotte"]
    And alice owns cats ["bella", "dory"]
    And bob owns dogs ["dusty", "buster", "scruggs"]
    And charlotte owns dogs ["sherlock", "meeko"]
    And charlotte owns cats ["garfield", "keanu", "gulliver"]
    When I GET /owners
    Then alice is returned with pets ["bella", "dory"]
    And bob is returned with pets ["dusty", "buster", "scruggs"]
    And charlotte is returned with pets ["sherlock", "meeko", "garfield", "keanu", "gulliver"]

Scenario Outline: Non-existent pets return Not Found
    Given <type> contains ["garfield", "keanu", "gulliver"]
    When I GET /<other_type>
    Then I receive a 404 status

    Examples: Types
    | type   | other_type |
    | cats   | dogs       |
    | dogs   | cats       |
    | cats   | unicorns   |
    | dogs   | unicorns   |
    
