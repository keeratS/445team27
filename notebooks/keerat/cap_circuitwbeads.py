import matplotlib.pyplot as plt

x1=[8,6,3,0]

y1=[820,760,725, 703]

x2=[8,6,0]
y2=[834, 754,704]

y3=[436-265, 540-340, 649-417]

plt.plot(x1,y1, label="Champagne Style Beads", marker= 'o')
plt.plot(x2,y2, label="Assorted Other Beads", marker= 'o')


plt.ylabel("Amplitude of Output Voltage Waveform (mV)")
plt.xlabel("Diameter of Bead")
plt.legend()
plt.title("Change in AC Bridge Output Voltage vs. Different simulated tunnel insects")

plt.show()
