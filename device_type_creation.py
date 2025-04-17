from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Start driver-a
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # 1. Login
    driver.get("https://demo.netbox.dev/login/")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("netboxdemo")
    driver.find_element(By.NAME, "password").send_keys("J7vZcfTKZbXcTnwm")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # 2. Navigation to "Add Device Type" page
    WebDriverWait(driver, 10).until(EC.url_contains("/home/"))
    driver.get("https://demo.netbox.dev/dcim/device-types/add/")

    # 3. Wait to appear form
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_model"))
    ).send_keys("AutoTestDevice")

    # 4. Click on "Create" button
    create_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(),'Create')]"))
    )
    create_btn.click()

    # 5. Check if page is changed
    WebDriverWait(driver, 10).until(EC.url_contains("/dcim/device-types/"))
    print("Device type successfully created!")

except Exception as e:
    print("Unexpected error:", e)
    driver.save_screenshot("screenshot_device_type_error.png")

finally:
    time.sleep(5)
    driver.quit()
