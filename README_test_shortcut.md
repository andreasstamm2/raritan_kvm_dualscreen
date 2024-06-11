Download the [usb_test_tool_sdcard_image.zip](usb_test_tool_sdcard_image.zip) and unzip it on your hard disc.<br>
It's a 16GB SD card image.
Make sure that you use a micro SD card that holds at least 16GB.<br>
You can use e.g. [Win32Diskimager](https://sourceforge.net/projects/win32diskimager/) if you're on Windows.<br>
This is the sequence:
1. Just select the unpacked disk image with the directory button on the top right.
2. Then select the drive of the USB stick on the top right.
3. Then press "Write" on the bottom.<br>

It will take some time to write the SD card.
If DiskImager successfully wrote the image to the SD card you can unmount the SD card and put it in your Raspberry Pi.<br>
If you disconnect the USB cable and connect it again to your PC, it should boot and do some tests.

Here you can get an overview of what should happen and what different results tell you:<br>
[Analysis of test results](readme_test_analysis.md)
