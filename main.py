from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import logins


W24 = "https://demo.warsztat24.com/"
ProfiAuto = "YOUR_LOCAL_PROFI_AUTO_URL"

w24_order_index = input("Podaj numer zamówienia: ")


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)
browser.get(W24)


w24_company_input = browser.find_element(By.ID, "u_firma")
w24_company_input.send_keys(logins.w24_company)

w24_name_input = browser.find_element(By.ID, "u_name")
w24_name_input.send_keys(logins.w24_name)

w24_password_input = browser.find_element(By.ID, "haslo")
w24_password_input.send_keys(logins.w24_password, Keys.RETURN)

w24_order = browser.find_element(By.LINK_TEXT, w24_order_index)


actions = ActionChains(browser)
actions.move_to_element_with_offset(w24_order, 451, 19).click().perform()

print(browser.current_url)

