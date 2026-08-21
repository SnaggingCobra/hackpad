# CobraPad

CobraPad is a compact USB macro pad built around a Seeed XIAO RP2040 and assembled from the KiCad design in this repository. The KiCad files in [PCB/CobraPad](PCB/CobraPad) are the authoritative source for the board, pin mapping, and hardware layout.

## Hardware summary

- MCU: Seeed XIAO RP2040
- Layout: 2-row by 4-column matrix with 1 diode per switch
- Input: 8 mechanical keys + rotary encoder with push switch
- Display: SSD1306 OLED over I2C
- Lighting: 8 LED SK6812MINI-E chain
- Power: 3.3V rail from the XIAO board, with common GND

## Verified board mapping

The mapping below was extracted from the actual schematic and board files and is used by the firmware in [Firmware/circuitpython/code.py](Firmware/circuitpython/code.py).

| Function | KiCad signal / board net | CircuitPython pin |
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
| LED data | PA6_A10_D10_MOSI | D10 |

## Repository layout

- [PCB/CobraPad](PCB/CobraPad) — KiCad schematic, board, project config, and design assets
- [kicad-libs](kicad-libs) — project-local symbol and footprint libraries
- [Firmware](Firmware) — CircuitPython firmware and instructions
- [CAD](CAD) — mechanical CAD and exported case files
- [Case](Case) — final case parts and exported STEP files
- [assets](assets) — board and schematic visual references
- [production](production) — fabrication outputs and release artifacts

## Firmware

The ready-to-flash firmware lives in [Firmware/circuitpython/code.py](Firmware/circuitpython/code.py). The companion documentation is in [Firmware/README.md](Firmware/README.md).

### Flashing workflow

1. Install CircuitPython for the Seeed XIAO RP2040.
2. Copy the contents of [Firmware/circuitpython](Firmware/circuitpython) to the CIRCUITPY drive.
3. Confirm the board enumerates as a USB keyboard.
4. Test the key matrix, OLED, encoder, and LED output.

## Mechanical files

The final case design and exports are present in [Case](Case):

- [Case/CobraPAD_CASE_FINAL.FCStd](Case/CobraPAD_CASE_FINAL.FCStd)
- [Case/CobraPAD_CASE_FINAL_top_cover.step](Case/CobraPAD_CASE_FINAL_top_cover.step)
- [Case/CobraPAD_CASE_Finalbottom_shell.step](Case/CobraPAD_CASE_Finalbottom_shell.step)

## Physical validation checklist

The following checks still require a real hardware test on the assembled board:

- Confirm all switch matrix rows/columns register correctly on the host
- Verify the rotary encoder increments and decrements in the expected direction
- Confirm the encoder button press works as a key or function trigger
- Verify the SSD1306 OLED powers on and displays the startup state
- Confirm the LED chain lights in the correct sequence and brightness
- Check USB enumeration and keyboard behavior across the target OS
- Inspect the final assembly for mechanical fit, screw clearance, and cable strain

## Notes

- The board files in [PCB/CobraPad](PCB/CobraPad) were used as the source of truth for this project.
- No PCB or case redesign was performed during this pass; the repository was finalized around the existing design.
- The firmware is intentionally constrained to the actual pin assignments in the schematic so it matches the hardware without assumptions.

## License

This project is released under the MIT license. See [LICENSE](LICENSE).
