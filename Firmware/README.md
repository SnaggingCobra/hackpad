# Firmware

This repository uses CircuitPython for the Seeed XIAO RP2040 variant used on the CobraPad PCB.

The board files in [PCB/CobraPad/CobraPad.kicad_sch](../PCB/CobraPad/CobraPad.kicad_sch) and [PCB/CobraPad/CobraPad.kicad_pcb](../PCB/CobraPad/CobraPad.kicad_pcb) are the source of truth. The firmware below is intentionally aligned to the actual KiCad net names and pin usage.

## Hardware mapping used by the firmware

| Function | KiCad / XIAO signal | CircuitPython pin |
| --- | --- | --- |
| Row 1 | PA02_A0_D0 | D0 |
| Row 2 | PA4_A1_D1 | D1 |
| Col 1 | PA10_A2_D2 | D2 |
| Col 2 | PA11_A3_D3 | D3 |
| Col 3 | PB08_A6_D6_TX | D6 |
| Col 4 | PB09_A7_D7_RX | D7 |
| OLED SDA | PA8_A4_D4_SDA | D4 |
| OLED SCL | PA9_A5_D5_SCL | D5 |
| Encoder A | PA7_A8_D8_SCK | D8 |
| Encoder B | PA5_A9_D9_MISO | D9 |
| LED data in | PA6_A10_D10_MOSI | D10 |
| Board GND | GND | GND |
| Board 3.3V | 3V3 | 3V3 |

### Notes
- The matrix is a 2x4 arrangement: 2 rows, 4 columns.
- The rotary encoder is connected to D8 and D9 with its common pin tied to GND.
- The LED chain is driven from D10 and uses 8 SK6812MINI-E devices in series.
- D7 is not shared with the encoder; the schematic confirms no conflict.

## Files

- [circuitpython/code.py](circuitpython/code.py) — main firmware for CircuitPython.

## Flashing

1. Install CircuitPython for the Seeed XIAO RP2040.
2. Copy the contents of the `circuitpython/` folder to the CIRCUITPY drive.
3. Ensure the required CircuitPython libraries are installed:
   - `adafruit_hid`
   - `adafruit_displayio_ssd1306`
   - `adafruit_neopixel`
   - `neopixel`
4. Reboot the board.

## Quick validation

- Confirm the OLED powers up and displays the startup banner.
- Press each key in the 2x4 matrix and verify the host sees the mapped actions.
- Turn the encoder and verify the host receives the expected increment/decrement behavior.
- Confirm the LED strip responds to key presses and boot animation states.

## Editing the key map

Open [circuitpython/code.py](circuitpython/code.py) and adjust the `KEYMAP` constant to match your intended macro assignments.
