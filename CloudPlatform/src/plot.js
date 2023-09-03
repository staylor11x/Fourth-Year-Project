const getPeriod = () => {

    var date1 = document.getElementById('startDate').value
    var date2 = document.getElementById('endDate').value

    let dateRange = {
        start: date1,
        end: date2
    }
    console.log(dateRange)
    fetch('http://localhost:8000/api/data', {
    method:'POST',
    body: JSON.stringify(dateRange),
    headers: {
        'Content-Type':'application/json'
    }
    }).then(response => {
        return response.json()
    }).then(data => {
        //plot the data
        console.log(data)
        graphData(data)
    })
}

const alarmsVsTime = () => {
    //get the total number of alarms over a defined time period

    fetch("http://localhost:8000/SingleAlarmData")
    .then(response => response.json())
    .then(data => {

        //get the date value from the UI & format appropriately
        var date1 = document.getElementById('startDate')
        var date2 = document.getElementById('endDate')
        
        if(date1.value){
            date1 = date1.value.replace(/-/g,"")        //remove all '-' chars
            date1 = parseInt(date1)                     //convert to int
        }
        if(date2.value){
            date2 = date2.value.replace(/-/g,"")
            date2 = parseInt(date2)   
        }

        //define variables for graph axis
        let xaxis = []
        let yaxis = []
        
        var alarmCount = {}
        var totalCount = 0      //for test purposes (counts the total # of alarms)


        for(i=0;i<data.length;i++){
            var dateToCompare = (data[i].X).replace(/-/g,"")    //remove all '-' chars
            dateToCompare = dateToCompare.slice(0,8)            //remove unused data
            console.log(dateToCompare)
            dateToCompare = parseInt(dateToCompare)
            if((dateToCompare >= date1) && (dateToCompare <= date2)){
                if(alarmCount[data[i].Tag]){
                    alarmCount[data[i].Tag] += data[i].Y
                    totalCount += data[i].Y
                }else{
                    alarmCount[data[i].Tag] = data[i].Y
                    totalCount += data[i].Y
                }
            }
        }
        console.log(totalCount)

        //sort the dictionary largest to smallest 
        alarmCount = Object.entries(alarmCount).sort((b,a) => a[1]-b[1])
        alarmCount = Object.fromEntries(alarmCount)

        //get the keys (tags) and values (no. trips) from the dictionary that returns from 
        //count, this then becomes the x and y cooridate arrays frot the graph
        const keys = Object.keys(alarmCount)
	    const values = Object.values(alarmCount)

        for(i=0; i<alarmCount.length; i++){
            xaxis.push(alarmCount[i].X)
            yaxis.push(alarmCount[i].Y)
        }

            var Graphdata = [
                {
                    x:keys,
                    y:values,
                    type:"bar"
                }
            ]
            console.log(Graphdata)

            var layout = {
                xaxis:{title:"Tag Numbers"},
                yaxis:{title:"Number of trips"},
                title: "Tag numbers vs No. of trips"
            };

            Plotly.newPlot("TagData", Graphdata, layout)
        })    
}


const getSingleAlarmData = () => {

    fetch("http://localhost:8000/SingleAlarmData")
    .then(response => response.json())
    .then(data => {
        //get the tag values from the dropdowns
    var tag1 = document.getElementById('tag1')
    var tag2 = document.getElementById('tag2')

    let xaxis1 = []
    let xaxis2 = []
    let yaxis1 = []
    let yaxis2 = []

    //assign the data to the relevant axis
    for(n=0; n<data.length; n++){
        if (data[n].Tag === tag1.value){        
            xaxis1.push(data[n].X)
            console.log(data[n].X)
            yaxis1.push(data[n].Y)
            console.log(data[n].Y)
        }
        else if(data[n].Tag === tag2.value){
            xaxis2.push(data[n].X)
            yaxis2.push(data[n].Y)
        }
        else continue
    }
    var trace1 = {
        type:"line",
        mode:"lines",
        name:tag1.value,
        x:xaxis1,
        y:yaxis1,
        line:{color: '#17BECF'}
    }
    var trace2 = {
        type:"line",
        mode:"lines",
        name:tag2.value,
        x:xaxis2,
        y:yaxis2,
        line:{color: '#eb4034'}
    }
    var data = [trace1, trace2]
    var layout = {
        title: 'Alarm comparison over time',
        xaxis: {
            autorange: true, 
            range: ['2023-01-01, 2023-04-06'],
            rangeselector: {buttons: [
                {
                    count:1, 
                    label:'1d',
                    step:'day',
                    stepmode:'backward'
                },
                {
                    count:7,
                    label:'1w',
                    step:'day',
                    stepmode:'backward'
                },
                {
                    count:1,
                    label:'1m',
                    step:'month',
                    stepmode:'backward'
                },
                {
                    count:6,
                    label:'6m',
                    step:'month',
                    stepmode:'backward'
                },
                {step:'all'}
            ]},
        rangeslider: {range: ['2023-01-01, 2023-03-01']},
        type:'date'
        },
        yaxis: {
            autorange:true,
            type:'linear'
        }
    }
    Plotly.newPlot('SingleAlarmData', data, layout)
    })
}

const tagsVsTrips = () => {
    //get the data related to the number of trips for each tag number
    //plot this on a bar graph

    fetch('http://localhost:8000/GeneralData')
    .then(response => response.json())
    .then(data => { //use the data and plot the graph

        let xaxis = []
        let yaxis = []

        console.log(data.length)

        for(i=0; i<data.length; i++){
            xaxis.push(data[i].X)
            yaxis.push(data[i].Y)
        }

            var Graphdata = [
                {
                    x:xaxis,
                    y:yaxis,
                    type:"bar"
                }
            ]
            console.log(Graphdata)

            var layout = {
                xaxis:{title:"Tag Numbers"},
                yaxis:{title:"Number of trips"},
                title: "Tag numbers vs No. of trips"
            };

            Plotly.newPlot("TagData", Graphdata, layout)
        })
}

const totalAlarmsVsArea = () => {
    //get the data related to the total alarms per area
    //plot this on a pie chart

    fetch('http://localhost:8000/AreaData')
    .then(response => response.json())
    .then(data => {

        let values = []
        let labels = []

        for(i=0; i<data.length;i++){
            values.push(data[i].Y)
            labels.push(data[i].X)
        }

        var data = [{
            values: values,
            labels: labels,
            type: 'pie'
        }]

        var layout = {
            height:750,
            width:750,
            title: "Alarms by Area"
        }
        Plotly.newPlot("AreaData", data, layout)

    })
}

const totalAlarmsVsDates = () => {
    //get the data related to the total alarms for each date
    //plot this on a bar graph

    fetch('http://localhost:8000/DayData')
    .then(response => response.json())
    .then(data => {

        let xaxis = []
        let yaxis = []

        console.log(data.length)

        for(i=0; i<data.length; i++){
            xaxis.push(data[i].X)
            yaxis.push(data[i].Y)
        }

            var Graphdata = [
                {
                    x:xaxis,
                    y:yaxis,
                    type:"bar"
                }
            ]
            console.log(Graphdata)

            var layout = {
                xaxis: {
                    //autorange: true, 
                    range: ['2023-01-01, 2023-04-06'],
                    rangeselector: {buttons: [
                        {
                            count:1, 
                            label:'1d',
                            step:'day',
                            stepmode:'backward'
                        },
                        {
                            count:7,
                            label:'1w',
                            step:'day',
                            stepmode:'backward'
                        },
                        {
                            count:1,
                            label:'1m',
                            step:'month',
                            stepmode:'backward'
                        },
                        {
                            count:6,
                            label:'6m',
                            step:'month',
                            stepmode:'backward'
                        },
                        {step:'all'}
                    ]},
                    rangeslider: {range: ['2023-01-01, 2023-03-01']},
                    type:'date'},
                yaxis:{title:"Number of trips"},
                title: "Dates vs No. of trips"
            };

            Plotly.newPlot("DayData", Graphdata, layout)
    })
}    

const topTenAlarms = () => {
    //Get the data related to the top 10 bad acting alarms
    //plot this on a rose diagram

    fetch('http://localhost:8000/TopTenData')
    .then(response => response.json())
    .then(data => {

        let xaxis = []
        let yaxis = []

        console.log(data.length)

        for(i=0; i<data.length; i++){
            xaxis.push(data[i].X)
            yaxis.push(data[i].Y)
        }

        var data = [{
            r:[yaxis[0]],
            theta:[xaxis[0]],
            name: xaxis[0],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"

        },
        {
            r:[yaxis[1]],
            theta:[xaxis[1]],
            name: xaxis[1],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[2]],
            theta:[xaxis[2]],
            name: xaxis[2],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[3]],
            theta:[xaxis[3]],
            name: xaxis[3],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[4]],
            theta:[xaxis[4]],
            name: xaxis[4],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[5]],
            theta:[xaxis[5]],
            name: xaxis[5],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[6]],
            theta:[xaxis[6]],
            name: xaxis[6],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[7]],
            theta:[xaxis[7]],
            name: xaxis[7],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[8]],
            theta:[xaxis[8]],
            name: xaxis[8],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        {
            r:[yaxis[9]],
            theta:[xaxis[9]],
            name: xaxis[9],
            //marker: {color: rgb(106,81,163)},
            type: "barpolar"
        },
        ]

        var layout = {
            title: "Top 10 alarms",
            height: 750,
            width:750,
            align:"Center",
            polar: {
                barmode: "overlay",
                bargap: 0,
                //radialaxis: {ticksuffix: "", angle: 45, dtick:20},
                angularaxis: {direction: "clockwise"}
            }
        }
    Plotly.newPlot("TopTenData", data, layout)
    })
}

const totalAlarmsVsTime = () => {
    //Get the data related to total alarms for each 1 min period
    //plot total alarms vs time

    fetch("http://localhost:8000/TimeData")
    .then(response => response.json())
    .then(data => {

        let xaxis = []
        let yaxis = []

        for(i=0; i<data.length; i++){
            xaxis.push(data[i].X)
            yaxis.push(data[i].Y)
        }

        var trace1 = {
            type:"scatter",
            mode:"lines",
            name:"Alarms",
            x:xaxis,
            y:yaxis,
            line:{color: '#17BECF'}
        }

        var data = [trace1]

        var layout = {
            title: 'Alarms over time',
            xaxis: {
                autorange: true, 
                range: ['2023-01-01, 2023-04-06'],
                rangeselector: {buttons: [
                    {
                        count:1, 
                        label:'1d',
                        step:'day',
                        stepmode:'backward'
                    },
                    {
                        count:7,
                        label:'1w',
                        step:'day',
                        stepmode:'backward'
                    },
                    {
                        count:1,
                        label:'1m',
                        step:'month',
                        stepmode:'backward'
                    },
                    {
                        count:6,
                        label:'6m',
                        step:'month',
                        stepmode:'backward'
                    },
                    {step:'all'}
                ]},
                //tickformat: '%d-%m-%Y %H-%M-%S',
            rangeslider: {range: ['2023-01-01, 2023-03-01']},
            type:'date'
            },
            yaxis: {
                autorange:true,
                type:'linear'
            }
        }
        Plotly.newPlot('TimeData', data, layout)
    })
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


//Initilise the plots
//tagsVsTrips()
totalAlarmsVsTime()
topTenAlarms()
totalAlarmsVsArea()
getSingleAlarmData()
alarmsVsTime()

//listen out for user input in the dropdowns
tag1.addEventListener('change', getSingleAlarmData)
tag2.addEventListener('change', getSingleAlarmData)

startDate.addEventListener('input', alarmsVsTime)
endDate.addEventListener('input', alarmsVsTime)
