## 2/8/2022

Talked to machine shop about physical design of the bee house, including dimensions, number of tubes and where they would go.
We decided we would use 8 mm id tubes, and 4 tubes vertically stacked. We were told to come back once we knew what specific materials we wanted.

## 2/10/2022

I created CAD files for the bee house in SolidWorks, and Keerat added the capacitor setup.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/bee_house_cad.png?raw=true" style="height: 400px"/>

## 2/18/2022

I did the circuit analysis for the first two parts of the circuit (AC bridge and instrumentation amplifier).

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/circuit_analysis.png?raw=true" style="height: 400px"/>

## 2/19/2022

We built a circuit for prototyping a very basic version of the capacitance detector on a breadboard.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/breadboard_AC_bridge.jpg?raw=true" style="height: 400px"/>

## 2/26/2022

I prototyped a voltage adder circuit on a breadboard to add a DC offset to the output voltage to ensure that it is in 
a range that is readable by the microcontroller, since the output voltage can be negative and the microcontroller only 
reads voltages between 0.5 and 5V. The experiment was unsuccessful because the sum of the two voltages did not match 
what the voltage summer outputted. I will debug some more in office hours later.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/summing_amplifier_research.jpg?raw=true" style="height: 400px"/>

## 3/8/22

I designed part of the PCB for the circuit. I designed the schematic and PCB for the AC bridge circuit, instrumentation amplifier,
balanced demodulator, and output amplifier and summing amplifier for adding a DC offset to the output. Jyotsna and Keerat worked
on the part of the PCB for the microcontroller and waveform generator. Eventually, we decided to split the design into two
boards, a microcontroller board and a sensor board. Here is the schematic and PCB for the sensor board V1:

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/sensor_board_schematic_V1.png?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/sensor_board_PCB_V1.png?raw=true" style="height: 400px"/>

## 3/23/22

I prototyped the balanced demodulator in the lab on a breadboard with just a sine waveform (instead of a DC signal modulated with a sine). 
The output should be a rectified sine wave, but instead I got two sine waves, one offset from the other by a phase of around 100 degrees. Not sure why.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/balanced_demodulator_circuit.jpg?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/balanced_demodulator_output.jpg?raw=true" style="height: 400px"/>


## 3/28/22 - 3/29/22 

I designed the V2 of the PCB for the microcontroller board. I researched the difference between an oscillator and a crystal,
and figured out that ECS-100AX which we had was an oscillator, not a crystal. An oscillator needs to be powered, and it is
an active device. On the other hand, a crystal alone cannot provide a clock for a microcontroller - it also needs external
capacitors as well as an oscillator circuit. I also submitted gerber files to PCBway and it passed the audit.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/oscillator_vs_crystal.png?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/microcontroller_board_schematic_V2.png?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/microcontroller_board_PCB_V2.png?raw=true" style="height: 400px"/>

## 4/4/22 

Verified that I was able to program the atmega with an external oscillator (uploaded a blink sketch).

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/ATmega_external_oscillator.jpg?raw=true" style="height: 400px"/>

## 4/7/22 

I soldered and wired up the SD card to the ATMega. I also found a tutorial on how to wire up and code the SD card. 

## 4/10/22 

I worked on the final report. I looked at final report guidelines and template, created a cover page, and downloaded
the final report LaTex template. I copied over some information from our design document and wrote the abstract. I realized
that I shouldn't have soldered headers to the SD card since we needed to plug it in to a user's computer - as a result, 
we bought a new SD card connector and SD card with a micro-SD card adapter.

## 4/12/22

I worked some more on the final report. I moved the block diagram to the introduction, and modified the design section as per final 
report guidelines.

## 4/19/22

Debugged PCB V2 in the lab with Keerat. When testing the waveform generator, we found that the issue was that
we were probing the output of the operational amplifier, whose resistors were not soldered yet. Once we fixed that,
we verified that the waveform generator worked on the PCB. We also realized that we forgot to include the summing 
amplifier for the sensor board to boost the output of the balanced demodulator to a positive voltage which the 
microcontroller can read. So, we constructed this non-inverting summing amplifier on a breadboard and tested it,
verifying that it showed the intended double pulse waveform on the oscilliscope, shifted up by 3V so that it was
always positive.

## 4/20/22

I designed a small PCB to include the summing amplifier to boost the output of the balanced demodulator to a positive 
voltage readable by the microcontroller.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/voltage_adder_schematic.png?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/voltage_adder_PCB.jpg?raw=true" style="height: 400px"/>

## 4/23/22 - 4/25/22

I helped debug the PCB. For some reason, the ATmega microcontroller was working fine on the breadboard but was not being programmed 
on the PCB in the exact same configuration. We tried to use a heat gun, solder wick, and a desoldering pump to remove it, but with
little success. Eventually, we decided to solder all of the components onto an entirely new PCB, since we had at least 2 counts of all 
of the components on hand (except the uA741 op-amps, which we had to get from the services shop). Lesson learned - do not use a through 
hole microcontroller on a PCB if you want to desolder it. After much debugging, we finally got all of the components working on the PCB.
Jyotsna and I talked to Glen about some last minute PCB mounting and a stand for the bee house. We realized that the SD card connector 
was hardwired to the wrong pin on the PCB, which is why it wasn't being written to correctly - luckily, we had broken out all spare pins 
on the PCB, so we were able to connect the SD card to a different pin. Just in time for the demo, we confirmed that our entire system 
worked as expected.

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/microcontroller_board_debugging.jpg?raw=true" style="height: 400px"/>

## 5/2/22

I helped create the final presentation and practiced presenting.

## 5/2/22 - 5/4/22

I helped record the final project video along with Keerat and Jyotsna. I learned how to use Davinci Resolve for video editing,
and edited the video. 

<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/video_editing.png?raw=true" style="height: 400px"/>
<img src="https://github.com/keeratS/445team27/blob/main/notebooks/piyush/bee_house.jpg?raw=true" style="height: 400px"/>


5/4/22 - 5/5/22

I worked on the final report, along with Jyotsna and Keerat. I wrote the introduction, design overview, some design details, and 
the conclusion section. I also wrote some equations in latex, proofread the paper for grammar/spelling errors, and modified the 
section about the balanced demodulator after obtaining a better understanding of how it works. I was under the impression that it
only outputs the modulated DC signal, and its only function is to reduce the noise of the modulated signal. However, it does 
both - it demodulates the signal and removes noise.

