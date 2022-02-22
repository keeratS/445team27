## 2/8/2022

Spoke to Gregg in machine shop about physical design of bee house.
Covered idea of removable tubes with connector piece to allow us to tinker with positioning as necessary while developing the device.
Discussed dimensions of house (8mm id tubes, square piece 2 in., house itself 5 or 6 across, tubes 5 or 6 deep)
We were advised to look into desired materials and specifics about sensing setup.

Decided on metal balls for bee and parasite simulation for demo because of availability of variety packs of ball bearing sizes.

## 2/10/2022

Pi created CAD files for the physical model of the bee house, I added the capacitor setup that we discussed yesterday.
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/beehouse_cutawaywcaps.png?raw=true" style="height: 100px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/beehouseiso_tube%20out_proposal.png?raw=true" style="height:200px"/>

## 2/15/2022

Met with Amr (TA) to discuss weekly progress. Determined that metal balls were not suitable for the demo, and plastic or other insulating materials should be used. Recommended to test different materials to see what produces the most change in capacitance.

## 2/19/2022

Built a circuit for prototyping initial sensor circuit concept. Used capacitors in parallel to simulate the increased capacitance caused by a bee going in between capacitor plates. Measured voltage out of op-amp with oscilloscope in 445 lab. Drove AC bridge with varying amplitudes of a 33kHz sinusoidal waveform (from waveform generator in 445 lab) and varying numbers of capacitors in the parallel arm to see what behavior of the circuit would be at different voltages and with different changes in capacitance.

Data collecting procedure as follows:
1. Turn off power supply and waveform generator outputs. Wait a few seconds. Adjust the parallel capacitor arm to contain the desired amount of capacitors.
2. Turn on the power supply and the waveform generator output.
3. If bee passage should be simulated, press button to include parallel capacitor arm in circuit.
4. Turn on the measure capability of the oscilloscope.
5. Wait 5 seconds.
6. Write down the mean amplitude measured by the oscilloscope.
7. Repeat steps 1-4.
8. Write down the "current" measured value of the amplitude measured by the oscilloscope. If the number is changing, use the number that shows up for the most time.

So for each combination of input waveform and capacitor number, we have two measurements: one average over 5 seconds and one observation.

The data we collected is as follows:

| Input Voltage (V) | # capacitors | Balanced C (obs & avg) (mV)| Unbalanced C (obs & avg) (mV) |
| :-----------: | :-----------: | :-----------: | :-----------: |
| 4 | 8 | 250 & 258 | 340 & 340 |
| 5 | 8 | 270 & 280 | 470 & 434 |
| 6 | 8 | 310 & 330 | 510 & 520 |
| 4 | 4 | 410 & 385 | 660 & 661 |
| 5 | 4 | 500 & 496 | 765 & 773 |
| 6 | 4 | 560 & 558 | 880 & 894 |

We also noticed that the output  voltage of the oscilloscope was not stable, sometimes the waveform was interrupted by a large spike. These spikes varied in height and occurred infrequently and unpredictably.

## 2/22/2022
Following the above procedure I collected data another time, with an even lower change in capacitance. Data collected is shown below.

| Input Voltage (V) | change in capacitance (pF) | Balanced Amplitude (mV) | Unbalanced Amplitude (mV) |
|-------------------|----------------------------|-------------------------|---------------------------|
|         4         |             2.5            |           300           |            540            |
|         5         |             2.5            |           376           |            677            |
|         6         |             2.5            |           453           |            809            |
|         4         |            1.25            |           160           |            249            |
|         5         |            1.25            |           204           |            321            |
|         6         |            1.25            |           260           |            392            |
|         4         |             0.5            |           265           |            436            |
|         5         |             0.5            |           340           |            540            |
|         6         |             0.5            |           470           |            649            |
