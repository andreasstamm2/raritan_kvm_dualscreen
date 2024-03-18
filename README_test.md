The following test set-up can be used to check if your target PC is set up to be controlled with the KVM switch.
We use a Raspberry Pi to simulate an absolute mouse.
In a small script we position the cursor at different points on the screen.
If this works we can see that the PC can be controlled and that the cursor positions should align.

We need a Raspberry Pi Zero W (the old one):<br>
[Raspberry Pi Zero W (Amazon.com)](https://www.amazon.com/dp/B06XFZC3BX)
I would also suggest to use a housing which makes it more comfortable (but this is not needed at all):
[Raspberry Pi Zero W Housing (Amazon.com)](https://www.amazon.com/dp/B075FLGWJL)

sudo nano /etc/rc.local
/etc/rc.local
...
/usr/bin/isticktoit_usb # libcomposite configuration
exit
