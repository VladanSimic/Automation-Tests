from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set path to its chromedriver, if it's not working automatically
driver_path = "chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # 1. Go to rack page
    driver.get("https://demo.netbox.dev/dcim/racks/39/")
    driver.maximize_window()

    # 2. Wait for rack (iframe using)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    rack_iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(rack_iframe)

    # 3. Find free option on rack (e.c. click on U10)
    slot = wait.until(EC.element_to_be_clickable((By.ID, "unit-10-front")))
    slot.click()

    driver.switch_to.default_content()

    # 4. Wait for dialog for device addition
    wait.until(EC.visibility_of_element_located((By.ID, "modal")))

    # 5. Click on "Create device"
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create device"))).click()

    # 6. Populate the form on device creation page
    wait.until(EC.presence_of_element_located((By.ID, "id_name")))
    driver.find_element(By.ID, "id_name").send_keys("AutoTestDevice")

    # Select site
    site_dropdown = driver.find_element(By.ID, "id_site")
    site_dropdown.click()
    site_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Site 1')]").click()

    # Select device type
    device_type_dropdown = driver.find_element(By.ID, "id_device_type")
    device_type_dropdown.click()
    device_type_dropdown.find_element(By.XPATH, "//option[contains(text(), 'Test Device Type')]").click()

    # Select rack
    rack_dropdown = driver.find_element(By.ID, "id_rack")
    rack_dropdown.click()
    rack_dropdown.find_element(By.XPATH, "//option[contains(text(), 'AMS01-Rack-1')]").click()

    # Type position - 10 and "front"
    driver.find_element(By.ID, "id_position").send_keys("10")
    driver.find_element(By.ID, "id_face").send_keys("Front")

    # Click on Save
    driver.find_element(By.XPATH, "//button[contains(text(), 'Create')]").click()

    # 7. Success confrim
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
    print("The device is successfully added.")

except Exception as e:
    print("Test unsuccessfull:", str(e))

finally:
    time.sleep(5)
    driver.quit()
