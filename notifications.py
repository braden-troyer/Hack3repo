#Notification with typelog data

import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC
#let there is no data initially

producData = None
try:
    #insert our file here to retrieve data
    productData = requests.get("https://corona-rest-api.herokuapp.com/Api/singapore")
except:
    #if the data is not fetched due to lack of internet or other problem
    print("Please relaunch the application")
#if data is fetched
if (productData != None):
    #converting data into JSON format
    data = productData.json()['Success']
    
    #repeating the loop for multiple times
    while(True):
        notification.notify(
            #title of the notification,
            title = "Productivity Stats {}".format(datetime.date.today()),
            #the body of the notification
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),  
            #we need to download a icon of ico file format
            app_icon = r'C:/Users/user/Downloads/hack3.ico',
            # the notification stays for 30sec
            timeout  = 30
        )
        #notification repeats after every 1hrs
        time.sleep(60*60*1)
