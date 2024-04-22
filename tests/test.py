from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Only for the first time :
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(50)
driver.get("https://app.wzone.io/")
driver.find_element(By.XPATH, "//a[@href='/sign-in']").click()
sleep(20)

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (assuming Chrome)
#driver = webdriver.Chrome()

# Navigate to your web page
## driver.get("https://app.wzone.io/")

# Find and click on the element that triggers the sign-in with Google modal
google_sign_in_button = driver.find_element(By.ID, 'buttonDiv').click()

# Switch to the Google sign-in modal dialog
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait for the modal to appear
main_window_handle = driver.window_handles[0]
google_sign_in_window_handle = driver.window_handles[1]
driver.switch_to.window(google_sign_in_window_handle)

# Enter Google account credentials
#email_input = driver.find_element_by_id("identifierId")
#email_input.send_keys("your_email@gmail.com")

#next_button = driver.find_element_by_id("identifierNext")
#next_button.click()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
#password_input = driver.find_element_by_name("password")
#password_input.send_keys("your_password")

#password_next_button = driver.find_element_by_id("passwordNext")
#password_next_button.click()

# Handle authorization if needed
# (e.g., granting permission for your application to access Google account data)

# Switch back to the main window
#driver.switch_to.window(main_window_handle)

# Continue with the rest of your automation flow

# driver.quit()