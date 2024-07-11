from splinter import Browser
from selenium.webdriver.firefox.service import Service
from os import getenv
from time import sleep
RTUSER = getenv('RTUSER')
RTPASS = getenv('RTPASS')

if not RTUSER or not RTPASS:
    raise SystemExit("Sorry could not grab the credentials!")

my_fox = Service(executable_path='./geckodriver')
browser = Browser('firefox',service = my_fox, headless = True)
browser.visit('http://192.168.50.1')
browser.fill('login_username', RTUSER)
browser.fill('login_passwd',RTPASS)
button = browser.find_by_xpath('/html/body/form/div/div/div[3]/div[9]')
button.click()
browser.find_by_xpath('//*[@id="Advanced_WAN_Content_menu"]').click()
browser.find_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td[6]/div/div").click()
browser.find_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[16]/td/div[5]/input").click()
sleep(3)
browser.quit()

