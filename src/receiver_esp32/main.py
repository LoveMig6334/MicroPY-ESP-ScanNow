import esp32
import espnow
import machine
import network
from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd
from utime import sleep_ms

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

esp = espnow.ESPNow()
esp.active(True)

# Default LED state to ON
BUTTON_PIN = Pin(13, Pin.IN)
LED_PIN = Pin(25, Pin.OUT)
LED_PIN.value(1)

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(22), scl=Pin(23), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


def button_release() -> bool:
    while True:
        v_1 = BUTTON_PIN.value()
        sleep_ms(200)
        v_2 = BUTTON_PIN.value()

        if (v_1 - v_2) != 0:
            return True


def first_screen_boot() -> None:
    lcd.putstr("LED is ON")
    sleep_ms(2000)
    lcd.clear()
    lcd.putstr("System Ready!")
    sleep_ms(2000)
    lcd.clear()

    for i in range(5):
        lcd.putstr("." * (i + 1))
        sleep_ms(500)
        lcd.clear()


def turn_on_off_button() -> None:
    if button_release() is True:
        LED_PIN.value(not LED_PIN.value())
        lcd.clear()

        # If LED turned ON
        if LED_PIN.value() == 1:
            pass
        # If LED turned OFF -> go to deep sleep
        else:
            lcd.putstr("LED OFF -> Sleep")
            sleep_ms(1000)

            # Configure pin 13 as wake-up source on rising edge (HIGH)
            esp32.wake_on_ext0(pin=Pin(13), level=esp32.WAKEUP_ANY_HIGH)

            # Go to deep sleep
            machine.deepsleep()


pushed_str = False


def check_name(result: tuple) -> None:
    global pushed_str

    if len(result) == 2:
        msg = result[1].decode("utf-8") if isinstance(result[1], bytes) else result[1]
    else:
        print("tuple length don't match")
        return

    for mac, info in esp.peers_table.items():
        rssi = info[0]
        print("RSSI:", rssi)

        if rssi > -88:
            print(f"Received message from: {msg} >>> in range")

            LED_PIN.value(not LED_PIN.value())
            sleep_ms(100)
            LED_PIN.value(not LED_PIN.value())

            if not pushed_str:
                lcd.putstr(str(msg))
                pushed_str = True
        else:
            print(f"Received message from: {msg} >>> out of range")
            lcd.clear()
            pushed_str = False


def main_loop() -> None:
    first_screen_boot()
    print("Receiver is listening for incoming messages...")

    is_running = True
    while is_running:
        if BUTTON_PIN.value() == 1:
            turn_on_off_button()

        result = esp.recv()
        if result:
            check_name(result)
        else:
            continue

        sleep_ms(10)


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("exit...")
