from selenium import webdriver
import time
import random
import string

NUMBER_OF_USERS = 10

driver = webdriver.Chrome("C:\\Chromedriver\\chromedriver.exe")
driver.get("http://joshmgrant.github.io/UserGenerator/login.html")

driver.find_element_by_id("username").send_keys("admin@testcorp.com")
driver.find_element_by_id("password").send_keys("p4zzW0Rd")
driver.find_element_by_name("login").click()

for i in range(NUMBER_OF_USERS):
    random_id = ''.join(random.choice(string.digits) for i in range(3))
    random_first = "user"
    random_last = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(5))
    random_email = random_first + random_last + "@testcorp.com"

    driver.find_element_by_id("userEmail").clear()
    driver.find_element_by_id("userEmail").send_keys(random_email)

    driver.find_element_by_id("userIdCode").clear()
    driver.find_element_by_id("userIdCode").send_keys(random_id)

    driver.find_element_by_id("newUserFirst").clear()
    driver.find_element_by_id("newUserFirst").send_keys(random_first)

    driver.find_element_by_id("newUserLast").clear()
    driver.find_element_by_id("newUserLast").send_keys(random_last)
    
    driver.find_element_by_id("newUserButton").click()

    time.sleep(2)

driver.quit()