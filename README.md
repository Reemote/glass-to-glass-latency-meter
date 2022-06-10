# Introduction
This 

# Installation instructions
1. Install Arduino IDE from [here](https://www.arduino.cc/en/Main/Software) (only required for actual compilation, not for running latency tests)
2. Connect the Arduino to USB
3. Running `ls -l /dev/ttyACM*` should give you `crw-rw-rw- 1 root dialout 166, 0 Okt 29 10:51 /dev/ttyACM0` 
4. Run `sudo usermod -a -G dialout <USERNAME>` (make sure to put in proper username)
5. Run `sudo chmod a+rw /dev/ttyACM0` to resolve any permission issues with access to USB port

# Setup instructions

1. Point the LED towards the camera
2. Tape the phototransistor to the screen and place the video stream in front of it
3. You should see the LED blinking with 1 second interval
4. Run `sudo python latency_reader.py` to kick off a measurement session

