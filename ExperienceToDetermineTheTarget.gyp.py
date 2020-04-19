# -*-coding:Latin-1 -*
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from hashlib import sha512 
import json
import unicodedata
import time


#configure the chrome thing to have the extension within the drive 


chop = webdriver.ChromeOptions()

chop.add_extension('./archive.zip')

# create new Chrome driver object with blazemeter extension

driver = webdriver.Chrome(executable_path="./chromedriver",chrome_options=chop)


#this part is to upload the browser and then getting connected to the gmail account 
#we upload the file where we have the list of the channels we will be using for the study 


#driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com/")
time.sleep(2)

with open('fichier.json') as json_data:
    data_dict = json.load(json_data)   

#nous allons regarder max 60 videos sur chaque chaine
k = 0
i = 0
print ((k < 5000) & (i < len(data_dict)))
while ((k < 200) & (i < len(data_dict))):
    chaineName = data_dict[i]["nom"]
    chaineLink = data_dict[i]["link"]
    driver.get(chaineLink+"/videos")
    toutRegarder = driver.find_element_by_xpath('//paper-button[@class="style-scope ytd-button-renderer style-text size-default"]')
    toutRegarder.click()
    aleatoir = driver.find_element_by_xpath('//button[@class="style-scope yt-icon-button"]')
    if aleatoir.get_attribute('aria-pressed') == False :
        aleatoir.click()
    j=0
    time.sleep(2)
    curentChannelName = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-channel-name"]/a').get_attribute('innerHTML')
    curentChannelName = unicodedata.normalize('NFKD', curentChannelName).encode('ascii', 'ignore')
    while ((j < 3) & (chaineName == curentChannelName)):
        print ("intered")
        url = driver.current_url
        while driver.current_url == url : 
            print (j)
        j+=1
        k+=1
        driver.delete_all_cookies()
        curentChannelName = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-channel-name"]/a').get_attribute('innerHTML')
        curentChannelName = unicodedata.normalize('NFKD', curentChannelName).encode('ascii', 'ignore')
        print (curentChannelName)
    i+=1
print ("done")

driver.close()




# check /video of each link 
# check tout regarder 
#check how to control the number of videos that can be contained in each channel 
#move to the next channel 




     
    