import schedule
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def job():
	driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')
	options = Options()
	options.add_argument("user-data-dir=/tmp/sheyril")
	driver = webdriver.Chrome(chrome_options=options)
	driver.get("https://web.whatsapp.com/")
	wait = WebDriverWait(driver, 600)
	target = '"das me"'
	string = "brush"

	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
	print (group_title)
	print ("Wait for few seconds")
	group_title.click()
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

	message.send_keys(string)
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()
	driver.close()


# schedule.every(15).seconds.do(job)
schedule.every().day.at("22:12").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)