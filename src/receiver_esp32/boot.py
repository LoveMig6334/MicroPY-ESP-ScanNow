# This file is executed on every boot (including wake-boot from deepsleep)

import gc
import sys

import esp
import machine
import uos

gc.collect()


machine.freq(240000000)
print("Platform:", sys.platform)

# Print ESP32 chip information
chip_id = machine.unique_id()
print("Chip ID:", chip_id)

# Print ESP32 flash size
flash_size = esp.flash_size()
print(f"Flash Size: {(flash_size / 1000000):.2f} MB")

# Print ESP32 frequency
freq = machine.freq()
print(f"Frequency: {(freq / 1000000):.2f} MH")

# Print ESP32 file system information
fs_info = uos.statvfs("/")
print("File System Info:", fs_info)

print()
