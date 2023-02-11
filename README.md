# Click-2.0 (On Pause)
*Currently on pause*

Documenting the intergration of smartness/automation into my robot computer xy plotter

The general idea: Get something to recognize what's on the screen, what is the screen, and how that thing can move a mouse to click stuff on said screen.


Current stage: make a python program that can do that first before attempting to integrate with my robot x-y plotter
Test environment: Cookie Clicker (has objects that can be identified, can still be used to integrate with robot x-y plotter, not too action intensive and fun to watch while coding the program)

The robot has a webcam and can run image detection, so we need to create a program that can do things without parsing webpages. The program has to:
- figure out where the screen is (find relative limits/calibrate search area for camera)
- identify numbers by the way they look
- be able to control the x-y plotter (convert pixels to mm)

Pseudo Code:

Open CV parts
- Identify window with cookie clicker open on screen (Note down pixels to create square for object search)
- Scan the area for desired target
- Convert target location into directions the x-y plotter should follow

*send target location instructions to arduino*

Arduino part:
- plug instructions into a steppermotor function
- Stepper motor sets the number of steps to get to the target
- Click after reaching target

Repeat over and over again
