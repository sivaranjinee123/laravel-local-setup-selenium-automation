from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://da.adlynk.in:8000/login")

print(driver.current_url)
print(driver.title)

wait = WebDriverWait(driver, 10)

email = ''.join(random.choices(string.ascii_lowercase, k=6)) + "@gmail.com"
password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

email_box = wait.until(EC.presence_of_element_located((By.ID, "email")))
password_box = wait.until(EC.presence_of_element_located((By.ID, "password")))

email_box.send_keys(email)
password_box.send_keys(password)

time.sleep(5)
driver.quit()
