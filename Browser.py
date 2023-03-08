from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class Browser:
    def __init__(self, url)                                         #Settings of the Browser.
        self.options = Options()
        self.options.add_argument("--window-size=1936,1056")
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=self.options)
        self.url = url

    def Open(self):                                                 #Method to open url.
        self.browser.get(self.url)

google = "http://google.com"

test = Browser(google)                                              #Testing opening browser with google url
test.Open()

