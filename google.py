from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome(r"C:\Users\Tamara\Desktop\chromedriver.exe")
queries = ["baba","zaba","ignjat","nika"]

driver.get("http://google.com")

driver.find_element_by_name("q").send_keys(random.choice(queries))

driver.find_element_by_name("q").send_keys(Keys.ENTER)

driver.maximize_window()
driver.minimize_window()
driver.refresh()

driver.quit()