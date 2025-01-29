Feature: Shopping flow

  Scenario: Purchase a white blouse
    Given I am on "http://www.automationpractice.pl" Home Page
    Then I click on Women tab
    Then I click on Blouse
    * I choose "White" color and "M" size and click on "Add to cart"
    * I click "Proceed to checkout" and I get redirected to Shopping Cart Page
    * In shopping cart I click "Proceed to checkout"
    Then I login using valid credentials
    * On address tab I click "Proceed to checkout"
    * On shipping tab I agree to terms of service and click "Proceed to checkout"
    Then I choose to pay by bank wire
    * I click "I confirm my order"
    * The green alert "Your order on My Shop is complete." should appear