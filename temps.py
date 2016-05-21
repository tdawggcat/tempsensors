#!/usr/bin/python

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#device_folder = glob.glob(base_dir + '28*')[0]
DeviceFile0 = '/sys/bus/w1/devices/28-800000081184/w1_slave'
DeviceFile1 = '/sys/bus/w1/devices/28-00152c26fdee/w1_slave'
DeviceFile2 = '/sys/bus/w1/devices/28-0315a4acc8ff/w1_slave'
DeviceFile3 = '/sys/bus/w1/devices/28-00152335c4ee/w1_slave'


def read_temp(DeviceFile):
    f = open(DeviceFile, 'r')
    lines = f.readlines()
    f.close()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
	
print(read_temp(DeviceFile0))
time.sleep(1)
print(read_temp(DeviceFile1))
time.sleep(1)
print(read_temp(DeviceFile2))
time.sleep(1)
print(read_temp(DeviceFile3))
