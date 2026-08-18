# CobraPad

CobraPad is a small custom macro pad / keyboard project: a compact PCB, accompanying KiCad libraries, mechanical CAD assets, and firmware sources for a small, hobbyist input device.

Built for tinkering, iterating, and easy reproduction — this repo contains everything you need to inspect, build, or adapt the design for your own use.

**Highlights**
- Custom PCB layout and schematic (KiCad project in `PCB/CobraPad`)
- KiCad component and footprint helpers in `kicad-libs`
- Mechanical CAD and assembly assets in `CAD`
- Firmware sources in `Firmware`
- Production-ready exports and manufacturing notes in `production`

**Repository layout**
- `PCB/CobraPad` — KiCad project files: board, schematic, and project configuration. Open `CobraPad.kicad_pro` in KiCad to view the full project.
- `kicad-libs` — symbol and footprint libraries used by the project.
- `Firmware` — microcontroller code and build scripts. See that folder for specific build/flash instructions.
- `CAD` — mechanical models, mounting designs, and any STEP/STEP-derived files for the case or plate.
- `assets` — images, diagrams, and reference files used in documentation or manufacturing.
- `production` — manufacturing outputs, gerbers, pick-and-place, and notes intended for the fabricator.

Getting started
1. Inspect the PCB and schematic
	- Open the KiCad project at `PCB/CobraPad/CobraPad.kicad_pro`.
	- Check `sym-lib-table` and `fp-lib-table` if parts are missing; `kicad-libs` contains project-specific symbols and footprints.

2. Review mechanical assets
	- CAD files live in `CAD/`. Use your preferred viewer or CAD tool to preview STEP/3D models.

3. Build and flash firmware
	- Enter the `Firmware/` directory and follow the instructions there. Common workflows include PlatformIO or the microcontroller's recommended SDK and flashing tool.
	- If `Firmware/README.md` is present, start there — it contains device-specific build steps.

4. Generate production outputs
	- Gerbers, drill files, and pick-and-place CSVs should be placed in `production/` when preparing boards for fabrication.

Contributing
- Found an issue or improvement? Open an issue and describe your steps to reproduce.
- Want to contribute a fix or feature? Send a pull request with a concise description and, where applicable, updated fabrication outputs.
- Keep schematic changes and footprint edits limited to `kicad-libs` and the `PCB/CobraPad` project to avoid breaking references.

Notes for maintainers
- Keep the KiCad library versions consistent when updating symbols/footprints.
- When updating firmware, tag the commit and include the firmware version in `production/` exports.

License
This repository does not include an explicit license file. If you intend to share or publish, add a `LICENSE` file (MIT/Apache/other) and reference it here.

Contact / Feedback
- Open an issue or PR for specific changes.
- If you'd like, tell me what tone or sections you'd prefer and I can adjust the README further.

---
_Small, focused, and intentionally editable — set up for quick iteration and clear handoffs._
