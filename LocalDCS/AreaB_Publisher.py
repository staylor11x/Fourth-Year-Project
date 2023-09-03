import paho.mqtt.client as mqtt
import random
import time
import pandas as pd

def FindTripLvl(number):
    '''func to find the trip level based on its potision in the df'''
    if number == 2:
        return "LL"    
    elif number == 3:
        return "L"
    elif number == 4:
        return "H"
    elif number == 5:
        return "HH"

#create link to broker
mqttBroker = "localhost"
BrokerPort = 1883
client = mqtt.Client("Process_Data")
client.connect(mqttBroker, BrokerPort)

#read in F&G test data from excel
File_name = "Alarm Test Data Format.xlsx"
df = pd.read_excel(File_name, sheet_name = 'AreaB')
print(df)

#non random test data
for i in range(len((df))):
    
    row = df.iloc[i]

    #convert row to array
    array = row.to_numpy()

    #for the current test data just use the last column
    #select a random column from the row to use as the alarm 
    number = random.randint(2,5)    
    Priority = (array[number])
    #Priority = (array[5])   #remember and change FindTripLvl paremeter too!!
    if  not(pd.isna(Priority)):
        #remove anything after the decimal point in priority in order to make int (save space)
        Str_priority = str(Priority)
        Priority = Str_priority.split(".")[0]
        #get the trip level based on this
        TripLvl = FindTripLvl(number)
        TagNo = array[0]
        Descrp = array[1]
        Alarm = random.randint(0,1)         #is the alarm high or low?
        #create message and publish 
        msg = (TagNo + "," + Descrp + "," + TripLvl + "," + str(Priority) + "," + str(Alarm))
        client.publish("AreaB", msg)
        print("{} - {}: {}: Priority {}".format(Alarm, TagNo, TripLvl, Priority)) 
        #sleeptime = random.randint(1,5)
        sleeptime = random.randint(1,5)
        time.sleep(sleeptime)
###create some test data to send - this loop will run forever
#while True:
#
#    #sample a random row
#    i = random.randint(1,(len(df)-1))
#    random_row = df.iloc[i]
#
#    #convert row to array 
#    array = random_row.to_numpy()
#
#    #select a random column from the row to use as the alarm 
#    number = random.randint(2,5)    
#    Priority = (array[number])
#
#    #if the chosen priority actually exists within the test data
#    if  not(pd.isna(Priority)):
#
#        #remove anything after the decimal point in priority in order to make int (save space)
#        Str_priority = str(Priority)
#        Priority = Str_priority.split(".")[0]
#
#        #get the trip level based on this
#        TripLvl = FindTripLvl(number)
#        
#        TagNo = array[0]
#        Descrp = array[1]
#        Alarm = random.randint(0,1)         #is the alarm high or low?
#
#        #create message and publish 
#        msg = (TagNo + "," + Descrp + "," + TripLvl + "," + str(Priority) + "," + str(Alarm))
#        client.publish("TEMPERATURE", msg)
#        print("{} - {}: {}: Priority {}".format(Alarm, TagNo, TripLvl, Priority)) 
#        sleeptime = random.randint(1,5)
#        time.sleep(sleeptime)
#
#    else:
#        continue