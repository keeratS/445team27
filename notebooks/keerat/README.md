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
Met with Amr for weekly meeting. Got feedback on: ways to test prototype circuit to determine caue of fixed 5V output, PCB design administrative details, different options to generate the sinusoid wave (active filter), summing amplifier prototype could have a gain of 2 which could cause the unexpected output, and some feedback about our design doc.

We also attended the PCB review meeting and spoke to Dean about our plan for the PCB. He gave advice including
* ok to use headers to change connections within PCB
* can do multiple boards as long as they are under size requirement
* make sure to use silkscreen labeling as much as possible
* testing points are an exposed pad
* consider using an external oscillator
* break out extra pins
* consider other microcontrollers, check SRAM memory for ATMEGA 328 to check it meets your requirements
* pick QFP parts with pads sticking out, not BGA or QFA with pads that look like bites out of the chip

## 3/6/2022
Created graph from lab data collected on 3/1 to test behavior of the instrumentation amplifier we created from 3 op-amps using the typical circuit design (referenced from the Wikipedia article on instrumentation amplifiers)

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/pythonplot_lab3-1.png?raw=true" style="height:200px"/>

From the graph, we concluded that it has a linear gain relationship between certain input voltages, but that the gain was much smaller than we were hoping.

## 3/7/2022
Jyotsna and I put together the PCB design for the board containing the microcontroller and waveform generator chips, with the understanding that it will be for prototyping and not for use in the final design of the bee house.

## 3/8/2022
Had our weekly meeting with Amr today. He pointed out that the gain pictured on the graph was actually larger than we initially thought. Since we had the demodulator and instrumentation amplifier ICs delivered, we will pursue further testing using the instrumentation amplifier IC rather than the one constructed of 3 op amps. We also uploaded our boards for the PCB order.

## 3/18/2022
Looked into ordering parts for the PCB and realized that the chip shortage is heavily impacting the availability of the ATMEGA328P we intend to use in our design. Jyotsna and I looked at alternative boards, but then I found a through-hole ATMEGA328P pre-loaded with a bootloader available in low stock on a website. We now plan to use that in our design.

## 3/19/2022
Jyotsna and I went into lab to test the behavior of the instrumentation amplifier IC. We concluded that changing the input waveforms changes the output of the chip in a way that matches our expectations, so we will move on with the testing.

## 3/20/2022
Jyotsna and I went into lab to test the behavior of the capacitance sensor system. This included the copper capacitance rings, the tube, the glass beads that simulate bees, and the instrumentation amplifier circuit. The data and graph of this testing are below.

|                     bead                    | Output voltage waveform amplitude no bead in tube | Output voltage waveform amplitude bead between cap rings |
|:-------------------------------------------:|---------------------------------------------------|----------------------------------------------------------|
|           8mm gray synthetic opal           |                       703 mV                      |                          834 mV                          |
|              8mm champagne bead             |                       702 mV                      |                          820 mV                          |
|         6mm unbuffed synthetic opal         |                       701 mV                      |                          754 mV                          |
| 2nd smallest champagne  bead (estimate 6mm) |                       704 mV                      |                          760 mV                          |
|    smallest champagne bead (estimate 3mm)   |                       703 mV                      |                          725 mV                          |

<img src="https://raw.githubusercontent.com/keeratS/445team27/ef045a0d1219dc02987ec9d1b732cdd7fe4ee6f2/notebooks/keerat/labbeadsamplitude.png?token=ADGDZJK2P65VWVQKV7RRJMDCHJVQC" style="height:200px"/>

## 3/22/2022
Had our weekly meeting with Amr today. We discussed the ATMEGA 328P purchasing issue and came to the conclusion to wait a week to see if we get tracking information and if not, we should find an alternate supplier. We also shared updates about work done over spring break, like the capacitance sensor subsystem testing.

## 3/23/2022
Piyush and I spent some time in lab confirming that our understanding of the demodulator was correct, and we found that it matched our expectations. Specifically, we set up a circuit with the demodulator and low-pass filters. I set up a waveform generator so that the demodulator received a 1kHz frequency wave modulated by a 10kHz frequency wave. The demodulator was able to extract the 1kHz frequency waveform when it was fed a 1kHz frequency reference signal. Further testing is required to adapt this behavior to the bee system.

## 3/27/2022
Jyotsna and I met in lab to investigate the MAX 038 waveform generator chip. Early in reading the datasheet[5], we saw that the output waveform’s frequency is controlled by an external resistor and capacitor pair. So Jyotsna figured out the rest of the connections for the chip while I focused on deciding what resistor and capacitor to use for our purposes. Eventually, I calculated that the ideal capacitor would be 3030 pF, and the ideal resistor would be 50k. We tested in the lab with a 3300 pF capacitor and a 47k resistor and found the chip generated a waveform of around 31 kHz, which is close enough to 33kHz for our purposes. This measurement was done with the frequency measurement on the oscilloscope in the 445 lab. We noted that the output waveform was about 2V peak to peak, so we decided to use a 2x amplification with an op amp to make the higher amplitude waveform we needed. After this testing, we decided to move forward with the MAX 038 in our design, and had determined the circuit design necessary to include it in our project.

## 3/28/2022
After the previous tests, I went into lab again to use the output of the instrumentation amplifier as the input to the demodulator, after consulting the datasheet of the demodulator to confirm the necessary connections. After constructing this circuit, which is shown in Figure 8, Jyotsna joined me for the testing portion.

In this test, Jyotsna and I held the tube horizontally using a clamp. We put glass beads in the tube at slow, medium, and fast speeds. We were measuring the output from the instrumentation amplifier (AD620) along with the demodulator (AD630), and found that we did get an asymmetric double pulse from the output of the demodulator, and that the direction of travel of the bead corresponded with the negative or positive orientation of this double pulse.
Initially we were getting noisy readings, but we added a filter before the oscilloscope reading (consisting of 2 1kohm resistors and 1 microfarad capacitor) and found much better results, so we adjusted our circuit plans to include that.

## 3/29/2022
Worked on PCB design of microcontroller PCB with Pi. I determined connections necessary for using external oscillator by consulting ATMEGA datasheet. Jyotsna determined the necessary connections for integrating an SD card.

## 4/7/2022
Piyush and I met in lab and he showed me that he had a blink sketch running on the ATMEGA chip. I confirmed it did make the LED blink, and he described to me how he connected everything to program it. There was not a TA in the lab so we were not able to go through the programming. Pi then said he would handle connecting the SD card.

## 4/8/2022
Jyotsna and I met in lab to continue work on testing the SD card and found that Pi had soldered wires directly to the SD card, making it impossible to put the SD card into any sort of computer for reading it. So we were not able to test the SD card sketch as we had originally planned. Instead, we did research to determine how to integrate an SD reader into our design since Pi's design did not accommodate reading. We found that adding a micro SD card reader module would be best for our intended use case of use by a non-technical person.

## 4/10/2022
Tested dual power supply setup and found it successfully outputs 5V and -5V and ground when set up connecting the positive terminal of one to the negative terminal of the other.

## 4/12/2022
Jyotsna and I met in lab to try the SD card writing sketch again now that the SD card reader parts had arrived. We had trouble getting the program onto the ATMEGA chip, so the test was not run.

I met with Amr today to give updates on the project progress. Jyotsna continued working in lab and Piyush is travelling but he should be making the beginning of the final project report.

Later I rejoined Jyotsna in the lab and found some errors in the connection so we were able to successfully run the SD card test. We were able to successfully write to the SD card with the ATMEGA328P and then read the correct data from our laptops.

## 4/15/2022
Went into lab to solder one sensor board. Finished soldering but didn't get a chance to test to confirm the soldering went well.

## 4/16/2022
Went into lab with Jyotsna. Found that newly soldered sensor board was not performing as expected: it should have behavior matching our breadboard experiements, specifically, a sinusoidal waveform out of the instrumentation amplifier that changes amplitude in response to changes in the tube occupancy, which goes into the demodulator chip and filters, after which the signal increases and decreases proportionally to the change in the earlier waveform. Instead of that expected behavior, we saw no waveform out of the instrumentation amplifier. Tried some troubleshooting technicques with no luck. Duplicated the PCB circuit on a breadboard to be able to probe more points to find the problem, but that circuit behaved as expected. Jyotsna wrote code for the microcontroller board, but that needed the sensor board to generate data so we didn't get a chance to test that either.

## 4/17/2022
Went into lab again to address the sensor board PCB problem. Went point by point to see at what point the PCB circuit and the breadboard circuit differed. Found the disconnect in the instrumentation amplifier chip, and found that I had soldered an op-amp in instead. Fixed that, and saw the expected behavior from the fixed PCB. Problem solved!


<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/67193144629__697EE1FC-7D2E-4903-9944-2EFBC258B2AA.jpg?raw=true" style="height:200px"/>

 I also completed soldering of microcontroller board. I connected it to the power supply and took oscilloscope readings of the waveform generator chips. Foudn that both of them generated a triangle-like waveform, which is not what we need. Was not able to investigate further as it was late into the night.
 
 
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/IMG_3948.jpg?raw=true" style="height:200px"/>

## 4/19/2022
Went into lab again to troubleshoot the waveform generator PCB issue. Duplicated the circuit on a breadboard to find issues, but found that the breadboard circuit worked fine, as in picture below.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/bb_max038_0419.jpg?raw=true" style="height:200px"/>

Pi joined me in lab at this point. We found that the issue was not in the waveform generator setup but in the summing amplifiers on the PCB. I did the calculation to figure out which resistors would be correct for our gain of 2x and Pi soldered the resistors into the PCB.
At this point, we saw that the sinusoidal output was fine, but the square output resembled a triangle wave. We confirmed (as seen in the picture) that the input (bottom waveform) to the amplifier was correct, but the output (top waveform) was wrong. I looked into what could cause the problem and found that the 741 op amp we were using has a low slew rate, which means that it is not able to change otuput fast enough to create a square wave output, causing a rectangular waveform to become trapezoidal. In our case, the effect was so strong it looked triangular. I found a substitutable part (same pinout but hi slew capability) available at the electronic services shop).

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/slew_opamp_419.jpg?raw=true" style="height:200px"/>

After this we replaced the 741 op amps with HA2515 op amps which have a high slew rate and saw that the square wave was properly amplified. At this point we noticed that the generated sin and square wave had a difference in freqency of about 10 KHz. We connected the generated waveforms to the rest of the system (square wave to demodulator reference and sin wave to center ring of capacitor sensor) and connected the outer rings to the sensor board, and found that the output of the demodulator followed the waveform from the sensor, as shown in the picture. Since this is the necessary behavior of the system, we decided not to address the difference in generated waveform frequency.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/keerat/success_boards_419.jpg?raw=true" style="height:200px"/>

Then Piyush implemented a +3 summing amplifier to the output of the demodulator so that the signal would definitely be within the range of the ATMEGA inputs. This was implemented on a breadboard because it was not originally included in the PCB, even though it was planned. We hope to create another PCB with this component. We added this to the output of the above circuit setup and found that it behaved as expected.

## 4/20/2022
I went to lab in the morning with Jyotsna and we found that the ATMEGA circuitry on the PCB was flawed. We created the circuit we needed on a breadboard and began testing code with that. We found that it successfully took measurements from the PCB data and put that data on the SD card. I also soldered another sensor board (now 2/3 sensor boards complete) and verified that it worked as expected. Then we took a break for lunch.

After lunch I went back to lab and continued to refine the code.

## 4/21/2022
I went into lab in the morning and began assembling the electronics on the bee house. I began by disassembling the tube and soldering the inner tube connector to the necessary wires. Then I connected the outer tube connector to the necessary wires, and color coded the wires to their purpose so that they would be recognizable while outside of the connector. Jyotsna and Pi joined later and worked on soldering the last sensor PCB and figuring out an issue where the SD card was not being written to in the loop portion of the ATMEGA code. At this point, Amr joined myself and the rest of my group in 445 lab for our mock demo. Then I finished soldering the final sensor PCB and attached the 3 sensor PCBs to the bee house. I then attached the signal wires from within the tube to their input connections on their respective PCBs. After this, I connected the rest of the setup to the PCBs and confirmed all the connections were successful and the system worked as expected. 

## 4/22/2022
Jyotsna and I spoke to Evan the TA in lab about our issue with the ATMEGA not executing any code in the loop portion. We were not able to find a solution. We did find that the PCB ATMEGA is connected to the external oscillator in a different way than the breadboard ATMEGA is connected, but both ways have been successful on a breadboard.

## 4/24/2022
I tested the SD card module at home, with a serial communication using an Arduino on the advice of Evan the TA.  I was able to successfully get serial messages which made debugging easier. At this point Jyotsna and I went to lab and attempted to debug. I found that, actually the issue about the loop code not executing was because our chip cannot open and write to SD card files that have names with 8 or more characters. Once we changed our files to have shorter names, we were able to move forward. (at this point it was 11:30 at night)
After this we wrote code that was able to take a reading from an analog pin and write it to the SD card in a csv format. We found that the ATMEGA on a breadboard was behaving irregularly so we switched to using an Arduino. At this point, we found out that the summing amplifier which was supposed to make sure that all the voltages going into the Arduino's analog pins was positive was not working, instead, it was outputting negative voltage. (The version that was made on the proto-board is also too large to fit on the house, which will probably be an issue soon.) This is not within the ATMEGA chip's operating area so we had to stop our coding and fix the summing amplifier. We were not able to figure out what was wrong. So we left (at this point it was 2:30 am)

## 4/25/2022
I went to lab and modified the Arduino code to take readings from 3 sensors and write it to the sd card in csv format. Jyotsna worked on creating splitter wires so we would be able to power our device safely and Piyush debugged the summing amplifier. He found that the resistance values were not high enough, so when he replaced the 2.2K resistors with 22K resistors it worked. I started writing python code to take the csv file and turn it into an image.
