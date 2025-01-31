Feature: Login

  Background: Navigate to Authentication Page
    Given I am on "http://www.automationpractice.pl" Home Page
    When I click on "Sign in" button
    Then I get redirected to Authentication Page

  Scenario: Empty email and password
    Given I do not fill email and password and click on "Sign in" button
    Then The red alert "An email address required." should appear

  Scenario: Valid email and empty password
    Given I fill email with "jkli2@gmail.com" and do not fill password and click on "Sign in" button
    Then The red alert "Password is required." should appear

  Scenario: Empty email and valid password
    Given I do not fill email and fill password with "123456" and click on "Sign in" button
    Then The red alert "An email address required." should appear

  Scenario: Valid email and invalid password
    Given I fill email with "jkli2@gmail.com" and fill password with "12345" and click on "Sign in" button
    Then The red alert "Authentication failed." should appear

  Scenario: Successful login
    Given I fill email with "jkli2@gmail.com" and fill password with "123456" and click on "Sign in" button
    Then I get redirected to My Account Page
  