import os
import sys
import re
import argparse

try:
    import bs4
except:
    os.system('pip3 install bs4')

try:
   import selenium
except:
    os.system('pip3 install selenium')
     
try:
    import pathlib
except:
    os.system('pip3 install pathlib')

from pathlib import Path
from selenium import webdriver


if  len(sys.argv) != 2:
    print("Invalid count of arguments inserted\nInsert only SteamID to run script properly")
    sys.exit(1)

PATH_FOLDER = Path(r'./')

parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()
    
url = 'https://steamcommunity.com/id/'+ args.name +'/games'

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

profile = webdriver.FirefoxProfile()
profile.set_preference("permissions.default.image", 2)

driver = webdriver.Firefox(options = options, firefox_profile=profile)
driver.get(url)   
driver.execute_script("document.head.parentNode.removeChild(document.head)")

html = driver.page_source
soup = bs4.BeautifulSoup(html, 'html.parser')

lol = soup.find_all(class_="gameListRowItem")
driver.quit()

totalRecentHours = 0.00

print("------------------------------------------------------")

for f in lol:
    weee = f.find(class_="hours_played")

    if weee.string:

        try:
            hours = weee.string.split("/")
            if not hours[1]:
                continue
            recentHours = hours[0].split(' ', 1)[0]
        except:
            continue

        print("| " , f.find(class_="gameListRowItemName").string) 

        print("| " , recentHours + "h\n------------------------------------------------------")

        totalRecentHours = totalRecentHours + float(recentHours)

if totalRecentHours > 0:  
    print("\n| Total hours in recent 2 weeks on Steam spent by playing games:\n| " , totalRecentHours)
else:
    print("\n| Not-existing SteamID or No record of playing games on Steam for last 2 weeks.")
