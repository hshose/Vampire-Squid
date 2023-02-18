import numpy as np
from pcbnew import *

########################################################
# pcb outline
outerDiameter = 63.5 #mm
innerDiameter = 53.5 #mm

# magnet ring
magnetCount = 92 # has to be even
magnetCenterlineDiameter = 58.57 #mm
magnetDiameter = 1.5 #mm

filename = 'VSEncoderWheel.pcbnew'
########################################################


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def find_layer(board, layer_name):
    for i in range(128):
        if board.GetLayerName(i) == layer_name:
            return i
    return -1


def drawCircle(board, center, diameter, layer='Edge.Cuts', width=0.15):
    layerId = find_layer(board, layer)
    if(layerId == -1):
        print('Layer not found!')

    circle = PCB_SHAPE()
    circle.SetShape(S_CIRCLE)
    circle.SetCenter(wxPoint(FromMM(center[0]), FromMM(center[1])))
    circle.SetEnd(wxPoint(FromMM(center[0]+diameter/2.0), FromMM(center[1])))
    circle.SetLayer(layerId)
    circle.SetWidth(FromMM(width))
    board.Add(circle)


## verify input values
## The AS5304 has a pole pair distance of 4mm, therefore the diameter has to be:
## d = 4.0mm * number of pole pairs / π
polePairs = magnetCount/2
checkDiameter = 4.0 * polePairs / np.pi

if(magnetCount & 0x01):
    print('Err: the magnet count has to be even')
    exit(-1)

if(not isclose(checkDiameter, magnetCenterlineDiameter,5e-3)):
    print('Computed diameter: ' + str(checkDiameter))
    print('Err: please verify magnet count and magnet center line diameter!')
    exit(-2)
    

### start generating the board ###
board = NewBoard(filename)

center = (150.0, 100.0)

drawCircle(board, center, innerDiameter)
drawCircle(board, center, outerDiameter)

for i in range(0,magnetCount):
    magnetAngle = (2.0*np.pi)*(i/magnetCount)
    r = magnetCenterlineDiameter/2.0
    magnetCenter = (float(center[0] + r * np.cos(magnetAngle)), float(center[1] + r * np.sin(magnetAngle)))
    print(magnetCenter)
    drawCircle(board, magnetCenter, magnetDiameter)


board.Save(filename)

