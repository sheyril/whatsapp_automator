import schedule
import time
import os

def job():
	os.system("python3 whatsapp.py")


# schedule.every(1).minutes.do(job)
schedule.every().day.at("22:12").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)