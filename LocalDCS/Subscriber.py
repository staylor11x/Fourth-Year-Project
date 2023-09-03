'''original subsriber file NO LONGER IN USE

    replaced on 19/01/2022 and added to MainAPP.py

'''



import paho.mqtt.client as mqtt
from EventObj import Event
from datetime import datetime
import subprocess
import pickle
from PriorityQueue import PriQueue
from P4Queue import P4Queue
from EventQueue import EventQueue

from multiprocessing import Process, Pipe, Queue
import json
from threading import Thread

def sendQueue(E):
    '''send data to the relevant queue/list'''
    #this could potentially be moved to the object class
    
    if(E.Pri == 4):
        #add item to p4 queue
        P4Q.Enqueue(E)
        print(P4Q)
    elif(E.Pri == 0):
        #add item to the event list
        EQ.Enqueue(E)
        print(EQ)
    else:
        #if the alarm is an alarm, add it to the priority queue
        PQ.Enqueue(E)
        print(PQ)

def sender(q):
    '''sends data to the GUI'''
    data = PQ.Size()
    json_data = json.dumps(data)
    q.put(json_data)

def f(conn, PQ):
    '''sends data to the GUI'''
    conn.send(PQ)
    conn.close()

def on_message(client, userdata, message):
    '''callback function to print out the message/store message as an object'''

    #apply date and time to event
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y %H:%M:%S")
    
    #decode message and make event object
    RecievedMsg = str(message.payload.decode("utf-8"))
    splitline = RecievedMsg.split(',')
    E = Event(splitline[0], splitline[1], splitline[2], int(splitline[3]), int(splitline[4]), timestamp)

    #send data to relevant queue 
    sendQueue(E)

    #send the data to the processing module
    data = pickle.dumps(E)
    command = "Processing.py"
    pipe = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
    pipe.stdin.write(data)
    pipe.stdin.close()
    #pipe.wait()

    ##delete item from the queue (test purposes)
    #if (PQ.Size() > 3):
    #    PQ.Dequeue(3)

def Thread1():
    '''open the publisher file(s)'''
    subprocess.Popen(["python","FG_Publisher.py"])
    #subprocess.Popen(["python","Random_Publisher.py"])
    #subprocess.Popen(["python","Process_Publisher.py"])

    #create link to broker
    mqttBroker = "localhost"
    BrokerPort = 1883
    client = mqtt.Client("Smartphone")
    client.connect(mqttBroker,BrokerPort)

    client.on_message = on_message

    client.subscribe("TEMPERATURE")

    '''start loop for listening'''
    client.loop_forever()
    #no commands can be executed after this statement!!

if __name__ == '__main__':

    #initilise the Queues
    PQ = PriQueue()
    P4Q = P4Queue()
    EQ = EventQueue()

    t1 = Thread(target=Thread1)
    t1.setDaemon(True)
    t1.start()
    while(True):
        pass