from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import logins

ProfiAuto = "https://YOUR-LOCAL-STORE-NAME.profiauto.net/klient/archiwum"
profi_order_date = input("Podaj datę utworzenia zamówienia: ")

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

profi_browser = webdriver.Chrome(options=options)
profi_browser.get(ProfiAuto)

profi_browser = webdriver.Chrome(options=options)
profi_browser.get(ProfiAuto)

profi_id_input = profi_browser.find_element(By.ID, "login")
profi_id_input.send_keys(logins.profi_auto_id)

profi_password_input = profi_browser.find_element(By.ID, "password")
profi_password_input.send_keys(logins.profi_password, Keys.RETURN)

search_order = profi_browser.find_element(By.LINK_TEXT, profi_order_date)
search_order.click()

items_number = len(profi_browser.find_elements(By.XPATH, "(//td[@data-id='0'])"))

print(profi_browser.current_url)
print(items_number)