Feature: Buzz Functionality

  Scenario Outline: Verify Buzz window
    Given user enters "<username>" and "<password>" and clicks on login button
    When Verify Buzz is displayed or not
    When I will navigate to the Buzz section
    Then I will validate the Page header "<pageHeader>"

    Examples:
      | username | password | pageHeader |
      | Admin | admin123 | Buzz Newsfeed |
      