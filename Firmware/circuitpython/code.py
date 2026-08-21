# pyright: reportMissingImports=false

import time
import board
import busio
import digitalio
import displayio
import terminalio
import neopixel
from adafruit_displayio_ssd1306 import SSD1306
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# CobraPad actual hardware mapping derived from the KiCad schematic.
# Rows: D0, D1
# Cols: D2, D3, D6, D7
# OLED: D4 (SDA), D5 (SCL)
# Encoder: D8 (A), D9 (B), GND common
# LEDs: D10 data

ROW_PINS = (board.D0, board.D1)
COL_PINS = (board.D2, board.D3, board.D6, board.D7)
KEYMAP = (
    (Keycode.F13, Keycode.F14, Keycode.F15, Keycode.F16),
    (Keycode.F17, Keycode.F18, Keycode.F19, Keycode.F20),
)
ENCODER_FORWARD_KEY = Keycode.RIGHT_ARROW
ENCODER_REVERSE_KEY = Keycode.LEFT_ARROW

rows = []
for pin in ROW_PINS:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row.value = True
    rows.append(row)

cols = []
for pin in COL_PINS:
    col = digitalio.DigitalInOut(pin)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP
    cols.append(col)

keyboard = Keyboard()
pressed = [[False for _ in range(len(COL_PINS))] for _ in range(len(ROW_PINS))]

# Encoder configuration.
# The KC encoder uses D8/A and D9/B with the common pin tied to GND.
enc_a = digitalio.DigitalInOut(board.D8)
enc_b = digitalio.DigitalInOut(board.D9)
enc_a.direction = digitalio.Direction.INPUT
enc_b.direction = digitalio.Direction.INPUT
enc_a.pull = digitalio.Pull.UP
enc_b.pull = digitalio.Pull.UP
last_encoder_state = (enc_a.value << 1) | enc_b.value

# Neopixel LED strip configuration.
leds = neopixel.NeoPixel(board.D10, 8, brightness=0.18, auto_write=False)
leds.fill((0, 0, 0))
leds.show()

# SSD1306 OLED configuration.
displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display = SSD1306(displayio.I2CDisplay(i2c, device_address=0x3C), width=128, height=32)

main_group = displayio.Group()
label = terminalio.Label(
    terminalio.FONT,
    text="CobraPad\nready",
    color=0xFFFFFF,
    scale=1,
)
label.x = 4
label.y = 10
main_group.append(label)
display.show(main_group)

# Utility helpers

def set_leds_for_matrix():
    for row_index, row_states in enumerate(pressed):
        for col_index, is_pressed in enumerate(row_states):
            led_index = (row_index * len(COL_PINS)) + col_index
            if led_index >= len(leds):
                continue
            if is_pressed:
                leds[led_index] = (0, 255, 128)
            else:
                leds[led_index] = (0, 0, 0)
    leds.show()


def handle_encoder():
    global last_encoder_state
    current = (enc_a.value << 1) | enc_b.value
    if current == last_encoder_state:
        return

    prev = last_encoder_state
    if (prev, current) in ((0b00, 0b01), (0b01, 0b11), (0b11, 0b10), (0b10, 0b00)):
        label.text = "CobraPad\n+"
        keyboard.press(ENCODER_FORWARD_KEY)
        time.sleep(0.02)
        keyboard.release(ENCODER_FORWARD_KEY)
    elif (prev, current) in ((0b00, 0b10), (0b10, 0b11), (0b11, 0b01), (0b01, 0b00)):
        label.text = "CobraPad\n-"
        keyboard.press(ENCODER_REVERSE_KEY)
        time.sleep(0.02)
        keyboard.release(ENCODER_REVERSE_KEY)

    last_encoder_state = current


# Main firmware loop
while True:
    for row_index, row in enumerate(rows):
        row.value = False
        time.sleep(0.0005)
        for col_index, col in enumerate(cols):
            is_pressed = not col.value
            keycode = KEYMAP[row_index][col_index]
            if is_pressed and not pressed[row_index][col_index]:
                keyboard.press(keycode)
                pressed[row_index][col_index] = True
            elif not is_pressed and pressed[row_index][col_index]:
                keyboard.release(keycode)
                pressed[row_index][col_index] = False
        row.value = True

    set_leds_for_matrix()
    handle_encoder()
    time.sleep(0.01)
