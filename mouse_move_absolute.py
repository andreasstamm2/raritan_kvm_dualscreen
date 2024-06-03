import time
import struct

def write_report(report):
    with open('/dev/hidg0', 'wb+') as fd:
        fd.write(report)


def limit_coord(coord):
    return min(32767, max(0, coord))

def point(pixel_coordinates, desktop_width, desktop_height):
    # transform pixel-coordinates to absolute mouse values 
    x = limit_coord(int((pixel_coordinates[0]/desktop_width) * 32767))
    y = limit_coord(int((pixel_coordinates[1]/desktop_height) * 32767))

    # HID reports use little endian
    x1, x2 = (x & 0xFFFFFFFF).to_bytes(2, 'little')
    y1, y2 = (y & 0xFFFFFFFF).to_bytes(2, 'little')

    report = bytearray(6)
    report[0] = 0    
    report[1] = x1
    report[2] = x2
    report[3] = y1
    report[4] = y2
    report[5] = 0

    write_report(report)