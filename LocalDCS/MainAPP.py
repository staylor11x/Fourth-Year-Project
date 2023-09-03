from MainMenu import Ui_MainWindow
from ListView import Ui_MainWindow as ListUi
from loginbox import Ui_Form as LoginUi
from MapView import Ui_MainWindow as MapViewUi
from AreaB_View import Ui_MainWindow as AreaBUi
from AreaA_View import Ui_MainWindow as AreaAUi
from AreaBPA1_View import Ui_MainWindow as AreaBPA1Ui
from Level4View import Ui_Form as Level4Ui

from PriorityQueue import PriQueue
from P4Queue import P4Queue
from EventQueue import EventQueue
from EventObj import Event

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import subprocess
import sys
from threading import Thread
from datetime import datetime
import time
import pickle
import paho.mqtt.client as mqtt
import sqlite3

#create database to store user login information (temporary)
users = {
    "Engineer"  :("ENGPASS", "ENG"),
    "CRO"       :("CROPASS", "CRO"),
    "Admin"     :("ADMINPASS", "ADM"),
}


def sendQueue(E):
    '''send data to the relevant queue/list'''
    #this could potentially be moved to the object class
    if(E.Pri == 4):
        #add item to p4 queue
        P4Q.Enqueue(E)
        #print(P4Q)
    elif(E.Pri == 0):
        #add item to the event list
        EQ.Enqueue(E)
        #print(EQ)
    else:
        #if the alarm is an alarm, add it to the priority queue
        PQ.Enqueue(E)
        print(PQ)
            


def on_message(client, userdata, message):
    '''callback function to print out the message/store message as an object'''
            
    #refresh = qtc.pyqtSignal(bool)

    #apply date and time to event
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
    
    #decode message and create event object
    RecievedMsg = str(message.payload.decode("utf-8"))
    print("Recieved message", RecievedMsg)
    splitline = RecievedMsg.split(',')
    E = Event(splitline[0], splitline[1], splitline[2], int(splitline[3]), int(splitline[4]), timestamp)

    #send data to relevant queue 
    sendQueue(E)

    #emit signal to refresh GUI (work in progress)
    #refresh.emit(True)

    #send the data to the processing module
    data = pickle.dumps(E)
    command = "Processing.py"
    pipe = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    pipe.stdin.write(data)
    pipe.stdin.close()
    #pipe.wait()


def Thread1():
    '''this thread runs the data aquisition'''

    '''open the publisher file(s)'''
    #subprocess.Popen(["python","FG_Publisher.py"])
    #subprocess.Popen(["python","Random_Publisher.py"])
    #subprocess.Popen(["python","Process_Publisher.py"])
    subprocess.Popen(["python", "AreaA_Publisher.py"])
    subprocess.Popen(["python", "AreaB_Publisher.py"])

    #create link to broker
    mqttBroker = "localhost"
    BrokerPort = 1883
    client = mqtt.Client("Smartphone")
    client.connect(mqttBroker,BrokerPort)

    client.on_message = on_message

    client.subscribe("AreaA")
    client.subscribe("AreaB")

    '''start loop for listening'''
    client.loop_forever()
    #no commands can be executed after this statement!!

def Thread2():
    '''This thread runs the main GUI app'''

    app = MainApp(sys.argv)
    
    sys.exit(app.exec())
    #no commands executed after this

class MainApp(qtw.QApplication):
    '''The Main application object'''

    def __init__(self, argv):
        super().__init__(argv)

        ##create and show Login window
        self.LoginWindow = LoginWindow()
        self.LoginWindow.show()

        #create other windows
        self.MainMenuWindow = MainMenuWindow()
        self.ListViewWindow = ListViewWindow()
        self.MapViewWIndow  = MapViewWindow()
        self.AreaB_ViewWindow = AreaBViewWindow()
        self.AreaA_ViewWindow = AreaAViewWindow()
        self.AreaBPA1_ViewWindow = AreaBPA1ViewWindow()
        self.Level4_ViewWindow = Level4View()

        #self.AreaB_ViewWindow.show()
        #self.AreaBPA1_ViewWindow.show()
        ##self.MainMenuWindow.show()
        #self.ListViewWindow.show()
        #self.AreaA_ViewWindow.show()
        

        #button logic
        self.LoginWindow.Login_submitted.connect(self.MainMenuWindow.show)
        self.LoginWindow.Permission_Lvl.connect(self.MainMenuWindow.Login)

        self.MainMenuWindow.ListView_requested.connect(self.ListViewWindow.show)
        #self.MainMenuWindow.ListView_requested.connect(self.MainMenuWindow.hide)
        self.MainMenuWindow.LoginRequested.connect(self.LoginWindow.show)
        self.MainMenuWindow.MapView_requested.connect(self.MapViewWIndow.show)
        #self.MainMenuWindow.MapView_requested.connect(self.MainMenuWindow.hide)    

        self.ListViewWindow.MainMenuWindow_requested.connect(self.MainMenuWindow.show)
        #self.ListViewWindow.MainMenuWindow_requested.connect(self.ListViewWindow.close)
        self.ListViewWindow.MapViewWindow_requested.connect(self.MapViewWIndow.show)
        #self.ListViewWindow.MapViewWindow_requested.connect(self.ListViewWindow.close)
        self.ListViewWindow.Level4View_requested.connect(self.Level4_ViewWindow.GetInfo)
        self.ListViewWindow.Level4View_requested.connect(self.Level4_ViewWindow.show)
        
        self.MapViewWIndow.MainMenuWindow_requested.connect(self.MainMenuWindow.show)
        #self.MapViewWIndow.MainMenuWindow_requested.connect(self.MapViewWIndow.close)
        self.MapViewWIndow.ListViewWindow_requested.connect(self.ListViewWindow.show)
        #self.MapViewWIndow.ListViewWindow_requested.connect(self.MapViewWIndow.hide)
        self.MapViewWIndow.AreaBViewWindow_requested.connect(self.AreaB_ViewWindow.show)
        #self.MapViewWIndow.AreaBViewWindow_requested.connect(self.MapViewWIndow.hide)
        self.MapViewWIndow.AreaAViewWindow_requested.connect(self.AreaA_ViewWindow.show)
        #self.MapViewWIndow.AreaAViewWindow_requested.connect(self.MapViewWIndow.hide)

        self.AreaB_ViewWindow.MainMenuWindow_requested.connect(self.MainMenuWindow.show)
        #self.AreaB_ViewWindow.MainMenuWindow_requested.connect(self.AreaB_ViewWindow.hide)
        self.AreaB_ViewWindow.ListViewWindow_requested.connect(self.ListViewWindow.show)
        #self.AreaB_ViewWindow.ListViewWindow_requested.connect(self.AreaB_ViewWindow.close)
        self.AreaB_ViewWindow.MapViewWindow_requested.connect(self.MapViewWIndow.show)
        #self.AreaB_ViewWindow.MapViewWindow_requested.connect(self.AreaB_ViewWindow.close)
        self.AreaB_ViewWindow.AreaBPA1ViewWindow_reuested.connect(self.AreaBPA1_ViewWindow.show)
        #self.AreaB_ViewWindow.AreaBPA1ViewWindow_reuested.connect(self.AreaB_ViewWindow.hide)

        self.AreaBPA1_ViewWindow.MainMenuWindow_requested.connect(self.MainMenuWindow.show)
        #self.AreaBPA1_ViewWindow.MainMenuWindow_requested.connect(self.AreaBPA1_ViewWindow.close)
        self.AreaBPA1_ViewWindow.Level4View_requested.connect(self.Level4_ViewWindow.show)
        self.AreaBPA1_ViewWindow.Level4View_info.connect(self.Level4_ViewWindow.GetInfo)
        self.AreaBPA1_ViewWindow.MapView_requested.connect(self.MapViewWIndow.show)
        #self.AreaBPA1_ViewWindow.MapView_requested.connect(self.AreaBPA1_ViewWindow.close)
        self.AreaBPA1_ViewWindow.ListView_requested.connect(self.ListViewWindow.show)
        #self.AreaBPA1_ViewWindow.ListView_requested.connect(self.AreaBPA1_ViewWindow.close)
        self.AreaBPA1_ViewWindow.Back_requested.connect(self.AreaB_ViewWindow.show)
        #self.AreaBPA1_ViewWindow.Back_requested.connect(self.AreaBPA1_ViewWindow.close)

        self.Level4_ViewWindow.removedItem.connect(self.AreaBPA1_ViewWindow.RemoveIcons)
        self.Level4_ViewWindow.removedItem.connect(self.AreaB_ViewWindow.RemoveIcons)
        self.Level4_ViewWindow.removedItem.connect(self.AreaA_ViewWindow.RemoveIcons)

        self.AreaA_ViewWindow.MainMenuWindow_requested.connect(self.MainMenuWindow.show)
        #self.AreaA_ViewWindow.MainMenuWindow_requested.connect(self.AreaA_ViewWindow.close)
        self.AreaA_ViewWindow.ListViewWindow_requested.connect(self.ListViewWindow.show)
        #self.AreaA_ViewWindow.ListViewWindow_requested.connect(self.AreaA_ViewWindow.close)
        self.AreaA_ViewWindow.MapViewWindow_requested.connect(self.MapViewWIndow.show)
        #self.AreaA_ViewWindow.MapViewWindow_requested.connect(self.AreaA_ViewWindow.close)
        self.AreaA_ViewWindow.Level4View_requested.connect(self.Level4_ViewWindow.show)
        self.AreaA_ViewWindow.Level4View_info.connect(self.Level4_ViewWindow.GetInfo)
        

class LoginWindow(qtw.QWidget):

    Login_submitted = qtc.pyqtSignal(bool)
    Permission_Lvl = qtc.pyqtSignal(str)

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.ui = LoginUi()           #create an instance of the form and assign it to self.ui
        self.ui.setupUi(self)         #call UI setup method and pass in self, this will build the GUI desigend onto this new widget

        self.ui.submit_button.clicked.connect(self.authenticate)        #connect button to function
        self.ui.password_edit.returnPressed.connect(self.authenticate)

    def authenticate(self):
        '''authenticate username and password information'''

        username = self.ui.username_edit.text()
        password = self.ui.password_edit.text()

        if username in users:
            #retrive the username and password information from dic
            password_hash, permission = users[username]
            if(password_hash == password):
                #display info message, open main program and hide login window
                qtw.QMessageBox.information(self, "Sucesss", "{} logged in".format(permission))
                self.Login_submitted.emit(True)
                self.Permission_Lvl.emit(permission)
                self.ui.username_edit.clear()
                self.ui.password_edit.clear()
                self.close()

            else:
                qtw.QMessageBox.critical(self, "Acess Denied", "Please try again")
                self.ui.password_edit.clear()               
        else:
            qtw.QMessageBox.critical(self, "Acess Denied", "Please try again")
            self.ui.password_edit.clear()

class Level4View(qtw.QWidget):

    removedItem = qtc.pyqtSignal(str)
    DisplayInfo_info = qtc.pyqtSignal(str, str, str)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Level4Ui()
        self.ui.setupUi(self)

        self.GetInfo(self)
        self.ui.PB_Resolved.clicked.connect(self.RemoveItem)
        self.DisplayInfo_info.connect(self.DisplayInfo)

    @qtc.pyqtSlot(str)
    def GetInfo(self, Tag):
        '''retrive the info from the button clicked signal in the level 3 view'''

        Red_Warning     = qtg.QPixmap("Graphics\RedWarning-removebg-preview.png")
        Amber_Warning   = qtg.QPixmap("Graphics\YellowWarningjpg-removebg-preview.png")
        Yellow_Warning  = qtg.QPixmap("Graphics\YellowWarning-removebg-preview.png")
        Grey_Warning    = qtg.QPixmap("Graphics\GreyWarning-modified.png")

        Tag = str(Tag)
        
        #now get the other data from the list based on the value of this button

        if(not PQ.isEmpty()):
            totalQueue = str(PQ)
            QueueItems = totalQueue.splitlines()

            for i in range(len(QueueItems)):
                if QueueItems[i][:8] == Tag:
                    Item = QueueItems[i].split("...")
                    self.ui.L_TagNo_data.setText(Item[0])
                    self.ui.L_AlarmStatus_data.setText(Item[2]) 
                    self.ui.L_Pri_data.setText(Item[3])
                    self.ui.L_Time_data.setText(Item[5])

                    #emit the signal to apply detailed info
                    self.DisplayInfo_info.emit(Tag, Item[2], Item[3])

                    #enable the buttons
                    self.ui.PB_Resolved.setEnabled(True)
                    self.ui.PB_Freeze.setEnabled(True)
                    self.ui.PB_Silence.setEnabled(True)

                    #apply graphic depending on priority
                    if Item[3] == "1":
                        self.ui.L_WarningSymbol.setPixmap(Yellow_Warning)
                    elif Item[3] == "2":
                        self.ui.L_WarningSymbol.setPixmap(Amber_Warning)
                    elif Item[3] == "3":
                        self.ui.L_WarningSymbol.setPixmap(Red_Warning)
                    break
                elif(QueueItems[i][:8] != Tag):
                    #if the alarm if not in the queue i.e. is not in alarm 
                    self.ui.L_WarningSymbol.setPixmap(Grey_Warning)
                    self.ui.L_TagNo_data.setText(Tag)
                    self.ui.L_AlarmStatus_data.setText("N/A")
                    self.ui.L_Pri_data.setText("N/A")
                    self.ui.L_Time_data.setText("N/A")
                    self.ui.TB_Actions.setText("Alarm not active, no actions avaliable.")
                    self.ui.TB_Causes.setText("N/A")
                    self.ui.TB_Conseq.setText("N/A")
                    self.ui.PB_Resolved.setEnabled(False)
                    self.ui.PB_Freeze.setEnabled(False)
                    self.ui.PB_Silence.setEnabled(False)
                    self.ui.TB_Actions.setText("N/A")
                    self.ui.TB_Conseq.setText("N/A")
                    self.ui.TB_Causes.setText("N/A")
        else:
            self.ui.L_WarningSymbol.setPixmap(Grey_Warning)
            self.ui.L_TagNo_data.setText(Tag)
            self.ui.L_AlarmStatus_data.setText("N/A")
            self.ui.L_Pri_data.setText("N/A")
            self.ui.L_Time_data.setText("N/A")
            self.ui.TB_Actions.setText("Alarm not active, no actions avaliable.")
            self.ui.TB_Causes.setText("N/A")
            self.ui.TB_Conseq.setText("N/A")
            self.ui.PB_Resolved.setEnabled(False)
            self.ui.PB_Freeze.setEnabled(False)
            self.ui.PB_Silence.setEnabled(False)
            self.ui.TB_Actions.setText("N/A")
            self.ui.TB_Conseq.setText("N/A")
            self.ui.TB_Causes.setText("N/A")

    def RemoveItem(self):
        '''remove an item from the queue'''

        Tag = self.ui.L_TagNo_data.text()
        #print(Tag)

        msg = qtw.QMessageBox.warning(self, 'Confirm Action', 'Are you want to remove {} from the queue'.format(Tag), qtw.QMessageBox.Yes | qtw.QMessageBox.No, qtw.QMessageBox.No)

        if msg == qtw.QMessageBox.Yes:
            #remove an item from the queue
            item = PQ.Dequeue(Tag)
            qtw.QMessageBox.information(self, "Removal Sucessfull","Item {}, removed from queue".format(Tag), qtw.QMessageBox.Ok)
            self.removedItem.emit(Tag)
            print("item removed: {}".format(item))
            self.close()
            #print(PQ)

    @qtc.pyqtSlot(str, str, str)
    def DisplayInfo(self, Tag, TripLvl, Pri):
        '''display the additional info related to actions etc'''
        
        #connect to db
        conn = sqlite3.connect('AlarmData.db')
        cursor = conn.cursor()

        #need to querey the database based on the tag number and the trip lvl then get the information 
        #and apply it to the labels!

        if Tag[:2] == "LD":
            cursor.execute("SELECT * FROM AlarmData WHERE TagNo=? AND TripLvl=?", (Tag, TripLvl))
            results = cursor.fetchone()     
        elif Tag[:2] == "ED":
            cursor.execute("SELECT * FROM AlarmDataFandG WHERE TagNo=? AND Priority=?", (Tag, Pri))
            results = cursor.fetchone()
            print("Results", results)
        conn.close()

        self.ui.TB_Actions.setText(results[3])
        self.ui.TB_Conseq.setText(results[4])
        self.ui.TB_Causes.setText(results[5])
          
class MainMenuWindow(qtw.QMainWindow):

    ListView_requested = qtc.pyqtSignal(bool)
    LoginRequested = qtc.pyqtSignal(bool)
    MapView_requested = qtc.pyqtSignal(bool)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ListView = ListViewWindow(self)

        '''define button operations'''
        self.ui.Logout_button.clicked.connect(self.Logout)
        self.ListView_requested = self.ui.List_button.clicked
        self.MapView_requested = self.ui.Map_button.clicked

    def Login(self, text):
        '''change the main window header depending on permission lvl'''
        text = ("Welcome " + text)
        self.ui.Heading.setText(text)

    def Logout(self):
        '''logout the current user'''
        response = qtw.QMessageBox.question(self, "Confirm Logout", "Are you sure you want to logout?", qtw.QMessageBox.Yes |
        qtw.QMessageBox.No, qtw.QMessageBox.No)
        if response == qtw.QMessageBox.Yes:
            self.LoginRequested.emit(True)
            self.close()   

class ListViewWindow(qtw.QMainWindow):

    MainMenuWindow_requested = qtc.pyqtSignal(bool)
    MapViewWindow_requested = qtc.pyqtSignal(bool)
    Level4View_requested = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = ListUi()
        self.ui.setupUi(self)
        
        self.MainMenuWindow_requested = self.ui.MainMenu_button.clicked
        self.MapViewWindow_requested = self.ui.Map_button.clicked
        #self.MainMenuWindow_requested = self.ui.back_button.clicked

        self.ui.Refresh_button.clicked.connect(self.AddTableItem)
        self.ui.Refresh_button.clicked.connect(self.AddListItem)
        self.ui.listWidget.itemClicked.connect(self.ItemClicked)
        self.AutoRefresh()

    def AutoRefresh(self):
        '''refresh the table and list every Xs'''

        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.AddListItem)
        self.timer.timeout.connect(self.AddTableItem)
        self.timer.timeout.connect(self.AddListColor)
        self.timer.start(1000)


    def ItemClicked(self, Item):
        '''get the item the user selected from the list'''
        Item = Item.text()
        Item = str(Item)
        Tag = Item[:8]
        self.Level4View_requested.emit(Tag)
     
    def AddListItem(self):
        '''add an item to the list'''

        #repaint the queue
        self.ui.listWidget.clear() 

        #split the queue object back up into individual items
        if (not PQ.isEmpty()):
            totalQueue = str(PQ)
            QueueItems = totalQueue.splitlines()
            #add to list on screen 
            for i in range(len(QueueItems)):  
                ListItem = qtw.QListWidgetItem(QueueItems[i])
                self.ui.listWidget.addItem(ListItem)
        else:
            ListItem = qtw.QListWidgetItem("No Alarms Currently Active")
            self.ui.listWidget.addItem(ListItem) 
            

    def AddListColor(self):
        '''add a color to the list items based on priority'''
        if (not PQ.isEmpty()):
            for i in range(len(self.ui.listWidget)):
                row = str(self.ui.listWidget.item(i).text())
                item = row.split("...")
                Pri = item[3]
                if Pri == "3":
                    self.ui.listWidget.item(i).setBackground(qtg.QColor('#FFDEDE'))
                elif Pri == "2":
                    self.ui.listWidget.item(i).setBackground(qtg.QColor('#FFEAD2'))
                elif Pri == "1":
                    self.ui.listWidget.item(i).setBackground(qtg.QColor('#FFFCDE'))

    def AddTableItem(self):
        '''update the table with latest figures'''

        #get the number of priority 1,2 & 3 items from the PriorityQueue
        P1items = PQ.Priority_count(1)
        P2items = PQ.Priority_count(2)
        P3items = PQ.Priority_count(3)
        Total = P1items + P2items + P3items

        #turn these into table widget items
        P1items = qtw.QTableWidgetItem(str(P1items))
        P2items = qtw.QTableWidgetItem(str(P2items))
        P3items = qtw.QTableWidgetItem(str(P3items))
        Total = qtw.QTableWidgetItem(str(Total))

        #add the items to the table
        self.ui.tableWidget.setItem(0,0, P3items)
        self.ui.tableWidget.setItem(0,1, P2items)
        self.ui.tableWidget.setItem(0,2, P1items)
        self.ui.tableWidget.setItem(0,3,Total)

class MapViewWindow(qtw.QMainWindow):

    MainMenuWindow_requested = qtc.pyqtSignal(bool)
    ListViewWindow_requested = qtc.pyqtSignal(bool)
    AreaBViewWindow_requested = qtc.pyqtSignal(bool)
    AreaAViewWindow_requested = qtc.pyqtSignal(bool)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = MapViewUi()
        self.ui.setupUi(self)

        self.MainMenuWindow_requested = self.ui.MainMenu_button.clicked
        self.ListViewWindow_requested = self.ui.ListView_button.clicked
        self.AreaBViewWindow_requested = self.ui.pushButton_AreaB.clicked
        self.AreaAViewWindow_requested = self.ui.pushButton_AreaA.clicked
        self.AutoRefresh()

    def AutoRefresh(self):
        '''refresh the icons and count'''

        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.DisplayIcons)
        self.timer.start(1000)
  
    def DisplayIcons(self):
        '''display icons and update figures for alarms'''

        areas = ["A", "B"]
        priorities = [3, 2, 1]

        for area in areas:
            for priority in priorities:
                count  = PQ.AreaPriority_Count(priority, area)
                enabled = count >0
                label = getattr(self.ui, f"label_{area}_P{priority}")
                label.setEnabled(enabled)
                label_count = getattr(self.ui, f"label_{area}1_P{priority}")
                label_count.setText(str(count))

class AreaBViewWindow(qtw.QMainWindow):

    #define signals 
    MainMenuWindow_requested = qtc.pyqtSignal(bool)
    ListViewWindow_requested = qtc.pyqtSignal(bool)
    MapViewWindow_requested = qtc.pyqtSignal(bool)
    AreaBPA1ViewWindow_reuested = qtc.pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = AreaBUi()
        self.ui.setupUi(self)

        self.MainMenuWindow_requested = self.ui.MainMenu_button.clicked
        self.ListViewWindow_requested = self.ui.ListView_button.clicked
        self.MapViewWindow_requested = self.ui.MapView_button.clicked
        self.AreaBPA1ViewWindow_reuested = self.ui.Button_ViewPA1.clicked
        self.AutoRefresh()

    def AutoRefresh(self):
        '''refresh screen items'''

        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.DisplayIcons)
        self.timer.start(1000)

    def DisplayIcons(self):
        '''display the icons in the correct place on the map'''

        Red_Warning     = qtg.QPixmap("Graphics\RedWarning-removebg-preview.png")
        Amber_Warning   = qtg.QPixmap("Graphics\YellowWarningjpg-removebg-preview.png")
        Yellow_Warning  = qtg.QPixmap("Graphics\YellowWarning-removebg-preview.png")

        if(not PQ.isEmpty()):

            totalQueue = str(PQ)
            QueueItems = totalQueue.splitlines()
            
            for i in range(len(QueueItems)):
                Item = QueueItems[-(i+1)].split("...")  #reverse the queue (so that highest pri items are painted last)
                Tag = Item[0]
                Pri = Item[3]
                if Tag[:2] == "LD":
                    label = getattr(self.ui, f"TAG_{Tag[4:8]}")
                    if Pri == "3": 
                        label.setPixmap(Red_Warning)
                    elif Pri == "2":
                        label.setPixmap(Amber_Warning)
                    elif Pri == "1":
                        label.setPixmap(Yellow_Warning)
                elif Tag[:2] == "ED":
                    #same thing here but for different area
                    continue


    @qtc.pyqtSlot(str)           
    def RemoveIcons(self, Tag):               
        '''if an item has been removed from the queue remove the symbol'''

        Grey_Warning    = qtg.QPixmap("Graphics\GreyWarning-modified.png")

        try:
            label = getattr(self.ui, f"TAG_{Tag[4:8]}")
            label.setPixmap(Grey_Warning)
        except:
            print("Error, AreaBPA1ViewWindow/RemoveIcons")

class AreaBPA1ViewWindow(qtw.QMainWindow):

    MainMenuWindow_requested = qtc.pyqtSignal(bool)
    ListView_requested = qtc.pyqtSignal(bool)
    MapView_requested = qtc.pyqtSignal(bool)
    Back_requested = qtc.pyqtSignal(bool)
    Level4View_requested = qtc.pyqtSignal(bool)
    Level4View_info = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = AreaBPA1Ui()
        self.ui.setupUi(self)

        self.MainMenuWindow_requested = self.ui.MainMenu_button.clicked
        self.ListView_requested = self.ui.ListView_button.clicked
        self.Back_requested = self.ui.back_button.clicked
        self.MapView_requested = self.ui.MapView_button.clicked

        self.ui.PB_LDPT2000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDTT2000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDPT1000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDTT1000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDLT1000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDPT3000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDTT3000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDTT2001.clicked.connect(self.DisplayLevel4)
        self.ui.PB_LDPT2001.clicked.connect(self.DisplayLevel4)
        self.AutoRefresh()

    def AutoRefresh(self):
        '''refresh screen items'''

        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.DisplayIcons)
        self.timer.start(1000)

    def DisplayLevel4(self):
        '''display the lvl 4 view for a specifc instrument'''

        #find out which button was clicked
        sender = self.sender()
        button = sender.objectName()

        Tag = str(button)
        Tag = Tag[3:]
        #print("here", Tag)
        

        #emit a signal to start up the window and a signal with the button info
        self.Level4View_requested.emit(True)
        self.Level4View_info.emit(str(Tag))

    def DisplayIcons(self):
        '''display the icons next to appropriate instruments'''

        Red_Warning     = qtg.QPixmap("Graphics\RedWarning-removebg-preview.png")
        Amber_Warning   = qtg.QPixmap("Graphics\YellowWarningjpg-removebg-preview.png")
        Yellow_Warning  = qtg.QPixmap("Graphics\YellowWarning-removebg-preview.png")
        

        if(not PQ.isEmpty()):
            totalQueue = str(PQ)
            QueueItems = totalQueue.splitlines()

            for i in range(len(QueueItems)):
                Item = QueueItems[-(i+1)].split("...")  #reverse the queue (so that highest pri items are painted last)
                Tag = Item[0]
                Pri = Item[3]
                if Tag[:2] == "LD":
                    try:    #check to see if label exists within current window
                        label = getattr(self.ui, f"label_{Tag}")
                        if Pri == "3": 
                            label.setPixmap(Red_Warning)
                        elif Pri == "2":
                            label.setPixmap(Amber_Warning)
                        elif Pri == "1":
                            label.setPixmap(Yellow_Warning)
                    except:
                        continue
                elif Tag[:2] == "ED":
                    #same thing here but for different area
                    continue

    @qtc.pyqtSlot(str)           
    def RemoveIcons(self, Tag):               
        '''if an item has been removed from the queue remove the symbol'''

        Grey_Warning = qtg.QPixmap("Graphics\GreyWarning-modified.png")

        try:
            label = getattr(self.ui, f"label_{Tag}")
            label.setPixmap(Grey_Warning)
        except:
            print("Error, AreaBPA1ViewWindow/RemoveIcons")

class AreaAViewWindow(qtw.QMainWindow):

    MainMenuWindow_requested = qtc.pyqtSignal(bool)
    ListViewWindow_requested = qtc.pyqtSignal(bool)
    MapViewWindow_requested = qtc.pyqtSignal(bool)
    Level4View_requested = qtc.pyqtSignal(bool)
    Level4View_info = qtc.pyqtSignal(str)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = AreaAUi()
        self.ui.setupUi(self)

        self.MainMenuWindow_requested = self.ui.MainMenu_button.clicked
        self.ListViewWindow_requested = self.ui.ListView_button.clicked
        self.MapViewWindow_requested = self.ui.MapView_button.clicked

        self.ui.PB_EDFD2000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDFD2001.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDFD2002.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDHV3000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDHV3001.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1000.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1001.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1002.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1003.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1004.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1005.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1006.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1007.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1008.clicked.connect(self.DisplayLevel4)
        self.ui.PB_EDSD1009.clicked.connect(self.DisplayLevel4)


        self.AutoRefresh()

    def AutoRefresh(self):
        '''refresh screen items'''
        self.timer = qtc.QTimer(self)
        self.timer.timeout.connect(self.DisplayIcons)
        self.timer.start(1000)

    def DisplayIcons(self):
        '''display the icons'''

        Red_Warning     = qtg.QIcon("Graphics\RedWarning-removebg-preview.png")
        Amber_Warning   = qtg.QIcon("Graphics\YellowWarningjpg-removebg-preview.png")
        Yellow_Warning  = qtg.QIcon("Graphics\YellowWarning-removebg-preview.png")

        if(not PQ.isEmpty()):
            totalQueue = str(PQ)
            QueueItems = totalQueue.splitlines()

            for i in range(len(QueueItems)):
                Item = QueueItems[-(i+1)].split("...")  #reverse the queue (so that highest pri items are painted last)
                Tag = Item[0]
                Pri = Item[3]
                if Tag[:2] == "ED":
                    try:    #check to see if label exists within current window
                        Button = getattr(self.ui, f"PB_{Tag}")
                        if Pri == "3": 
                            Button.setIcon(Red_Warning)
                        elif Pri == "2":
                            Button.setIcon(Amber_Warning)
                        elif Pri == "1":
                            Button.setIcon(Yellow_Warning)
                    except:
                        continue

    def DisplayLevel4(self):
        '''display the lvl 4 view for a specifc alarm'''

        #find out which button was clicked
        sender = self.sender()
        button = sender.objectName()

        Tag = str(button)
        Tag = Tag[3:]
        

        #emit a signal to start up the window and a signal with the button info
        self.Level4View_requested.emit(True)
        self.Level4View_info.emit(str(Tag))

    @qtc.pyqtSlot(str)           
    def RemoveIcons(self, Tag):               
        '''if an item has been removed from the queue remove the symbol'''

        Grey_Warning    = qtg.QIcon("Graphics\GreyWarning-modified.png")

        try:
            button = getattr(self.ui, f"PB_{Tag}")
            button.setIcon(Grey_Warning)
        except:
            print("Error, AreaAViewWindow/RemoveIcons")



if __name__ == '__main__':

    #initilise the Queues
    PQ = PriQueue()
    P4Q = P4Queue()
    EQ = EventQueue()

    app = MainApp(sys.argv)
    
    #start threads
    #t2 = Thread(target=Thread2)     #this runs the GUI
    t1 = Thread(target=Thread1)     #this runs the backend
    #t2.setDaemon(True)
    t1.setDaemon(True)
    #t2.start()

    #time.sleep(5)    #for test purposes (allow user to login)
    t1.start()

    

    while(True):
        sys.exit(app.exec())
        pass

