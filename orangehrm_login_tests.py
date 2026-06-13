# ----------------------------------------------------------
# OrangeHRM Login Functionality - Selenium WebDriver Tests
# Cross-browser: Chrome, Edge, Firefox
# Accounts: Admin and Standard User
# ----------------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ----------------------------------------------------------
# WebDriver Factory Functions
# ----------------------------------------------------------
def create_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def create_edge():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Edge(options=options)


def create_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    return webdriver.Firefox(options=options)


# ----------------------------------------------------------
# Login Test
# ----------------------------------------------------------
def run_login_test(driver, base_url, username, password, account_label):
    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, 20)

        # Enter username
        user_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        user_field.clear()
        user_field.send_keys(username)

        # Enter password
        pass_field = driver.find_element(By.NAME, "password")
        pass_field.clear()
        pass_field.send_keys(password)

        # Click login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Verify successful login by waiting for the dashboard header
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Dashboard']")
            )
        )
        print(f"PASS: {account_label} login succeeded.")
    except Exception as error:
        print(f"FAIL: {account_label} login failed -> {error}")
    finally:
        time.sleep(2)
        driver.quit()


# ----------------------------------------------------------
# Main Execution
# ----------------------------------------------------------
if __name__ == "__main__":
    base_url = "https://opensource-demo.orangehrmlive.com/"

    # Admin credentials
    admin_user = "Admin"
    admin_pass = "admin123"

    # Standard user credentials
    standard_user = "Jaredp01"
    standard_pass = "Orange123!"

    browsers = [
        ("Chrome", create_chrome),
        ("Edge", create_edge),
        ("Firefox", create_firefox),
    ]

    for browser_name, browser_func in browsers:
        print(f"\n--- Running tests in {browser_name} ---")

        # Admin login test
        run_login_test(browser_func(), base_url, admin_user, admin_pass, "Admin")

        # Standard user login test
        run_login_test(browser_func(), base_url, standard_user, standard_pass, "Standard User")
