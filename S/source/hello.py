from splinter import Browser
from selenium.webdriver.firefox.service import Service
from time import sleep
my_fox = Service(executable_path='./geckodriver')
browser = Browser('firefox', service = my_fox)
browser.visit("https://www.pythonanywhere.com/")
sleep(20)
browser.quit()
