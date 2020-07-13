from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome(r'/Users/sheyril/Downloads/chromedriver')

#to not log in every time script runs
options = Options()
options.add_argument("user-data-dir=/private/var/folders/x_/srprhlnd1xd53k70t9vh6dlw0000gn/T/.com.google.Chrome.Ao2MGJ/Default")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")

#time.sleep(1)
#wait = WebDriverWait(driver, 1200)

# recipient of the message (group/individual)
target = "das me"

# message to be sent
string = "Brush!"

inp_xpath_search = "//input[@title='Search or start new chat']"
wait = WebDriverWait(driver, 10)
time.sleep(2)
input_box_search = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="_3FRCZ copyable-text selectable-text"]')))
input_box_search.click()

time.sleep(2)
input_box_search.send_keys(target)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+target+"']")
selected_contact.click()

inp_xpath = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(string + Keys.ENTER)
time.sleep(2)

driver.close()
