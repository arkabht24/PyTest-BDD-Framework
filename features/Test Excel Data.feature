Feature: Login functionality

  Scenario Outline: Verify login with multiple credentials
    When user enters "<username>" and "<password>"
    # Then login should be "<expectedResult>"

    Examples:
      | username | password | expectedResult |
      