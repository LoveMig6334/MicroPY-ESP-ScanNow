# This file is executed on every boot (including wake-boot from deepsleep)

import gc

import machine

gc.collect()
machine.freq(80000000)
