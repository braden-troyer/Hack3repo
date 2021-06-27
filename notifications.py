#Notification with typelog data

import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC
import csv
from os.path import exists
#let there is no data initially

instance = []
index = []
keys_pressed = []

filename = "statistics.csv"

if exists(filename):        
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            if counter == 0:
                counter += 1
            else:
                instance.append(int(row[0]))
                index.append(int(row[1]))
                keys_pressed.append(int(row[2]))

def average(args):
    counter = 0
    total = 0
    for i in range(len(args)):
        total += int(args[i])
        counter += 1
    return total // counter


average_keys = average(keys_pressed)


productData = None
#try:
    #insert our file here to retrieve data
    #productData = requests.get("https://corona-rest-api.herokuapp.com/Api/singapore")
#except:
    #if the data is not fetched due to lack of internet or other problem
    #print("Please relaunch the application")
#if data is fetched
if not productData:
    #converting data into JSON format
    data = productData.json()['Success']
    
    #repeating the loop for multiple times
    while(True):
        notification.notify(
            #title of the notification,
            title = "Productivity Stats {}".format(datetime.date.today()),
            #the body of the notification

        
            message = "Average Keys Pressed : [average_keys]\nTotal Keys Pressed : [total]"
            #.format(
                        #totalcases = data['cases'],
                        #todaycases = data['todayCases'],
                        #todaydeaths = data['todayDeaths'],
                        #active = data["active"]),  


            
            #we need to download a icon of ico file format
            app_icon = r'C:/Users/user/Downloads/hack3.ico',
            # the notification stays for 30sec
            timeout = 30
        )
        #notification repeats after every 1hrs
        time.sleep(60*60*1)
