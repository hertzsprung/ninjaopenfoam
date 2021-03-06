from .paths import Paths

import os

class Case:
    def __init__(self, name, prefix='$builddir'):
        self.name = name
        self.root = os.path.join(prefix, name)

        self.advectionDict = self.path("system/advectionDict")
        self.asamGrid = self.path("asam.grid")
        self.averageCellCentreDistance = self.path("averageCellCentreDistance.txt")
        self.averageEquatorialSpacing = self.path(Paths.averageEquatorialSpacing)
        self.blockMeshDict = self.path("system/blockMeshDict")
        self.collapseDict = self.path("system/collapseDict")
        self.controlDict = self.path("system/controlDict")
        self.courantNumber = self.path(Paths.courantNumber)
        self.createPatchDict = self.path("system/createPatchDict")
        self.decomposeParDict = self.path("system/decomposeParDict")
        self.deformationalAdvectionDict = self.path("system/deformationalAdvectionDict")
        self.dx = self.path(Paths.dx)
        self.energy = self.path('energy.dat')
        self.environmentalProperties = self.path("constant/environmentalProperties")
        self.exnerInit = self.path("constant/Exner_init")
        self.extrudeMeshDict = self.path("system/extrudeMeshDict")
        self.fvSchemes = self.path(Paths.fvSchemes)
        self.fvSolution = self.path("system/fvSolution")
        self.ghostPolyMesh = [self.path(f) for f in Paths.ghostPolyMesh]
        self.gmtConf = self.path("gmt.conf")
        self.maxw = self.path(Paths.maxw)
        self.maxKE = self.path(Paths.maxKE)
        self.meshQualityDict = self.path("system/meshQualityDict")
        self.mountainDict = self.path("system/mountainDict")
        self.mountainHeight = self.path(Paths.mountainHeight)
        self.s3Uploaded = self.path("s3.uploaded")
        self.sampleDict = self.path("system/sampleDict")
        self.setGaussiansDict = self.path(Paths.setGaussiansDict)
        self.sponge = self.path("constant/muSponge")
        self.T_init = self.path("constant/T_init")
        self.Tf_init = self.path("constant/Tf_init")
        self.thermophysicalProperties = self.path("constant/thermophysicalProperties")
        self.thetaInit = self.path("constant/theta_init")
        self.thetafInit = self.path("constant/thetaf_init")
        self.timestep = self.path(Paths.timestep)
        self.tracerFieldDict = self.path("system/tracerFieldDict")
        self.velocityFieldDict = self.path("system/velocityFieldDict")

        self.polyMesh = [self.path(f) for f in Paths.polyMesh]
        self.systemFiles = [self.fvSchemes, self.fvSolution, self.controlDict]

    def path(self, path, *paths):
        return os.path.join(self.root, path, *paths)

    def __str__(self):
        return self.root

class CopyCase:
    def __init__(self, name, source, target, files=[], renamedFiles={}):
        self.name = name
        self.sourceCase = Case(name, prefix=source)
        self.targetCase = Case(name, prefix=target)
        self.files = files
        self.renamedFiles = renamedFiles

    def write(self, generator):
        g = generator

        g.copyAll(Paths.polyMesh, self.sourceCase, self.targetCase)

        for f in self.files:
            g.copy(self.sourceCase.path(f), self.targetCase.path(f))

        for sourceFile, targetFile in self.renamedFiles.items():
            g.copy(
                    self.sourceCase.path(sourceFile),
                    self.targetCase.path(targetFile)
            )

    def __str__(self):
        return self.name
