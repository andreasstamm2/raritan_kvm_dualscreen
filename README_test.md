The following test set-up can be used to check if your target PC is set up to be controlled with the KVM switch.
We use a Raspberry Pi to simulate an absolute mouse.
In a small script we position the cursor at different points on the screen.
If this works we can see that the PC can be controlled and that the cursor positions should align.

We need a Raspberry Pi Zero W (the old one):<br>
[Raspberry Pi Zero W (Amazon.com)](https://www.amazon.com/dp/B06XFZC3BX)<br>
I would also suggest to use a housing which makes it more comfortable (but this is not needed at all):<br>
[Raspberry Pi Zero W Housing (Amazon.com)](https://www.amazon.com/dp/B075FLGWJL)<br>
<br>

First of all you need the Linux operating system which you can get using the official Tool:

Then we need to add the following line to /boot/config.txt 
```
dtoverlay=dwc2
```

We are using the Config-Filesystem (ConfigFS) to create/simulate our USB HID device, the mouse.
For this we use the script in [myusbmouse](myusbmouse)
to create a USB HID device with absolute mouse mode.
This script should be copied to /usr/bin/
Then make is executable by running
```
sudo chmod +x /usr/bin/myusbmouse
```

Make sure that the script is put in the boot-up-sequence:
Edit /etc/rc.local as root and add the following  before the line ‘exit’.
```
sudo nano /etc/rc.local

...
/usr/bin/isticktoit_usb # libcomposite configuration
exit
```

Now when you reboot the Raspberry Pi Zero it should create a USB Mouse that works in absolute mouse mode.
At the end of the script myusbmouse we start a small script that moves the mouse to certain coordinates.
You can adjust the test, but it is made to see if the cursor moves to the edges of the 2 screens.
If there is a 3rd screen connected/configured somewhere or the two screens are shifted in the y-axis to each other this should be noticed by observing the cursor.
