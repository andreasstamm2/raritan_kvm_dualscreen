# raritan_kvm_dualscreen

This project should explain what needs to be done to connect to a dual-screen PC with two Raritan KVM switches, specifically two Raritan DKX4-101.
The idea is to control the devices from a SW provided by Raritan which is called AKC-Client.
In order to control the PC the absolute mouse mode should be used.
The project is build up by three parts:

1. Setup
2. Absolute mouse mode
3. Prerequisits
4. Tests
5. Application

<b>The setup:</b><br>
<img src="https://github.com/andreasstamm2/raritan_kvm_dualscreen/assets/162843177/406541bc-31f9-4823-be2d-5cc45df4fe85" width="396" height="300">

<b>Absolute mouse mode:</b><br>
In order to control the PC the KVM is connected to the PC via a USB cable as shown in the section "Setup".
The KVM introduces two devices on the PC:
- a mouse
- a keyboard

For the mouse two distinct modes can be used:
- relative mode
- absolute mode

Relative mode:
In this mode the KVM sends data to the PC which are interpreted as differential movement (+/-x,+/-y).
This limits the remote setup or makes synchronisation necessary.
In this mode the KVM cannot move the mouse to a specific position, so on the remote side the remote mouse cursor and the cursor of the target machine needs to be synched before operation.
As soon as the mouse at the target system is moved locally the two cursors are out of sync and need to be synced again.

Absolute mode:
In absolute mode the KVM sends coordinates which relate to a virtual desktop which is build up of all screens on the target machine.
During introduction of the mouse the KVM sets a maximum value for x/y, e.g. 32768/32768.
If the system is a PC with a single screen with 1280x1024 resolution, if the KVM sends 32768/1 will position the cursor at pixel 1280/1.
If the system is a PC with two screens both with 1280x1024 resolution, if the KVM sends 32768/1 will position the cursor at pixel 1280/1 of the 2nd screen.
If the KVM sends 16384/1 will position the cursor at pixel 1280/1 of the 1st screen.
So it's necessary that the KVM knows the screen setup to understand that it is operating on a virtual desktop.

<b>Prerequisits:</b><br>
In order for the KVM to be able to give you the possibility to operate the target PC on the Remote-PC the Target-PC needs to give you the possibility to connect the two video output of the target-PCs to the KVM.
If the video outputs are not HDMI (as is the DKX4-101) you will need a video-splitter and a video-converter. The descriptions about this is not part of this project.<br>
In order for the KVM to be able to steer the target PC, the KVM introduces a USB HID keyboard and two USB HID mice (1 mouse for relative mode and 1 mouse for absolute mode).
For the best user experience absolute mouse mode is needed.
In order for the KVM to operate in absolute mouse mode the PC needs to accept a 2nd (or 3rd) mouse that operates in parallel to the 1st local mouse.
Not all systems support this, sometimes the system is even configured in a way to restrict the use of only one mouse.
Usually from my experience as IT Admin, MS Windows systems nearly always support the 2nd mouse operation, older Linux systems sometimes do, sometimes don't.
The absolute mouse is even more tricky.
In Windows systems the absolute mouse mode is supported since 2019 with native drivers.
However, since 2021 the absolute mouse mode was confined to only work on the primary screen (because of a security update).
There are drivers from KVM manufacturers however to get back to the "old" way of working that let's you operate with absolute mouse mode on all screens:
- [Matrox KVM driver](https://video.matrox.com/en/apps/drivers/graphics/download?id=816)
- [Adder KVM driver](https://www.adder.com/en/resources/dual-monitor-driver-v10)

<b>Tests:</b><br>

[Information about a possible test-setup](README_test.md)



