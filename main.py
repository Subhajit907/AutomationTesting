# selenium 4
import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the login page
driver.get("https://app.tryloop.ai/login/password")
driver.find_element("xpath","//input[@class='MuiInputBase-input MuiOutlinedInput-input css-1x5jdmq']").send_keys("qa-engineer-assignment@test.com")
driver.find_element("xpath","//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2']").send_keys("QApassword123$")
driver.find_element("xpath","//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-disableElevation MuiButton-fullWidth MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeLarge MuiButton-containedSizeLarge MuiButton-disableElevation MuiButton-fullWidth css-1rijiyb']").click()

get_title = driver.title
if get_title == "Login | Loop app":
 print("Login Successfull")
def verify_grand_totals():
 # Navigate to the URL
 driver.get("https://app.tryloop.ai/chargebacks/stores/view")

 # Loop through each month column
 for month_index in range(1, 8):
  # Find all store names
  store_names = driver.find_elements("xpath","(//h6[@class='MuiTypography-root MuiTypography-subtitle2 css-m09714-MuiTypography-root'])[8]")
  # Find the grand total for the month
  #grand_total = driver.find_element("xpath",f"//th[contains(text(), 'Month')]/following-sibling::th[{month_index}]/following-sibling::td[last()]")
  # Calculate the sum of store values
  #sum_values = sum(float(store.text.replace('$', '')) for store in store_names)
  # Convert grand total to float
  #grand_total_value = float(grand_total.text.replace('$', ''))
  # Verify if sum matches grand total
  #if sum_values == grand_total_value:
  # print(f"Month {month_index}: Sum matches Grand Total: {sum_values}")
  #else:
  # print(f"Month {month_index}: Sum does not match Grand Total: Sum = {sum_values}, Grand Total = {grand_total_value}")


# Call the function
verify_grand_totals()






