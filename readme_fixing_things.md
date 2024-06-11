In case that the test results are not the way that you expect them to be you might need to change something on the PC that you want to connect to.

<b>Confinement of absolute mouse to 1st screen on Windows machines:</b>
<br>
In case that you are working with a Windows machine that is newer than a couple of years, the absolute mouse mode that the KVM test tool is working in is restricted to the first screen. 
In Windows systems the absolute mouse mode is supported with native drivers for a long time.
However, since 2021 the absolute mouse mode was confined to only work on the primary screen (because of a security update).
There are drivers from KVM manufacturers however to get back to the "old" way of working that let's you operate with absolute mouse mode on all screens:
- [Matrox KVM driver](https://video.matrox.com/en/apps/drivers/graphics/download?id=816)
- [Adder KVM driver](https://www.adder.com/en/resources/dual-monitor-driver-v10)
<br>



<b>No cursor movement:</b>
<br>
If you're not seeing any movement of the cursor it could be that you have a Linux PC that is configured to not accept any input from a 2nd mouse. 
On older Linux machines with X being the display manager one could have a very specific configuration of your input devices in /etc/X11/xorg.conf. 
If you connect a KVM (or the KVM test tool) to such a machine the machine might not recognize the mouse from the KVM as a valid input device.
If this is the case, make sure that you have this setting in your xorg.conf:
```
Section "ServerFlags"
  [...]
  Option "AutoEnableDevices" "true"
  Option "AutoAddDevices" "true"
EndSection
```
<br>

<b>Cursor movement with offset:</b>
<br>
If the cursor is moving, but there is an offset it could be that you are connecting to a Linux machine that uses a generic legacy mouse driver which does not support absolute mouse mode.
Even if the Linux Kernel supports absolute mouse mode, if this legacy driver is used the driver will try to translate absolute coordinates to relative coordinates. This will most likely lead to a shift in coordinates. The exact offset depends on where the mouse was positioned before you attached the KVM test device.```
If this is the case the same configuration as above will help.
Make sure that you have these two flags in the ServerFlags section of your xorg.conf:
```
Section "ServerFlags"
  [...]
  Option "AutoEnableDevices" "true"
  Option "AutoAddDevices" "true"
EndSection
```
