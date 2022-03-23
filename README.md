# AnyCamera REMOTE
## _Take photos remotely with any camera_

AnyCamera REMOTE is a wired camera remote wich is using [gPhoto2] and a Raspberry Pi. Power the Pi, attach a button to Pi's GPIO and with a USB cable connect camera to Pi. Start taking photos with external button.  

## Installation

- Using [Raspberry Pi Imager] (and Ctrl-Shift-X command) set up SSH and install Raspberry Pi OS Lite on a Raspberry Pi computer.
- Install [gPhoto2] using command 
```
sudo apt-get install gphoto2
```
- Create a "Scripts" folder and add script [p.py] using [GNU Nano] (location: /home/pi/Scripts/p.py) and SSH
- Edit rc.local file: add "sudo python3 /home/pi/Scripts/p.py &" that will make run the script after Raspberry Pi boots up

<img src="https://raw.githubusercontent.com/Kub1V/AnyCamera-REMOTE/main/Images/rclocal_image.png?token=GHSAT0AAAAAABSW32BEMTDMRAOK7BCTJD2AYR23LTA" alt="rc.local file opened in text editor" width="200"/>



[gPhoto2]: <http://gphoto.org>
[Raspberry Pi Imager]: <https://www.raspberrypi.com/software/>
[p.py]: <https://github.com/Kub1V/AnyCamera-REMOTE/blob/main/Code/p.py>
[GNU Nano]: <https://www.nano-editor.org>