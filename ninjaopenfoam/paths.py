import os

class Paths:
    averageEquatorialSpacing = 'averageEquatorialSpacing.txt'
    courantNumber = 'co.txt'
    defaultControlDict = os.path.join('src/controlDict.template')
    dx = 'dx.txt'
    fvSchemes = 'system/fvSchemes'
    maxw = 'maxw.txt'
    maxKE = 'maxKE.txt'
    mountainHeight = 'mountainHeight.txt'
    polyMesh = [os.path.join("constant/polyMesh", f) for f in ["points", "faces", "owner", "neighbour", "boundary"]]
    timestep = 'dt.txt'
