# Create panelized PCB #
- install [kikit](https://github.com/yaqwsx/KiKit/blob/master/doc/installation.md)
- for KiCad 6 nightly: set PYTHONPATH: PYTHONPATH=/usr/lib/kicad-nightly/lib/python3/dist-packages/
- `kikit panelize --layout 'grid; rows: 2; cols: 3; space: 3mm' --tabs 'fixed; width: 3mm;' --cuts 'mousebites; drill: 0.4mm; spacing: 0.6mm; offset: -0.1mm; prolong: 0.25mm' --post 'millradius: 1.25mm; copperfill: true' encoder-magnet-as5304.kicad_pcb encoder-magnet-as5304_panel.kicad_pcb`
