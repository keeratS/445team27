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