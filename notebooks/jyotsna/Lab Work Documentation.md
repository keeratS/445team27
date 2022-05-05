Lab Work Documentation

Feb 8, 2022:
Visited the Machine Shop to discuss our physical design needs for this semester. Explained our project to Gregg and received some feedback 
about tunnel sizing. Will be looking into suitable materials for tunnel and bee simulation. Currently thinking to go with spherical
metal balls, such as ball bearings, as this is what was chosen in the UEPI research paper and shown to work. 

Feb 15, 2022:
First meeting with TA Amr Ghoname; decided to start looking into other materials to simulate bee, as steel or metal might not be suitable to work
with our sensor rings.

Feb 19th, 2022:
Headed into lab with my group mate Keerat Singh, and began to build our prototype AC bridge circuit. This is going to be the core mechanism that will make
our detection sucessful. 

We set up the arms of the AC bridge with different capacitor values by combining capacitors in series to create unequal capacitance values in the two arms. 
Drove AC bridge with 33 kHz sine waveform to mimic how system will work when we have our sensors in hand. Tried to collect data by simulating
a bee passing through by unbalancng the circuit as described in the previous few sentences. 

Data collecting procedure as follows: (this passage is the same as my partner Keerat's, as we conducted these tests together)

- Turn off power supply and waveform generator outputs. Wait a few seconds. Adjust the parallel capacitor arm to contain the desired amount of capacitors.
- Turn on the power supply and the waveform generator output.
- If bee passage should be simulated, press button to include parallel capacitor arm in circuit.
- Enable "measure"  on oscilloscope.
- Wait 5 seconds to allow mean value to be calculated (this was done so we could get a steady value 
                                                     as the signal seemed a little jumpy, system seemed susceptible to noise)
- Write down the mean amplitude measured by the oscilloscope.
- Repeat steps 1-4.
- Write down the "current" measured value of the amplitude measured by the oscilloscope. If the number is changing, use the number that shows up for the most time.

Please find the data collected in this repo: the figure is named AC_data_collection_2_19_2022.png

Feb 21, 2022:
Researched what the dielectric constant of bees could be, found a research paper at https://etda.libraries.psu.edu/files/final_submissions/18863,
by Omar Alzaabi at Penn State Univeristy, were he has conducted studies into the properties of airborne insects using radar. By observing how the presence of the insects
interacts with the emitted radar, Alazaabi concludes the dielectric constant value of a honey bee is about 10. Using this value as a guideline, further 
research led me to find that glass has the closet dielectric value to 10. 

Feb 20th, 2022:
Worked on creating the design document for our design document check. Worked on creating the block diagram for our system as we understand at this time.
Created requirements and verification tables and content. 

Feb 21, 2022:

We attended our design document check. Prf Victoria Shao, and TAs Amr, David, and Evan were in attendance. We received some feedback, namely that
we could add visual indicators to the beekeepers that action is needed on their part to secure their tunnels. I recevied some notes to make the 
block diagram more clear, as I had forgotten to add a legend; I think I will add some captions by the arrows to clarify their roles as well. 

General feedback included:
- no need for seperate processor to perform data analysis, could do it al on ATMega
- could do copper tape instead of copper rings to make sensors; could help in making sensor profiles smaller
- visual indicator for beekeper to take action, like LEDs
- there could be off the shelf components we could use to do wat our capacitance sensors could do

Feb 22, 2022:
Weekly Meeting with Amr, reported on our progress this week. Discussed making only one or two tunnels to save on cost, as parts seem to be quite expensive, and
we have only $150 in course provided budget. We spoke that this will be aceptable for demo. Our meeting focused a 
bit more this time on writing the design documents, and discussed best practices and points for imporovement based on the check. 

Feb 24th, 2022:
Made the block diagram better, final version we used in our design document check can be seen in this repo under the name block_diagram_DDC.png
Spent today writing and finishing the Design Document 

Feb 25th, 2022:
Keerat and I met today to find a wave to generate the waveforms [ 33kHz sine and square waves] needed for our applications. Our original plan was to use the 
ATMega to generate these signals from its PWM digital out pins, but I found from online resources that manipulating this waveform more finely can be difficult
with the ATMega. It seems to be easy to change values like the duty cycle, as the PWM / digital IO library has functions to help users do that, but changing 
the frquency needs lower level code to manipulate the clock and timer registers in the ATMega328P. Forums didn't have much good guidance on how to do this, and
it seemed that this method would anyways not generate a 33 kHz signal in the way we envisoned. 

Main source of information: https://www.arduino.cc/en/pmwiki.php?n=Tutorial/SecretsOfArduinoPWM
More sources were consulted but they were more like forum posts.

Feb 27th, 2022:
Keerat and I went into lab to debug our prototyping circuit, as she had previously sen some weird behavior in the AC bridge circuitry. Balanced and unbalanced circuitry / input into the AC bridge generated the same constant 5 V output from the Instrumentation Amplifier we had constructed out of three opamps. We simply are simply stumped by this behavior. Did some reading on how and why instrumentation amplifiers work; really realizing that I am reaching the depth of my EE knowledge, so am working hard to get a better understandind of the inner workings of this component. 

We decided we would need Amr's help in understanding what is going on, so we emailed him.

Feb 28th, 2022: 
Attended our Design Document Review: in attendance were Prf Victoria Shao, Amr, and three of our peers from class. Feedback on design had been addressed previously in our design document check, so there was not much discussion on the design choices today. Our third groupmate was not at this review. 

March 1, 2022:
Eventful day ! 

Met Amr for weekly meeting, and asked him our questions from the wonky behavior of our test circuit.
Was in some talks with the Machine Shop as work on our Bee House has begun. 

Attended the PCB design review meeting and met Dean. He had some excellent advice on what to do for our PCBs, especially as we are not yet sure 
how the system will come together in the end. We decided we will lead our ATMEGA pins onto header pins for maximum design flexibility. Deciede to also use external oscillator component for our ATMega.

March 7, 2022:
Worked with Keerat to create the microcontroller board for the draft 1 deadline. We think this board will not be used in the final integration, as many things in our design are still coming together and our understanding of the waveform generating chips and the ATmega will probably evolve between now and final build. 

Thursday before spring break
in discussions with glen about tunnels

Friday before spring break
soldered wires onto the rings machined by Glen
Assembled prototype tunnel
checked continuity from sensor to wire connection, all passed

Thursday of Spring Break
bought beads

March 20, 2022:
Connected the prototype tunnel to the instrumentation amplifier, sucessfully saw change in amplitude from the output of the instrumentation amplifier when a glass bead
was passed through the sensor



March 21, 2022:
Delivered sensor rings with wires attached back to Glen so that they could be mmounted inside the tunnel.

April 7, 2022:
Picked up Mason Bee House structure from Machine Shop

April 8, 2022:
Was in lab for about 1.5 hours; worked with Keerat on getting Atmega328 up and running on our laptops based on work Piyush had done. 
Concluded that current system that was setup [ SD card is soldered to headers, and Atmega writes directly to SD Card] will not work for our long term use. 
Decided instead that we would need an SD card reader, so that we may eject SD card from microcontroller board and insert into PCs. 

April 10, 2022:
[with Keerat]
Received the power supplies we had ordered, and tested the method we had learned from online [insert resource here] that
allows us to get both positive and negative voltage for our application/ICs. Confirmed that we can +5 and - 5 out of the power supplies, 
will test it this coming week on our actual circuit.

April 12, 2022:
[with Keerat]
Worked on SD card reading. There were some initial problems with the Atmega cirucit: it's connection to the crystal oscillator case was incorrect 
[ XTAL1 was  not grounded, XTAL2 was unused, this is not how it is supposed to be], and through some error in disassembling Piyush's original wiring up of the Atmega circuit , 
we messed up the crystal connection. RESET pin [pin 1] also needed to be pulled high using a resistor [ it was connected directly to VCC by me ]. Zadig did not work as intended,
but using "Program using Programmer" combined with selecting a COM port made programmer easy/possible to use. 
MicroSD card module was then connected; microSD card was formatted and then used with adapter/module. Test circuit of connection to microSD card works: "Testing 1,2,3" appears
in a file named TEST on the microSD card. 

Will work in next lab session to read signals from the demodulator. 

April 16, 2022:
[with Keerat]

Tested the first soldered Sensor Board [soldered by Keerat], and found that the output of the demodulator was not at all what was expected. The demodulator chip simply was 
not responding to input from the instrumentation amplifier. Tried to find the issue by checking continuity between joints and found that joints were connected thoroughly. 
All resistors and capacitors were also verified to be soldered on well to the best of our knowledge. Rebuilt the cicrcuit form the PCB onto breadboard to double check PCB
circuit functionality, and saw that everything was working as expected. Decided to solder a new sensor board, got halfway through. Keerat will retouch solder on originally 
soldered sensor board PCB and retest behavior; hopefully this will resolve our issue. 

Update from the future: retouching solder joints worked

Somewhere along the way:
- learned that there are a few ways to get atmega boot up and running

- created serial interception device with keerat and her arduino to get serial monitor output. helped a little in debugging our sd card issue

- sd card issue


April 25th, 2022:
Big Assembly Day, big problem solving day
April 26th, 2022:
Finished final integration of device
Demo
