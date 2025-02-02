Feature: Registration

  Background: Navigate to Authentication Page
    Given I am on "http://www.automationpractice.pl" Home Page
    When I click on "Sign in" button
    Then I get redirected to Authentication Page

 Scenario: Empty email address
    Given I do not fill Email address and click on "Create an account" button
    Then The red alert "Invalid email address" should appear on Authentication Page

  Scenario: Input valid email address then clear all fields and attemp to register an account
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I clear all fields and click on Register button
    Then The red alerts for all required fields should appear on Create Account Page

  Scenario: Invalid first name
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill first name with "123" and rest of required fields with valid data and click on Register button
    Then The red alert "firstname is invalid" should appear on Create Account Page

  Scenario: Invalid last name
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill last name with "123" and rest of required fields with valid data and click on Register button
    Then The red alert "lastname is invalid" should appear on Create Account Page

  Scenario: Invalid email
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill email again with "123" and rest of required fields with valid data and click on Register button
    Then The red alert "email is invalid" should appear on Create Account Page

  Scenario: Invalid password
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill password with "123" and rest of required fields with valid data and click on Register button
    Then The red alert "passwd is invalid" should appear on Create Account Page

  Scenario: Successful registration
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill all the required fields with valid data and click on Register button
    Then I get redirected to My Account Page and green alert "Your account has been created" appears

# There's no validation for the date of birth, if there were it could end in
# "Then The red alert "date of birth is invalid" should appear on Create Account Page"
  Scenario: Successful registration with invalid birth date and optional fields
    Given I fill Email address with "qamyk1258@gmail.com" and click on Create an account button
    Then I fill invalid date of birth, click on "Mr" title and check "Sign up for our newsletter"
    Then I fill all the required fields with valid data and click on Register button
    Then I get redirected to My Account Page and green alert "Your account has been created" appears
    

  
