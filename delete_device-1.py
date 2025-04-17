from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Start browser
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Test Data
DEVICE_NAME = "AutoTestDevice"
DEVICE_TYPE_NAME = "Test Device Type"

try:
    # 2. Go to device list page
    driver.get("https://demo.netbox.dev/dcim/devices/")
    driver.maximize_window()

    # 3. Search device by name
    search_input = wait.until(EC.presence_of_element_located((By.ID, "id_q")))
    search_input.send_keys(DEVICE_NAME)
    driver.find_element(By.XPATH, "//button[text()='Search']").click()

    # 4. Click on device on the list
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, DEVICE_NAME))).click()

    # 5. Click on "Delete" button
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete"))).click()

    # 6. Deletion confirm
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Yes, I’m sure')]"))).click()

    print(f"Device '{DEVICE_NAME}' successfully deleted.")

    # 7. Go to Device Types
    driver.get("https://demo.netbox.dev/dcim/device-types/")

    # 8. Search by name
    search_input = wait.until(EC.presence_of_element_located((By.ID, "id_q")))
    search_input.send_keys(DEVICE_TYPE_NAME)
    driver.find_element(By.XPATH, "//button[text()='Search']").click()

    # 9. Click on device type
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, DEVICE_TYPE_NAME))).click()

    # 10. Click on Delete
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Delete"))).click()

    # 11. Confirm
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Yes, I’m sure')]"))).click()

    print(f"Device Type '{DEVICE_TYPE_NAME}' successfully deleted.")

except Exception as e:
    print("It turns out an error:", str(e))

finally:
    time.sleep(5)
    driver.quit()
