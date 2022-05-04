2/8/2022

Talked to machine shop about physical design of the bee house, including dimensions, number of tubes and where they would go.
We decided we would use 8 mm id tubes, and 4 tubes vertically stacked. We were told to come back once we knew what specific materials we wanted.

2/10/2022

I created CAD files for the bee house in SolidWorks, and Keerat added the capacitor setup.

![alt text](https://github.com/keeratS/445team27/tree/main/notebooks/piyush/bee_house_cad.jpg?raw=true)

2/18/2022

I did the circuit analysis for the first two parts of the circuit (AC bridge and instrumentation amplifier).

2/19/2022

We built a circuit for prototyping a very basic version of the capacitance detector on a breadboard.

2/26/2022

I prototyped a voltage summer circuit on a breadboard to add a DC offset to the output voltage to ensure that it is in 
a range that is readable by the microcontroller, since the output voltage can be negative and the microcontroller only 
reads voltages between 0.5 and 5V. The experiment was unsuccessful because the sum of the two voltages did not match 
what the voltage summer outputted. I will debug some more in office hours later.

3/8/22

Designed part of the PCB for the circuit. Designed the schematic and PCB for the AC bridge circuit, instrumentation amplifier,
balanced demodulator, and output amplifier and summing amplifier for adding a DC offset to the output. Jyotsna and Keerat worked
on the part of the PCB for the microcontroller and waveform generator.

3/23/22

Prototyped the balanced demodulator in the lab on a breadboard with just a sine waveform (instead of a DC signal modulated with a sine). 
The output should be a rectified sine wave, but instead I got two sine waves, one offset from the other by a phase of around 100 degrees. Not sure why.

3/28/22 - 3/29/22 

Designed PCB V2 for microcontroller board. Researched the difference between an oscillator and a crystal, figured out that ECS-100AX
which we had was an oscillator, not a crystal. Submitted gerber files to PCBway and it passed the audit.

4/4/22 

Verified that I was able to program the atmega with an external oscillator.

4/7/22 

Soldered and wired up the SD card to the ATMega. Also found a tutorial on how to wire up and code the SD card. 

4/10/22 

Worked on the final report. Looked at final report guidelines and template. Created cover page and downloaded
final report LaTex template. Copied over some information from design document and wrote abstract.

4/12/22

Worked more on the final report. Moved block diagram to introduction, modified design section as per final 
report guidelines.

4/19/22

Debugged PCB V2 in the lab with Keerat. When testing the waveform generator, we found that the issue was that
we were probing the output of the operational amplifier, whose resistors were not soldered yet. Once we fixed that,
we verified that the waveform generator worked on the PCB. We also realized that we forgot to include the summing 
amplifier for the sensor board to boost the output of the balanced demodulator to a positive voltage which the 
microcontroller can read. So, we constructed this non-inverting summing amplifier on a breadboard and tested it,
verifying that it showed the intended double pulse waveform on the oscilliscope, shifted up by 3V so that it was
always positive.

4/20/22

Designed a small PCB to include the summing amplifier to boost the output of the balanced demodulator to a positive 
voltage readable by the microcontroller.
