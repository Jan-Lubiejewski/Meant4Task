Feature: Registration

  Background: Navigate to Authentication Page
    Given I am on "http://www.automationpractice.pl" Home Page
    When I click on "Sign in" button
    Then I get redirected to Authentication Page

  #Scenario: Empty email address
  #  Given I do not fill Email address and click on "Create an account" button
  #  Then The red alert "Invalid email address" should appear

  Scenario: Valid email address
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button

  
