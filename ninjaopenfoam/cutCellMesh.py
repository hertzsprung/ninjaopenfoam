from .case import Case

import os

class CutCellMesh:
    def __init__(
            self,
            name,
            asamGridFile,
            createPatchDict,
            extrudeMeshDict=os.path.join('src/cutCellMesh/extrudeMeshDict'),
            meshQualityDict=os.path.join('src/mesh/meshQualityDict'),
            patchSets=os.path.join('src/cutCellMesh/patchSets'),
            fvSchemes=os.path.join('src/fvSchemes'),
            fvSolution=os.path.join('src/fvSolution'),
            controlDict=os.path.join('src/controlDict')):
        self.case = Case(name)
        self.asamCase = Case(name + '-asam')
        self.asamGridFile = asamGridFile
        self.createPatchDict = createPatchDict
        self.extrudeMeshDict = extrudeMeshDict
        self.meshQualityDict = meshQualityDict
        self.patchSets = patchSets
        self.fvSchemes = fvSchemes
        self.fvSolution = fvSolution
        self.controlDict = controlDict

    def write(self, generator):
        g = generator
        case = self.case
        asamCase = self.asamCase

        g.w.build(
                outputs=case.polyMesh,
                rule='cutCellMesh',
                implicit=[
                    case.path('vertical_slice.obj'),
                    case.controlDict,
                    case.extrudeMeshDict,
                    case.meshQualityDict,
                    case.createPatchDict,
                    self.patchSets
                ],
                variables={'case': case, 'patchSets': self.patchSets}
        )
        g.w.newline()

        g.w.build(
                outputs=asamCase.path('vertical_slice.obj'),
                rule='cutCellPatch',
                inputs=[asamCase.asamGrid],
                variables={'case': asamCase}
        )
        g.w.newline()

        g.copy(asamCase.path('vertical_slice.obj'), case.path('vertical_slice.obj'))
        g.copy(self.asamGridFile, asamCase.asamGrid)
        g.copy(self.extrudeMeshDict, case.extrudeMeshDict)
        g.copy(self.meshQualityDict, case.meshQualityDict)
        g.copy(self.createPatchDict, case.createPatchDict)
        g.copy(self.fvSchemes, case.fvSchemes)
        g.copy(self.fvSolution, case.fvSolution)
        g.copy(self.controlDict, case.controlDict)

        g.s3uploadCase(case, case.polyMesh)

    def __str__(self):
        return self.case.name
