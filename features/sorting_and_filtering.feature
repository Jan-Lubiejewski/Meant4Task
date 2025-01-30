Feature: Item sorting and filtering

  #Scenario: Sort by Price: Lowest first
  #  Given I am on "http://www.automationpractice.pl" Home Page
  #  Then I click on Women tab
  #  When I choose Sort by "Price: Lowest first"
  #  Then The prices should be sorted in ascending order

  #Scenario: Sort by Price: Highest first
  #  Given I am on "http://www.automationpractice.pl" Home Page
  #  Then I click on Women tab
  #  When I choose Sort by "Price: Highest first"
  #  Then The prices should be sorted in descending order

  #Scenario: Sort by Product Name: A to Z
  #  Given I am on "http://www.automationpractice.pl" Home Page
  #  Then I click on Women tab
  #  When I choose Sort by "Product Name: A to Z"
  #  Then The names should be sorted in ascending order

  Scenario: Sort by Product Name: Z to A
    Given I am on "http://www.automationpractice.pl" Home Page
    Then I click on Women tab
    When I choose Sort by "Product Name: Z to A"
    Then The names should be sorted in descending order