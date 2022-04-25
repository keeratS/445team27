# this script displays data from the bee tube in a time vs voltage
# graph. To use this you will need to install plotly and pandas
# pip install plotly
# pip install pandas
# the script does not currently deal with timestamp overflow
# the graph will display on your default browser

import csv
import plotly.express as px

#lists to store data from the text file
time=[]
sen1=[]
sen2=[]
sen3=[]

#populate lists with data from csv file
with open("D:\SEN3.TXT") as File:
  beedata = csv.reader(File, delimiter = ',')

  for row in beedata:
    time.append(row[0])
    sen1.append(row[1])
    sen2.append(row[2])
    sen3.append(row[3])

#make picture
fig = px.line(title='Measured activity within tube')
fig.add_scatter(x=time, y=sen1, name='shallow')
fig.add_scatter(x=time, y=sen2, name='mid')
fig.add_scatter(x=time, y=sen3, name='deep')

fig.update_layout(
    xaxis_title="time",
    yaxis_title="voltage",
    )

fig.show()
