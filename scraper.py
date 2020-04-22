import os
import sys
import re
import argparse
import subprocess



#print(sys.platform)

if sys.platform == "linux":

	#os.system('sudo cp geckodriver /usr/local/bin')
	a = subprocess.Popen(["dpkg", "-l", "firefox-geckodriver"], stdout=subprocess.PIPE)
	a.communicate()[0]
	if a.returncode != 0:
		print("installing firefox-geckodriver")
		os.system('sudo apt-get install firefox-geckodriver >> /dev/null')


try:

    import bs4

except:

    print("\n\tbs4 not found, using pip3 to install module\n\n")

    os.system('pip3 install bs4')


try:

   import selenium

except:

    print("\n\tSelenium not found, using pip3 to install module\n\n")

    os.system('pip3 install selenium')

     
try:

    import pathlib

except:

    print("\n\tpathlib not found, using pip3 to install module\n\n")

    os.system('pip3 install pathlib')


import bs4

from pathlib import Path

from selenium import webdriver





if  len(sys.argv) != 2:

    print("Invalid count of arguments inserted\nInsert only SteamID to run script properly")

    sys.exit(1)



PATH_FOLDER = Path('./')



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



print("\n\n------------------------------------------------------")



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



        print("| " , recentHours , "h\n------------------------------------------------------")



        totalRecentHours = totalRecentHours + float(recentHours)





print("\n\n------------------------------------------------------")

if totalRecentHours > 0:  

    print("| Total hours in recent 2 weeks on Steam spent by playing games:\n| " , totalRecentHours,"h")

else:

    print("| Not-existing SteamID or No record of playing games on Steam for last 2 weeks.")

print("------------------------------------------------------")