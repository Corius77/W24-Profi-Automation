from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import logins


W24 = "https://demo.warsztat24.com/"
ProfiAuto = "https://YOUR-LOCAL-STORE-NAME.profiauto.net/klient/archiwum"

w24_order_index = input("Podaj numer zlecenia: ")
profi_order_date = input("Podaj datę utworzenia zamówienia: ")


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")

w24_browser = webdriver.Chrome(options=options)
w24_browser.get(W24)

profi_browser = webdriver.Chrome(options=options)
profi_browser.get(ProfiAuto)

profi_id_input = profi_browser.find_element(By.ID, "login")
profi_id_input.send_keys(logins.profi_auto_id)

profi_password_input = profi_browser.find_element(By.ID, "password")
profi_password_input.send_keys(logins.profi_password, Keys.RETURN)

search_order = profi_browser.find_element(By.LINK_TEXT, profi_order_date)
search_order.click()

benchmark = profi_browser.find_element(By.XPATH, "//a[@class='p-form_back js-p_btn']")


w24_company_input = profi_browser.find_element(By.ID, "u_firma")
w24_company_input.send_keys(logins.w24_company)

w24_name_input = w24_browser.find_element(By.ID, "u_name")
w24_name_input.send_keys(logins.w24_name)

w24_password_input = w24_browser.find_element(By.ID, "haslo")
w24_password_input.send_keys(logins.w24_password, Keys.RETURN)

w24_order = w24_browser.find_element(By.LINK_TEXT, w24_order_index)


actions = ActionChains(w24_browser)
actions.move_to_element_with_offset(w24_order, 451, 19).click().perform()

add_position = w24_browser.find_element(By.ID, "short_cut_use_insert")
add_position.click()

print(w24_browser.current_url)

