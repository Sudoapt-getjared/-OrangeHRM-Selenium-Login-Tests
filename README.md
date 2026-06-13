# OrangeHRM Login Automation - Cross-Browser Selenium Tests

<p align="center">
  <a href="https://www.youtube.com/watch?v=zgqfWLHNKLk">Video Demonstration</a>
</p>

## Description
This project automates the login functionality of the OrangeHRM web application using Python and the Selenium WebDriver. The script verifies that both an **Admin** account and a **Standard User** account can successfully authenticate, and it runs the same login flow across three browsers (Chrome, Edge, and Firefox) so the application's login behavior can be confirmed in each environment. The tests target the public OrangeHRM demo instance and report a clear PASS/FAIL result for every browser-and-account combination.

The suite is also wired into a GitHub Actions workflow so the cross-browser tests run automatically on every push and pull request, and it has been executed on a self-provisioned AWS EC2 instance set up specifically for testing.

## Languages and Utilities Used
- Python
- Selenium WebDriver
- GitHub Actions (CI workflow)

## Environments Used
- Visual Studio Code (VS Code)
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- AWS EC2 instance (self-created for testing)

## Test Coverage
| Account | Username | Browsers |
| --- | --- | --- |
| Admin | Admin | Chrome, Edge, Firefox |
| Standard User | Jaredp01 | Chrome, Edge, Firefox |

## Program walk-through:

<p align="center">
Open the project in VS Code: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Project open in VS Code"/>
<br /><br />
Run the login script: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Running the script"/>
<br /><br />
Chrome - Admin and Standard User login: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Chrome login"/>
<br /><br />
Edge - Admin and Standard User login: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Edge login"/>
<br /><br />
Firefox - Admin and Standard User login: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Firefox login"/>
<br /><br />
Test results (PASS output in the terminal): <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="Terminal results"/>
<br /><br />
GitHub Actions workflow run: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="GitHub Actions run"/>
<br /><br />
Running on the AWS EC2 instance: <br/>
<img src="https://i.imgur.com/placeholder.png" height="80%" width="80%" alt="AWS EC2 run"/>
</p>

## How to Run
1. Install the dependencies: `pip install -r requirements.txt`
2. Make sure Chrome, Edge, and Firefox are installed (Selenium 4 manages the drivers automatically).
3. Run the tests: `python orangehrm_login_tests.py`

## What I Learned
Through this project I learned how to drive a real web application end to end with Selenium WebDriver in Python: locating elements reliably with explicit waits instead of fixed delays, building reusable driver "factory" functions so the same test logic could be pointed at Chrome, Edge, and Firefox, and structuring assertions so each browser-and-account result is reported clearly. I also got hands-on practice setting up a continuous integration pipeline with GitHub Actions using a build matrix to fan the tests out across browsers, and I provisioned and configured my own AWS EC2 instance to run the suite in a clean, headless environment. Together these gave me a much better feel for how automated UI testing fits into a real development and CI workflow.

## Future Improvements
This first version keeps the structure deliberately simple, and there are a few things I would refine on the next project. I would adopt the **Page Object Model (POM)** to separate page locators and actions from the test logic, which makes the suite far easier to maintain as more pages are covered. I would also move from the current sequential browser loop to **true parallel execution** (for example with `pytest` + `pytest-xdist`), so all three browsers run at the same time and the suite finishes faster. Adding an HTML/Allure test report would also make the pass/fail results easier to review at a glance.
