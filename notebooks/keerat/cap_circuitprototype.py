import matplotlib.pyplot as plt

x=[4,5,6]

y1=[340-258, 434-280, 520-330]

y2=[661-385, 773-496, 894-558]

plt.plot(x,y1, label="Using Capacitance Change of 1.25 pF", marker= 'o')
plt.plot(x,y2, label="Using Capacitance Change of 2.5 pF", marker= 'o')
plt.ylim(0,400)

plt.xlabel("Input Voltage (V)")
plt.ylabel("Change in Output Voltage (mV)")
plt.legend()
plt.title("Change in AC Bridge Output Voltage vs. Input Voltage")

plt.show()
