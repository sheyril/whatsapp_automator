# whatsapp_automator
This is a simple python script to automate sending WhatsApp messages. You can also schedule messages as per your needs using the scheduler script or if you're on a Unix-like system, you can make use of Cron.

## Installation
1. First, make sure you're running the script using python3

2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Selenuim.
```bash
pip install selenium 
```
3. To download chromedriver, you can use [pip](https://pip.pypa.io/en/stable/). However, to avoid running into compatibility errors, go to [ChromeDriver](https://chromedriver.chromium.org/downloads) and download according to your Chrome version.

4. If you're using schedule.py to run the script periodically, install the Python library Scheduler using [pip](https://pip.pypa.io/en/stable/)
```bash
pip install schedule 
```
## Usage 

### Using Schedule
Run scheduler.py using python3 from the terminal.
For more information on the Schedule library, visit [docs](https://schedule.readthedocs.io/en/stable/)

### Using CronTab
Open the CronTab editor using 
```bash
crontab -e
```
If this is your fist cron file, you'll have to add in a few extra commands 
```
SHELL=/bin/bash
PATH=/usr/local/bin/:/usr/bin:/usr/sbin
```
Now add in the command to schedule the script. For example, if you want to run the script at 12:30 PM everyday,
```
30 12 * * * cd <path to directory containing script> && <path to python3> whatsapp.py >/tmp/stdout.log 2>/tmp/stderr.log
```
For more information on how to set up cron jobs, check out [docs](https://man7.org/linux/man-pages/man5/crontab.5.html) or [opensource](https://opensource.com/article/17/11/how-use-cron-linux) 
