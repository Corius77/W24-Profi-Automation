from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:
    def __int__(self):
        self.options = Options()                                    #Settings of the Browser
        self.options.add_argument("--window-size=1936,1056")
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=self.options)

    def Open(self, url):                                            #Method to open url
        self.browser.get(url)

test = Browser()
google = "http://google.com"                                        #Testing opening browser with google url
test.Open(google)

