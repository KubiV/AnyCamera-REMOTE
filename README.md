# AnyCamera REMOTE
## _Take photos remotely with any camera_

AnyCamera REMOTE is a wired camera remote wich is using [gPhoto2] and a Raspberry Pi. Power the Pi, attach a button to Pi's GPIO and with a USB cable connect camera to Pi. Start taking photos with external button.  

*****
## Installation

- Using [Raspberry Pi Imager] (and Ctrl-Shift-X command) set up SSH and install Raspberry Pi OS Lite on a Raspberry Pi computer.
- Install [gPhoto2] using command 
```
sudo apt-get install gphoto2
```
- Create a "Scripts" folder and add script [p.py] using [GNU Nano] (location: /home/pi/Scripts/p.py) and SSH
- Edit rc.local file: add "sudo python3 /home/pi/Scripts/p.py &" that will make run the script after Raspberry Pi boots up

<img src="https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Images/rclocal_image.png?raw=true" alt="rc.local file opened in text editor" width="500"/>


- Print a [case]
- Add power switch, battery, Li-Io charging circuit, step-up boost board to 5,1 V and micro USB to USB A adapter

<div>
<img src="https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Images/img_2.jpg?raw=true" alt="component position in a case" height="300"  style="float: left;"/>
<img src="https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Images/img_1.jpg?raw=true" alt="assembled case" height="300" />
</div>



*****
## Connecting the button

<a href="https://pinout.xyz"><img src="https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Images/img_pinout.png?raw=true" alt="raspberry pi pinout" height="300" /></a>
<img src="https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Images/img_4.jpg?raw=true" alt="button connection" height="300" style="float: left;"/>

## ende

[gPhoto2]: <http://gphoto.org>
[Raspberry Pi Imager]: <https://www.raspberrypi.com/software/>
[p.py]: <https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Code/p.py>
[GNU Nano]: <https://www.nano-editor.org>
[case]: <https://www.prusaprinters.org/cs/prints/153947-box-for-raspberry-pi-zero-battery-and-buttons/files>