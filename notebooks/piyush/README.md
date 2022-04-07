2/8/2022

Talked to machine shop about physical design of the bee house, including dimensions, number of tubes and where they would go.
We decided we would use 8 mm id tubes, and 4 tubes vertically stacked. We were told to come back once we knew what specific materials we wanted.

2/10/2022

I created CAD files for the bee house, and Keerat added the capacitor setup.

2/18/2022

I did the circuit analysis for the first two parts of the circuit (AC bridge and instrumentation amplifier).

2/19/2022

We built a circuit for prototyping a very basic version of the capacitance detector on a breadboard.

2/26/2022

I prototyped a voltage summer circuit on a breadboard to add a DC offset to the output voltage to ensure that it is in a range
that is readable by the microcontroller, since the output voltage can be negative and the microcontroller only reads voltages between 0.5 and 5V. The experiment was unsuccessful because the sum of the two voltages did not match what the voltage summer outputted. I will debug some more in office hours later.

3/8/22

Designed part of the PCB for the circuit. Designed the schematic and PCB for the AC bridge circuit, instrumentation amplifier,
balanced demodulator, and output amplifier and summing amplifier for adding a DC offset to the output. Jyotsna and Keerat worked
on the part of the PCB for the microcontroller and waveform generator.

3/23/22

Prototyped the balanced demodulator in the lab on a breadboard with just a sine waveform (instead of a DC signal modulated with a sine). 
The output should be a rectified sine wave, but instead I got two sine waves, one offset from the other by a phase of around 100 degrees. Not sure why.


3/28/22 - 3/29/22 Designed PCB V2 for microcontroller board. Researched the difference between an oscillator and a crystal, figured out that ECS-100AX which we had was an oscillator, not a crystal. Submitted gerber files to PCBway and it passed the audit.

4/4/22 

Verified that I was able to program the atmega with an external oscillator.

4/7/22 

Soldered and wired up the SD card to the ATMega. Also found a tutorial on how to wire up and code the SD card. 