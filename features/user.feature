Feature: Handle storing, retrieving and deleteing customer details
    Scenario: Retrieve a customer details
        Given flask is setup
        And some users are in the system
        When I retrieve the customer bob01
        Then I should get a 200 as response status code
        And the following user details are returned:
            | name        |
            | Robert Sale |

    Scenario: Retrieve a customer details that doesn't exist
        Given flask is setup
        And some users are in the system
        When I retrieve the customer wacky01
        Then I should get a 404 as response status code