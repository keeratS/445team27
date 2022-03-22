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

## 2/21/2022
Today my group did our design document check where we got feedback on our design document graph from Porfessor Victoria Shao, our TA Amr, another TA David Null, and another TA. The feedback we received included:
* making the block diagram more clear by providing details on the different arrows
* looking into off the shelf chips for the capacitance sensor circuitry
* looking into copper tape rather than copper tubing for the sensor itself
* considering removing the processor and doing all the data analysis and storage from the ATMEGA
* making sure the wires from the sensor to everything else are as short as possible
* specifying how much data we expected to store on the SD card
* adding some sort of warning to the outside of the mason bee house if it is suspected to have a parasite or other issue
* making sure each capacitor pair has its own amplifier

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

 Also today, I met with Amr along with my teammates. We discussed that the irregular behavior from the prototype circuit could be from the open circuit that is introduced because of the switch. He recommended that we construct a circuit and switch out capacitors betweent aking measurements, to make the prototyping tes tmore accurate to the intended use case. He also recommended adding a graph that showed change in capacitance vs output voltage for a fixed input voltage, along with the input voltage versus change in output voltage graph I made earlier in the day. He also advised that we could write to an SD card fromt eh ATMEGA directly, using instructions from the 445 website wiki. We also discussed some of the feedback we got from the design document review, including whether to create a companion desktop app for our device (conclusion was probably not but we could take a look again once it got to that stage), reducing the tunnnels in our project (he said it would be ok to do 2 instead of 4), and we went over feedback from our proposal so that we could improve the writing and report for our design document.

## 2/25/2022
I met with Jyotsna to do research on producing the necessary waveforms to drive the capacitance circuitry from the ATMEGA. Jyotsna looked into producing a square wave of 5V and 33kHz from the ATMEGA while I looked at what would be necessary to turn that into a sinusoidal wave. I found that an RC filter should work for this purpose as long as the time constant fit our desired frequency. A 3 stage filter (3 RC pairs) were recommended as "enough" to round out the square into a sinusoidal shape, with 4.7 nF capacitors and 100k Ohm resistors.

## 2/26/2022
I went into lab to test out the RC filter design along with the changes to the prototyping circuit. I found that 3 RC pairs created a waveform that looked like a triangle wave on the oscilloscope, so I added a fourth RC pair which resulted in a sinusoidal shape. However, with 4 resistors and 4 capacitors, the amplitude of the waveform was reduced to 1.25 V. Thus, I concluded that a passive filter on the ATMEGA- generated square wave would not be sufficient for our purposes of driving the AC bridge, and we should look into an off-the-shelf waveform generator part.

I also tested the modified AC bridge circuit and found unexpected behavior. Even after using a balanced (equal) capacitance on both arms of the AC bridge, the circuit outputted 5V constant. At this point I double checked the wiring, found no flaws, and tabled the issue for later. Piyush Sud was also in the lab and checked the circuit.

## 2/27/2022
I went into lab to test the prototyping circuit again, along with my teammate Jyotsna Joshi. Found the same behavior. Re-wired it on a different breadboard and again found the same behavior. Checked whether it responded to an unbalanced bridge (0.5 pF on one arm and 10/11 pF on the other arm) and found the same result: a 5V constant output from the op-amp. At this point we decided that we needed support from a TA, so we emailed Amr.

## 2/28/2022
Today we had our design document peer review. Professor Victoria Shao and our TA Amr were in attendanc along with 3 students from the class. They had no feedback on the design but had some feedback on the placement of figures within the report. 

## 3/1/2022
Met with Amr for weekly meeting. Got feedback on: ways to test prototype circuit to determine cause of fixed 5V output, PCB design administrative details, different options to generate the sinusoid wave (active filter), summing amplifier prototype could have a gain of 2 which could cause the unexpected output, and some feedback about our design doc.

We also attended the PCB review meeting and spoke to Dean about our plan for the PCB. He gave advice including
* ok to use headers to change connections within PCB
* can do multiple boards as long as they are under size requirement
* make sure to use silkscreen labeling as much as possible
* testing points are an exposed pad
* consider using an external oscillator
* break out extra pins
* consider other microcontrollers, check SRAM memory for ATMEGA 328 to check it meets your requirements
* pick QFP parts with pads sticking out, not BGA or QFA with pads that look like bites out of the chip

Lab Work:
Took measurements with behavior of instrumentation amplifier constructed using 3 op amps. Data collected is shown below:
| V1    | V2   | Output voltage |
|-------|------|----------------|
|   2   |   2  |      2.32      |
|   2   | 2.01 |      2.755     |
|  2.01 |   2  |      1.87      |
| 2.001 | 2.00 |      2.175     |
|  2.1  |   2  |      1.81      |
|   2   |  2.1 |      4.28      |
|   2   |  2.5 |      4.28      |
|   2   | 2.05 |      4.281     |
|   2   | 2.04 |      4.135     |

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/pythonplot_lab3-1.png?raw=true" style="height: 400px"/>

## 3/6/2022
Investigated MAX038 chip from Electronic Services Shop to determine if it would be ok for our use case. Concluded tha tit should be fine if we are able to amplify the output from 1v amplitude to 5v amplitude. Still need to determine the exact resistor and capactior to set the frequqncy to 33kHz but all other pin connections have been determined.

PCB Design: Realized that previous planning had not accounted for the need for one demodulator for each capacitor pair. Adjusted plans to take 3 pairs per tube into account.
