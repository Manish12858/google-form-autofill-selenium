from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium 4.6+ downloads the matching ChromeDriver automatically (Selenium Manager),
# so no hard-coded driver path is needed.
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeQvVOm_I11CAcX6_eMrnFWjjG-UKs0F30eQqbuczfufeLQeg/viewform")
time.sleep(5)
my_details = ["Manish", "Kumar", "manishkumarnit3@gmail.com"]
inputs = driver.find_elements(by=By.CLASS_NAME, value="whsOnd.zHQkBf")

for i in range(len(my_details)):
    inputs[i].send_keys(my_details[i])
submit = driver.find_element(by=By.CLASS_NAME, value="NPEfkd.RveJvd.snByac")
submit.click()
time.sleep(5)
driver.quit()
