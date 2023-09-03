const fs = require("fs")
const path = require('path')
const PORT = 8000
const axios = require('axios')
const express = require('express')
const bodyParser  = require('body-parser')
const app = express()
const cors = require('cors')
const { format } = require("path")
app.use(cors())
app.use(express.urlencoded({extended: false}))

//start server on local host port 8000
app.listen(PORT, () => console.log('server running on PORT', PORT))

const getData = () => {
	//function to read in the data from .csv files (NOT Async)
	//function will read in entire directory 'data'
	//data will be read into an array

	let array = []
	fs.readdirSync('data').forEach(file =>{
		csv = fs.readFileSync(`data/${file}`)
		var tempArray = csv.toString().split("\r");
		array.push(...tempArray)
	})
	return array
}

const createObjects = (array, alarms) => {
	//create objects from the array generated from the csv file(s)

	for(i=1; i< array.length - 1; i++){			//this removes the first row of header data
		let alarmVals = []
		alarmVals = array[i].split(",")

		alarm = {

			"tagNo" : alarmVals[0].slice(1,10),
			"desc"	: alarmVals[1],
			"tripLvl" : alarmVals[2],
			"state"	:	alarmVals[3],
			"date"	: alarmVals[4],
			"time"	: alarmVals[5]
		}

		//Check that the tag no. is of suitable length
		//if not row is likley header data although could be corrupted
		//in each case remove it from the program
		if(alarm.tagNo.length !==8)
			continue
		else
			alarms.push(alarm)
	}
	return alarms;
}

const formatData = (count, Tag) => {
	//format the data for sending i.e. X&Y points & any other additional data
	//tag number can be used here as an identifier (i.e. if you are plotting data with time 
	//on the x-axis). If it is not required, then do not pass it into the function

	let dataPoints = []
	
	//split the data from the dic into two lists (x & y)
	const keys = Object.keys(count)
	const values = Object.values(count)
	console.log("Number of unique dataPoints", keys.length)

	//create an object and add to array of objects
	for(i=0; i< keys.length; i++){
		data = {
			Tag : Tag,
			X : keys[i],
			Y : values[i]
		}
		dataPoints.push(data)
	}

	//sort the objects, if the X coordinate is a tag number sort by Y value
	//if the X value is a date then sort by this date
	//this decision is made based on the length of the parameter

	if ((dataPoints[0].X).length > 9 )
		dataPoints.sort((a, b) => {
			return (a.X < b.X) ? -1 : ((a.X > b.X) ? 1 : 0)
		}); 
	else{
		dataPoints.sort((a, b) => b.Y - a.Y);
	}	
	//console.log(dataPoints)

	return dataPoints
}

//const sendAllData = (alarms) => {
//	//send all alarm objects to API
//	app.get('/AllData', function(req,res){
//		res.json(alarms)
//	})
//}

const getUnique = (alarms) => {
	//get unique tag numbers from list
	let tempList = [];

	//sort alarms based on tag no
	sortedAlarms = alarms.sort((a,b) => {
		fa = a.tagNo.toLowerCase(),
		fb = b.tagNo.toLowerCase();

		if (fa <fb){
			return -1;
		}
		if(fa>fb){
			return 1;
		}
		return 0;
	});
	
	for(i=0;i<alarms.length;i++){
		tempList.push(alarms[i].tagNo)
	}
	const uniqueList = [...new Set(tempList)]		//using a set as cannot contain duplicates
	return uniqueList
}

const Count = (tempList) => {
	//filter the alarm list based on a specfic paramater
	//this function will return the count of how many times each 
	//element appears in the temp list

	var alarmCount = {};
	for(var element of tempList){
		if(alarmCount[element]){			//if the element is already a key in alarmCount
			alarmCount[element] +=1;		//increment that keys count by 1
		}else{											
			alarmCount[element] =1;			//otherwise create a key for that element and add one to its count
		}
	}
	return alarmCount;
}

const countAlarms = (alarms) => {
	//function to count the occurences of each alarm in the csv based on tag no.
	let tempList = [];
	for(i=0;i<alarms.length;i++){
		tempList.push(alarms[i].tagNo)
	}
	
	alarmCount = Count(tempList)
	return alarmCount;
}

const areaCount = (alarms) => {
	//count the number of alarms in specific areas
	let tempList = []

	//get the unique areas
	for(i=0; i<alarms.length;i++){
		tempList.push(alarms[i].tagNo.slice(0,2))	//get the area from the tag number
	}
	
	alarmCount = Count(tempList)
	return alarmCount;
}

const dayCount = (alarms) => {
	//count the number of alarms for each day
	let tempList = []

	//get the unique days
	for(i=0;i<alarms.length;i++){
		// convert the date and time to ISO format
		const [day, month, year] = alarms[i].date.split("-");
		const dateTime = new Date(year, month-1, day)	//the month is 0-indexed
		let dateTimeISO = dateTime.toISOString()
		tempList.push(dateTimeISO);
	  }
	alarmCount = Count(tempList)
	return alarmCount;
}

const timeCount = (alarms) => {
	//count the number of alarms at a specific time (nearest minuite)
	let tempList = []

	//get the unique times
	for(i=0;i<alarms.length;i++){
		// convert the date and time to ISO format
		const [day, month, year] = alarms[i].date.split("-");
		const [hour, minute, second] = alarms[i].time.split(":");
		const dateTime = new Date(year, month-1, day, hour, minute)	//the month is 0-indexed
		let dateTimeISO = dateTime.toISOString()
		tempList.push(dateTimeISO);
	  }
	alarmCount = Count(tempList)
	return alarmCount;

}

const topTen = (alarms) => {
	//top ten bad acting alarms 

	let topTen = []
	for(i=0; i<10; i++){
		topTen.push(alarms[i])
	}
	
	return topTen
}

const singleAlarm = (alarms, Tag) => {
	//return the trip data for a single alarm
	console.log("Tag",Tag)
	tempList = []

	for(i=0; i<alarms.length; i++){
		if(Tag === alarms[i].tagNo){
			const [day, month, year] = alarms[i].date.split("-");
			const dateTime = new Date(year, month-1, day)	//the month is 0-indexed
			dateTimeISO = dateTime.toISOString()
			tempList.push(dateTimeISO);
		}
	}
	alarmCount = Count(tempList)

	return alarmCount
}

const autoSingleAlarm = (uniqueTags) => {
	//automatically pass through each unique alarm tag to find
	//how many times that alarm has tripped on a specfic day
	var TotalData = []
	var n = 0
	while( n< uniqueTags.length){
		let alarm1 = singleAlarm(alarms,uniqueTags[n])
		alarm1 = formatData(alarm1, uniqueTags[n])
		TotalData = TotalData.concat(alarm1)
		n++
	}
	return TotalData	
}

//////////////////////////////////////////////////////////////////////////////////////////////////////
///read the data in from CSV
var RawData = getData()

//convert the items in the array to objects
let alarms = []
alarms = createObjects(RawData, alarms)
console.log("No. of objects", alarms.length)

//get the unique tags
let uniqueTags = []
uniqueTags = getUnique(alarms)

//perform processing to obtain data
let count = countAlarms(alarms)
let areaData = areaCount(alarms)
let dayData  = dayCount(alarms)
let timeData = timeCount(alarms)

//sendAllData(alarms)
areaData = formatData(areaData)
generalData = formatData(count)
let topTenData = topTen(generalData)
dayData = formatData(dayData)
timeData = formatData(timeData)

var TotalData = autoSingleAlarm(uniqueTags)

//send data
app.get('/GeneralData', function(req,res){
	res.json(generalData)
	})

app.get('/AreaData', function(req,res){
	res.json(areaData)
})

app.get('/DayData', function(req,res){
	res.json(dayData)
})

app.get('/TopTenData', function(req,res){
	res.json(topTenData)
})

app.get('/TimeData', function(req,res){
	res.json(timeData)
})

app.get('/SingleAlarmData', function(req,res){
	res.json(TotalData)
})

app.get('/AllData', function(req,res){
	res.json(alarms)
})


