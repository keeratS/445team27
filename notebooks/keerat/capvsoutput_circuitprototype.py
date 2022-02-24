import matplotlib.pyplot as plt

x=[0.5, 1.25, 2.5]
y=[540-340, 321-204, 677-376]

plt.plot(x,y, marker='o')

plt.xlabel("Change in Capacitance (pF)")
plt.ylabel("Change in Output Voltage (mV)")

plt.title("$\Delta$ AC Bridge Output Voltage vs $\Delta$ Capacitance for 5V input")

plt.show()
