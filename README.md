# CobraPad

A compact, hobbyist macro pad / keyboard project: PCB, KiCad libraries, mechanical CAD, and firmware.

This repository contains the sources and assets needed to inspect, build, and adapt the CobraPad design for personal use or small-batch production.

**Key features**
- Compact KiCad board and schematic optimized for hobby assembly
- Project-specific symbol & footprint libraries
- CAD models for the case and mounting hardware
- Firmware source and flashing/build scripts
- Production exports and manufacturing notes

**Repository layout**
- [PCB/CobraPad](PCB/CobraPad) — KiCad project files (board, schematic, project config). Open [PCB/CobraPad/CobraPad.kicad_pro](PCB/CobraPad/CobraPad.kicad_pro) in KiCad.
- [kicad-libs](kicad-libs) — project symbol and footprint libraries used by the design.
- [Firmware](Firmware) — firmware source, build scripts, and device-specific instructions (see `Firmware/README.md` if present).
- [CAD](CAD) — mechanical models, STEP/3D exports, and assembly assets.
- [assets](assets) — images, diagrams, and documentation assets.
- [production](production) — gerbers, drill files, pick-and-place CSVs, and fabrication notes.

**Quick start**
1. Inspect the PCB and schematic
   - Open the project: [PCB/CobraPad/CobraPad.kicad_pro](PCB/CobraPad/CobraPad.kicad_pro).
   - If parts are missing in KiCad, check `sym-lib-table` and `fp-lib-table` and the [kicad-libs](kicad-libs) folder.

2. Review mechanical assets
   - Preview CAD models in [CAD](CAD) with your preferred viewer (STEP/STEP-derived files available).

3. Build and flash firmware
   - Change into the `Firmware` directory and follow its instructions.
   - Common workflows: PlatformIO, chip vendor SDKs, or `make`/`cmake` depending on the board.

4. Prepare production outputs
   - Place final gerbers, drill files, and pick-and-place CSVs in [production](production) for fabrication.

**Assembly & First Boot**

What you'll need
- PCB and case files from this repo
- Mechanical parts: switches, keycaps, standoffs, screws
- Electronics: microcontroller/module, USB connector, diodes (if used), headers
- Tools: soldering iron, solder, flux, tweezers, multimeter, USB cable, (optional) programmer/debugger

Assembly steps
1. Inspect the PCB for visible damage or manufacturing defects. Confirm footprints and mounting holes match your hardware.
2. Solder SMD parts first (diodes, resistors, LEDs, connectors) while keeping the board flat. Use flux and tweezers for small parts.
3. Solder through-hole components and switches next. Place each switch, tack two opposite pins, then solder the remaining pins.
4. Fit any connectors or microcontroller modules. If your MCU is a socketed module, insert it after the socket is soldered.
5. Mount the PCB into the case using standoffs and screws from the [CAD](CAD) outputs. Verify no mechanical stress on solder joints.
6. Install keycaps and perform a visual inspection for bridges or cold joints.

Initial electrical checks
- With power disconnected, use a multimeter continuity check to confirm there are no shorts between VBUS/GND.
- After a quick visual check, connect USB and confirm the board draws reasonable current (no smoke!).

Flashing firmware (examples)
Note: this repo's `Firmware` folder is currently empty — adapt the commands below to your firmware toolchain.

PlatformIO (if project uses it):
```bash
cd Firmware
pio run -e <env> -t upload
```

Generic DFU (for DFU-capable MCUs):
```bash
dfu-util -a 0 -D firmware.bin
```

esptool (ESP chips):
```bash
esptool.py --chip esp32 write_flash -z 0x1000 firmware.bin
```

stm32 (st-flash example):
```bash
st-flash write firmware.bin 0x8000000
```

First boot checklist
1. Connect the board by USB. Confirm the OS enumerates a USB device (check `dmesg` on Linux or Device Manager on Windows).
2. Use a keyboard tester (online) or `evtest`/`hid-recorder` on Linux to verify key matrix and layout.
3. If keys are missing or miswired, check solder joints, diode orientation, and matrix wiring.

Troubleshooting tips
- No USB device: check connector orientation, cable, and power rails.
- Only some keys register: inspect diodes and row/column traces for shorts or opens.
- Firmware fails to upload: ensure correct boot mode or programmer connection; double-check target flash address.

If you'd like, provide a specific firmware project or target MCU and I will add exact build/upload commands to this tutorial.

**Contributing**
- Found an issue? Open an issue with reproduction steps and expected behavior.
- Want to contribute? Fork, create a topic branch, and submit a pull request with a clear description and any updated fabrication files.
- Keep library updates scoped to [kicad-libs](kicad-libs) and changes to [PCB/CobraPad](PCB/CobraPad) to avoid breaking references.

**Maintainers / release notes**
- When updating firmware, tag releases and include the firmware version and change notes in [production](production).
- Keep KiCad library versions consistent across commits; include library version notes when changing symbols/footprints.

**License**
This repository currently has no `LICENSE` file. Add an appropriate license (for example, MIT or Apache-2.0) if you intend to publish or share.

**Contact / feedback**
- Prefer issues and pull requests for technical changes.
- For help shaping the README tone or adding examples, tell me your preferred style (concise technical / tutorial / marketing), and I will update the file accordingly.

---
_Designed for quick iteration: inspect, build, adapt._