# NetBox Rack Automation - Selenium Script

This repository contains a Python script that uses Selenium to automate the process of adding a device to a specific rack unit in the NetBox demo environment.

## What the Script Does

1. Opens the **rack detail page** in NetBox (`https://demo.netbox.dev/dcim/racks/39/`).
2. Switches to the embedded rack diagram (`iframe`) and selects **unit U10**.
3. Clicks on **"Create device"** in the popup modal.
4. Fills out the **device creation form** with:
   - Name: `AutoTestDevice`
   - Site: `Site 1`
   - Device Type: `Test Device Type`
   - Rack: `AMS01-Rack-1`
   - Position: `10`, Face: `Front`
5. Submits the form.
6. Confirms success by checking for the appearance of a success alert message.

## Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Selenium (`pip install selenium`)

## How to Run

1. Make sure `chromedriver.exe` is in the same directory or update the `driver_path` variable.
2. Install dependencies:
   ```bash
   pip install selenium
