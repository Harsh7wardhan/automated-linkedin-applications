from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path="C:\development\chromedriver_win32\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2677415966&f_WRA=true&geoId=102713980")
sign_up=driver.find_element_by_xpath("/html/body/div[1]/header/nav/div/a[2]")
sign_up.click()

time.sleep(3)

mail=driver.find_element_by_id("username")
mail.send_keys("mcgregordwayne2000@gmail.com")
password=driver.find_element_by_id("password")
password.send_keys("aldo13sec")
enterrok=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
enterrok.send_keys(Keys.ENTER)


apply=driver.find_element_by_css_selector(".jobs-s-apply button")
apply.send_keys(Keys.ENTER)
phone=driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2677415966,9,phoneNumber~nationalNumber)"]')
phone.send_keys("8167216562")

submit=driver.find_element_by_xpath('//*[@id="ember365"]')
submit.send_keys(Keys.ENTER)