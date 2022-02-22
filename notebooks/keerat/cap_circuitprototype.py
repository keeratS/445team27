import matplotlib.pyplot as plt

x=[4,5,6]

y1=[249-160, 321-204, 392-260]

y2=[540-300, 677-376, 809-453]

y3=[436-265, 540-340, 649-417]

plt.plot(x,y1, label="Using Capacitance Change of 1.25 pF", marker= 'o')
plt.plot(x,y2, label="Using Capacitance Change of 2.5 pF", marker= 'o')
plt.plot(x,y3, label="Using Capacitance Change of 0.5 pF", marker= 'o')


plt.xlabel("Input Voltage (V)")
plt.ylabel("Change in Output Voltage (mV)")
plt.legend()
plt.title("Change in AC Bridge Output Voltage vs. Input Voltage")

plt.show()
