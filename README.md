# Fourth-Year-Project
My fourth year project (all files)

This project contains two separate sections, one based in JS with express and the other based as a python GUI app built using QT.

## Local DCS (Python)

This is a desktop application created using PyQT5.

The app is designed to resemble an operators workstation displaying alarms on screen via various different map views and also in list form.

The data is fed in to the program via different excel sheets which act as different test cases. These can be selected based on the script used to read them.

The data is read by a python file then sent over an MQTT server where another python script 'subscribes' and then then feeds this into the main queue system.

As a historical record of alarms once they are read in by the application they are then sent to a history file system. This creates a new file for each day. In hindsight this is actually quite useful for running efficient queries.

Admittedly, there are probably a million better ways this could have been designed!

## Cloud Platform (JavaScript)

This uses node in the backend and then express in the frontend. The plots are generated using plotly.js.

The app gets its data from the excel sheets generated from the local DCS (discussed above), processes the data within these and then sends the data to the frontend.

In the frontend the data is then queried by the user and they can view data for different alarms within the facility over different time periods.
