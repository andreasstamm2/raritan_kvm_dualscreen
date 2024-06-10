The following test set-up can be used to check if your target PC is set up to be controlled with the KVM switch.
We use a Raspberry Pi to simulate an absolute mouse.
In a small script we position the cursor at different points on the screen.
If this works we can see that the PC can be controlled and that the cursor positions should align.

We need a Raspberry Pi Zero W (the old one):<br>
[Raspberry Pi Zero W (Amazon.com)](https://www.amazon.com/dp/B06XFZC3BX)<br>
I would also suggest to use a housing which makes it more comfortable (but this is not needed at all):<br>
[Raspberry Pi Zero W Housing (Amazon.com)](https://www.amazon.com/dp/B075FLGWJL)<br>
<br>
And you will definetly a micro SD card.

<b>Shortcut:<br></b>
Below I will explain how the Raspberry Pi Linux system can be set up.
If you just want the the running tool you can skip this and follow this instruction about flashing the micro SD card instead:<br>
[Shortcut showing how to flash the finished image to the SD card](README_test_shortcut.md)

<b>Detailed setup:<br></b>
First of all you need the Raspberry Pi OS which you can get using the official Raspberry Pi Imager:<br>
[Raspberry Pi Imager (Windows, latest)](https://downloads.raspberrypi.org/imager/imager_latest.exe)<br>
You should select "Raspberry Pi Zero", <b>NOT</b> "Raspberry Pi Zero 2"
Then chose "Raspberry Pi OS (other)" and select "Raspberry Pi OS (Legacy, 32-bit) Lite".
Then chose the SD-card that you want to use for the Raspberry Pi.
<b>Settings "General":<br></b>
In the general settings, select "username + password".
You will need this when connecting to your Raspberry Pi through SSH later.
Wifi:<br>
You should set a Wifi-Network, so that you can connect to your Raspberry Pi in your local network.
Settings "Wifi":<br>
<b>Settings "Services":<br></b>
Activate SSH and choose to use password instead of public-key.

The continue so that the Image will be written to the SD card.
After a couple of minutes you can take out the SD card and put it in your Raspberry Pi.

Make sure that you use a data cable Mini-USB to USB!
Not all cables that have Mini-USB on the one side and USB on the other are data cables.
Some just power up the Raspberry Pi, so that you see the LED flashing, but you later wonder why nothing more is happening :-)

Connect the "real" data cable to the data port of the Pi:<br>
<img src="https://github.com/andreasstamm2/raritan_kvm_dualscreen/assets/162843177/33ebbedf-3e9d-406e-bbf3-e982b6c71d9b" width="546" height="300">

Find out the IP address of the Raspberry Pi in your local network (probably through the admin page of your router) and connect via ssh (I use Putty as my SSH client) to your Raspberry Pi.
Use the credentials that you set with the Raspberry Pi Imager above.
If you are logged in to your Raspberry Pi:

Add the following line to /boot/config.txt 
```
dtoverlay=dwc2
```

For that you can e.g. use the nano editor
```
sudo nano /boot/config.txt
```

We are using the Config-Filesystem (ConfigFS) to create/simulate our USB HID device, the mouse.
For this we use the script in [myusbmouse](myusbmouse)
to create a USB HID device with absolute mouse mode using configFS.
This script should be copied to /usr/bin/
Then make is executable by running
```
sudo chmod +x /usr/bin/myusbmouse
```

Make sure that the script is put in the boot-up-sequence:
Edit /etc/rc.local as root and add the following  before the line ‘exit’.
```
sudo nano /etc/rc.local

/usr/bin/myusbmouse # libcomposite configuration
exit
```

At the end of the script there is a call to the test script that will actually move the mouse cursor.
You need to replace <USERNAME> with the actual user that was created on the raspberry and copy two python files to the home directory of this user.
In my case the line needs to be changed to
```
python /home/andreas/absolute_mouse_test.py &
```

Your home directory should contain these two files:<br>
[absolute_mouse_test.py](absolute_mouse_test.py)<br>
[mouse_move_absolute.py](mouse_move_absolute.py)<br>

So again, in my case:
```
/home/andreas/absolute_mouse_test.py
/home/andreas/mouse_move_absolute.py
```

Now when you reboot the Raspberry Pi Zero it should create a USB Mouse that works in absolute mouse mode.
At the end of the script myusbmouse we start a small script that moves the mouse to certain coordinates.
You can adjust the test, but it is made to see if the cursor moves to the edges of the 2 screens.
If there is a 3rd screen connected/configured somewhere or the two screens are shifted in the y-axis to each other this should be noticed by observing the cursor.
