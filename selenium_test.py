from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Call google page
browser = webdriver.Safari()
browser.implicitly_wait(60)
browser.get("https://www.google.co.th/")
browser.implicitly_wait(60)
browser.quit()
## Success to test