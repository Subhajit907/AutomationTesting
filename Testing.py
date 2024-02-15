from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Replace with your credentials
username = "ga-engineer-assignment@test.com"
password = "Qapasswordi23$"

# Define the URL and target element
url = "https://app.tryloop.ai/chargebacks/stores/view"
grand_total_element_xpath = "//div[@class='ant-table-tfoot ant-table-footer']//th[last()]"

def login(driver):
    """Logs in to the Tryloop platform"""
    driver.get("https://app.tryloop.ai/login/password")
    driver.find_element("xpath","//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq']").send_keys(username)
    driver.find_element("xpath","//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']").send_keys(password)
    driver.find_element("xpath","//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-disableElevation MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-disableElevation MuiButton-fullWidth css-1rijiyb']").click()


def get_store_data(driver):
    """Extracts store data from the table"""
    rows = driver.find_elements("xpath", "(//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-m09714-MuiTypography-root'])[2]")
    store_data = []
    for row in rows:
        store_name = row.find_element(By.XPATH, "(//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-u2nh6v'])[1]").text
        monthly_data = [float(cell.text.replace("$", "")) for cell in row.find_elements(By.XPATH, "(//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-u2nh6v'])[2]")]
        store_data.append((store_name, monthly_data))
    return store_data

def calculate_grand_total(store_data):
    """Calculates the grand total for each month"""
    grand_totals = [0] * len(store_data[0][1])
    for store_name, monthly_data in store_data:
        for i, value in enumerate(monthly_data):
            grand_totals[i] += value
    return grand_totals

def verify_grand_totals(driver, expected_totals):
    """Verifies if the displayed grand totals match the calculated values"""
    grand_total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", grand_total_element_xpath))
    )
    displayed_totals = [float(cell.text.replace("$", "")) for cell in grand_total_element.find_elements("xpath", "(//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-u2nh6v'])[92]")]
    for i, (expected, displayed) in enumerate(zip(expected_totals, displayed_totals)):
        if abs(expected - displayed) > 0.01:
            print(f"Error: Grand total mismatch for month {i+1}. Expected: ${expected:.2f}, Displayed: ${displayed:.2f}")
        else:
            print(f"Grand total for month {i+1} matches: ${expected:.2f}")

def take_screenshot(driver, filename):
    """Takes a screenshot of the browser window"""
    driver.save_screenshot(filename)

def main():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    store_data = get_store_data(driver)
    expected_totals = calculate_grand_total(store_data)

    verify_grand_totals(driver, expected_totals)

    take_screenshot(driver, "tryloop_data_verification.png")

    driver.quit()

if __name__ == "__main__":
    main()
