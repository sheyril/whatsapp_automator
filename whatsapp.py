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

wait = WebDriverWait(driver, 600)

# recipient of the message (group/individual)
target = '"das me"'

# message to ne sent
string = "sit up straight"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
By.XPATH, x_arg)))
print (group_title)
print ("Sending message")
group_title.click()
message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

message.send_keys(string)
sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
sendbutton.click()
driver.close()