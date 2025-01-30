# Automation practice BDD acceptante tests 
Automation Acceptance Tests written for website [Automation Practice](http://www.automationpractice.pl/) using:
- **Python v. "3.9.1"**
- **Selenium v. "4.28.1"**
- **Pytest v. "8.3.4"**
- **Pytest-bdd v. "3.9.74"**

## Overiew
The automation acceptance tests are written for following modules:
1. Login
2. Register
3. Shopping flow
4. Item Sorting and Filtering

## Dependencies and Setup
To run the tests you have to have Python 3.9.1 (or later version) installed on your machine. You will also need Google Chrome browser:
- [Python installation](https://www.python.org/downloads/)
- [Google Chrome installation](https://www.google.com/chrome/)

### Prerequisites
First, if you like it may be a good idea to set up virtual environment. To do so run the following commands:
```bash
    python -m venv venv
    venv\Scripts\activate # On Windows
    source venv/bin/activate # On Linux
```
Then you should install all the requirements using this command:
```bash
    pip install -r requirements.txt
```
### Running tests
To run all the test files use the command:
```bash
    pytest
```

To run specific test file you can use:
```bash
   pytest <test_file_relative_to_root_location>
```
For example
```bash
   pytest features/steps/test_login_steps.py
```

### Test report
To generate test report add following flag
```bash
    pytest --html=report.html
```
