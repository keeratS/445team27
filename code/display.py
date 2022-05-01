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
import numpy as np

fontcolor='#ffffff'

# lists to store data from the text file
time=[]
sen1=[]
sen2=[]
sen3=[]

avg_time=[]
avg_sen1=[]
avg_sen2=[]
avg_sen3=[]

# populate lists with data from csv file
# make sure data is being read as numbers and not strings

# use below line for use with device
with open("D:\SEN3.TXT") as File:

# use below line for use during debugging
# with open("SEN3v2.TXT") as File:
  beedata = csv.reader(File, delimiter = ',')

  for row in beedata:
    time.append(int(row[0]))
    sen1.append(int(row[1]))
    sen2.append(int(row[2]))
    sen3.append(int(row[3]))

# make picture of continuous data
'''
fig = px.line(title='Raw measured activity within tube')
fig.add_scatter(x=time, y=sen1, name='shallow')
fig.add_scatter(x=time, y=sen2, name='mid')
fig.add_scatter(x=time, y=sen3, name='deep')

fig.update_layout(
    xaxis_title="time",
    yaxis_title="voltage",
    )
'''
# do analysis to identify interesting bee behavior patterns

# average out the data
# uses slightly overlapping averaging windows for a smoother graph
for i in range(1,(len(time)-3),1):

    avg_time.append(round((time[i]+time[i+1]+time[i+2]+time[i+3])/4))
    avg_sen1.append(round((sen1[i]+sen1[i+1]+sen1[i+2]+sen1[i+3])/4))
    avg_sen2.append(round((sen2[i]+sen2[i+1]+sen2[i+2]+sen2[i+3])/4))
    avg_sen3.append(round((sen3[i]+sen3[i+1]+sen3[i+2]+sen3[i+3])/4))

fig1 = px.line(title='Processed activity within tube')

fig1.add_scatter(x=avg_time, y=avg_sen1, name='shallow', line=dict(color='DarkSeaGreen'))
fig1.add_scatter(x=avg_time, y=avg_sen2, name='mid', line=dict(color='LightSkyBlue'))
fig1.add_scatter(x=avg_time, y=avg_sen3, name='deep', line=dict(color='Violet'))

fig1.update_layout(
    xaxis_title="time",
    yaxis_title="voltage",
    plot_bgcolor='#19183a',
    paper_bgcolor='#19183a',
    title_font_color=fontcolor,
    legend_font_color=fontcolor,
    legend_grouptitlefont_color=fontcolor,
    legend_title_font_color=fontcolor,

    )

fig1.update_xaxes(color=fontcolor)
fig1.update_yaxes(color=fontcolor)

# find interesting things in the data

# find "normal" to be able to make conclusions about abnormal
med1=np.median(avg_sen1[75:])
med2=np.median(avg_sen2[75:])
med3=np.median(avg_sen3[75:])

# put the reference lines on the graph
#fig1.add_hline(ref1)
#fig1.add_hline(med2)
#fig1.add_hline(med3)

# mark potential bee crossing points, stage 1: cross the median
in1=[]
out1=[]
in2=[]
out2=[]
in3=[]
out3=[]

sensitivity = 2 #how much of a deviation from normal is significant (in same units as y axis)

for i in range(1,(len(avg_time)-10)):

    #identify potential bee crossings on shallow data
    #ins
    if ((avg_sen1[i]<med1) and (avg_sen1[i+1]>med1)):
        if ((sum(avg_sen1[i-5:i])/5)< med1-sensitivity and ( sum(avg_sen1[i:i+5])/5)>med1+sensitivity):
            in1.append((avg_time[i], avg_sen1[i]))
    #outs
    if ((avg_sen1[i]>med1) and (avg_sen1[i+1]<med1)):
        if ((sum(avg_sen1[i-5:i])/5)> med1+sensitivity and ( sum(avg_sen1[i:i+5])/5)<med1-sensitivity):
            out1.append((avg_time[i], avg_sen1[i]))

    #identify potential bee crossings on mid data
    #ins
    if ((avg_sen2[i]<med2) and (avg_sen2[i+1]>med2)):
        if ((sum(avg_sen2[i-5:i])/5)< med2-sensitivity and ( sum(avg_sen2[i:i+5])/5)>med2+sensitivity):
            in2.append((avg_time[i], avg_sen2[i]))
    #outs
    if ((avg_sen2[i]>med2) and (avg_sen2[i+1]<med2)):
        if ((sum(avg_sen2[i-5:i])/5)> med2+sensitivity and ( sum(avg_sen2[i:i+5])/5)<med2-sensitivity):
                out2.append((avg_time[i], avg_sen2[i]))

    #identify potential bee crossings on deep data
    #ins
    if ((avg_sen3[i]<med3) and (avg_sen3[i+1]>med3)):
        if ((sum(avg_sen3[i-5:i])/5)< med3-sensitivity and ( sum(avg_sen3[i:i+5])/5)>med3+sensitivity):
            in3.append((avg_time[i], avg_sen3[i]))
    #outs
    if ((avg_sen3[i]>med3) and (avg_sen3[i+1]<med3)):
        if ((sum(avg_sen3[i-5:i])/5)> med3+sensitivity and ( sum(avg_sen3[i:i+5])/5)<med3-sensitivity):
                out3.append((avg_time[i], avg_sen3[i]))


#if any entry or exits are found, label them on the graph
if (in1):
    fig1.add_scatter(x=list(zip(*in1))[0], y=list(zip(*in1))[1],
    mode='markers', name='shallow in', marker=dict(size=10, color='GreenYellow'))
if (out1):
    fig1.add_scatter(x=list(zip(*out1))[0], y=list(zip(*out1))[1],
    mode='markers', name='shallow out', marker=dict(size=10, color='LimeGreen'))
if (in2):
    fig1.add_scatter(x=list(zip(*in2))[0], y=list(zip(*in2))[1],
    mode='markers', name='mid in', marker=dict(size=10, color='Aqua'))
if (out2):
    fig1.add_scatter(x=list(zip(*out2))[0], y=list(zip(*out2))[1],
    mode='markers', name='mid out', marker=dict(size=10, color='DodgerBlue'))
if (in3):
    fig1.add_scatter(x=list(zip(*in3))[0], y=list(zip(*in3))[1],
    mode='markers', name='deep in', marker=dict(size=10, color='Fuchsia'))
if (out3):
    fig1.add_scatter(x=list(zip(*out3))[0], y=list(zip(*out3))[1],
    mode='markers', name='deep out', marker=dict(size=10, color='DarkViolet'))

# add pictures of reference value for visual confirmation
fig1.show()



# uncomment the lower code when using it on the device
# make a correctly dated copy of data

now = str(datetime.datetime.now())[5:19]
now = now.replace(":","_")

src="D:\SEN3.TXT"
dst="D:data"+str(now)+".txt"
shutil.copyfile(src,dst)

#clear the original file to make space for next reading
with open("D:\SEN3.TXT", 'w'):
    pass
