from splinter import Browser
from selenium.webdriver.firefox.service import Service
from time import sleep
my_fox = Service(executable_path='./geckodriver')
browser = Browser('firefox', service = my_fox)

browser.visit("https://www.python.org/")
li_elements = browser.find_by_css("li")
for element in li_elements:
    print(f"Text: {element.text}")
    print(f"Value: {element.value}")
browser.quit()
