#!/usr/bin/env python

import sys
import os
import math


print("Use $KIFOOTPRINTGENERATOR env variable to set the path to the kicad-footprint-generator repo.")

# ensure that the kicad-footprint-generator directory is available
sys.path.append(os.environ.get('KIFOOTPRINTGENERATOR'))  # enable package import from parent directory
#sys.path.append("D:\hardware\KiCAD\kicad-footprint-generator")  # enable package import from parent directory
#sys.path.append(os.path.join(sys.path[0],"..","..","kicad_mod")) # load kicad_mod path
#sys.path.append(os.path.join(sys.path[0],"..","..")) # load kicad_mod path
#sys.path.append(os.path.join(sys.path[0],"..","tools")) # load kicad_mod path

from KicadModTree import *

footprint_name = "code_wheel"

# init kicad footprint
kicad_mod = Footprint(footprint_name)
kicad_mod.setDescription("Code wheel for AEDR-8600")
#kicad_mod.setTags("example")

# set general values
kicad_mod.append(Text(type='reference', text='REF**', at=[0, 1], layer='F.SilkS'))
kicad_mod.append(Text(type='value', text=footprint_name, at=[0, -1], layer='F.Fab'))

# create silkscreen
#kicad_mod.append(RectLine(start=[-2, -2], end=[5, 2], layer='F.SilkS'))

# create courtyard
#kicad_mod.append(RectLine(start=[-2.25, -2.25], end=[5.25, 2.25], layer='F.CrtYd'))

def mm_to_inch(mm):
    return mm / 25.4

radius = 29.25
diameter = radius * 2 ## mm
lines_per_inch = 300  # 
line_count = math.floor(math.pi * mm_to_inch(diameter) * lines_per_inch)
pad_width = diameter * math.pi / line_count / 2
pad_size = [pad_width, 3.3]

print("Line count: " + str(line_count))
print("Pad width: " + str(pad_width))

for i in range(0, line_count):
    angle = (i / line_count) * 2 * math.pi
    pos = [radius * math.sin(angle), radius * math.cos(angle)]
    pad = Pad(number=i,
              type=Pad.TYPE_SMT,
              shape=Pad.SHAPE_TRAPEZE,
              at=pos,
              size=pad_size,
              rotation=(angle * 180.0 / math.pi),
              layers=["F.Cu"])
    kicad_mod.append(pad)

# output kicad model
file_handler = KicadFileHandler(kicad_mod)
file_handler.writeFile('code_wheel.kicad_mod')
