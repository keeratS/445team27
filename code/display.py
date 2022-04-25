# this script displays data from the bee tube in a time vs voltage
# graph. To use this you will need to install plotly and pandas
# pip install plotly
# pip install pandas
# the script does not currently deal with timestamp overflow, because
# millis starts at zero when the arduino is powered and does not roll over
# until apporx 50 days have passed, which is like a whole bee season
# the graph will display on your default browser
# the script also clears the file in which the arduino writes data, and makes a
# copy of the data it cleared in a file named with the data and time

import csv
import plotly.express as px
import shutil
import datetime

# lists to store data from the text file
time=[]
sen1=[]
sen2=[]
sen3=[]

# populate lists with data from csv file
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

#make a correctly dated copy of data
now = str(datetime.datetime.now())[5:19]
now = now.replace(":","_")

src="D:\SEN3.TXT"
dst="D:data"+str(now)+".txt"
shutil.copyfile(src,dst)

#clear the original file to make space for next reading
with open("D:\SEN3.TXT", 'w'):
    pass
