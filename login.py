from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Credentials
username = "testuser123"
password = "Test1234!"

# Starting of Chrome
driver = webdriver.Chrome()
driver.get("https://demo.netbox.dev/")
print("Loading the page...")

wait = WebDriverWait(driver, 10)

try:
    # Click on Log In link in top right corner
    login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log In")))
    login_link.click()
    print("Click on 'Log In'")

    # Credentials typing
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
    print("Trying to login...")

    # Checking if login is successfull (Verifying if user name appears in headeru)
    time.sleep(3)
    if username in driver.page_source:
        print("Login successfull.")
    else:
        print("Login unsuccessfull. Creation of a new user...")

        # If login is not successfull, triggering user creation
        driver.get("https://demo.netbox.dev/users/login/")
        signup_link = driver.find_element(By.LINK_TEXT, "Sign up")
        signup_link.click()

        # Data input for registration
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[contains(text(),'Create & Sign In')]").click()
        print("New user created and logged in")

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except TimeoutException as e:
    print(f"Time for element waiting is expired: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    time.sleep(3)
    print("Closing the browser.")
    driver.quit()
