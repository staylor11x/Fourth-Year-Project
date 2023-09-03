
from datetime import datetime
import os

class Event():

    '''
    implementation of a class to represent and Proccess A&T events

    '''

    def __init__(self, Tag, Descrp, Trip, Pri, Alarm, Time):
        '''initilise attributes'''
        self.Tag = Tag          #tag number for sensor
        self.Descrp = Descrp    #description of alarm 
        self.Trip = Trip        #trip lvl for sensor i.e LL/HH
        self.Pri = Pri          #Alarm priority
        self.Alarm = Alarm      #alarm state high/low
        self.Time = Time        #timestamp for when alarm recieved by DCS

    def __str__(self):
        return str(self.Tag) + "..." + self.Descrp + "..." +str(self.Trip) + "..." + str(self.Pri) + "..." + str(self.Alarm) + "..." + str(self.Time)

    def Archive(self):
        '''Archive the event to the history module'''
        #get the current date and time so the each file represents a new day
        now = datetime.now()
        date_str = now.strftime("%d-%m-%Y")
        #split the date and time parameters 
        datetimesplit = str(self.Time).split()

        #if the file does not already exist apply header formatting then data
        #else just apply data
        if not(os.path.exists("History Modules\HistoryModule - {}.csv".format(date_str))):
            with open("History Modules\HistoryModule - {}.csv".format(date_str), "a")as f:
                f.write("TagNO" + "," + "Description" + "," + "Trip Level" + "," + "High/Low" 
                + "," + "Date" + "," + "Time" + "\n" )
                f.write(self.Tag + "," + self.Descrp + "," + self.Trip + "," + str(self.Alarm) 
                + "," + datetimesplit[0] + "," + datetimesplit[1] + "\n" )
                f.close()
        else:   
            with open("History Modules\HistoryModule - {}.csv".format(date_str), "a")as f:
                f.write(self.Tag + "," + self.Descrp + "," + self.Trip + "," + str(self.Alarm) 
                + "," + datetimesplit[0] + "," + datetimesplit[1] + "\n" )
                f.close()   

    def WarningMsg(self):
        """function to determine what the priority of the alarm is and based on this 
        send message to operator"""

        if(self.Pri == 4):
            #not technically an alarm as the operator cannot do anything
            #send alarm to special queue
            return ("!!!Warning Critical priority alarm ESD on module {}!!!\n".format(self.Tag))
        elif((self.Pri ==1) or (self.Pri ==2) or (self.Pri == 3)):
            #these are the alarms that will show up on the operators console
            return ("Warning level {} alarm on module {}\n".format(self.Pri, self.Tag))
        else:
            #events will not show up on the operators main console
            return ("Event Logged\n")


        