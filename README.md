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

<b>The setup:</b>

<b>Absolute mouse mode:</b>
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

Tests:
[Information about a possible test-setup](README_test.md)



