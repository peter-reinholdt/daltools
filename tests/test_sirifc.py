import unittest
import os
import numpy as np
from util import full
from . import daltools
from daltools import sirifc

class TestSirIfc(unittest.TestCase):

    def tmpdir(self, name=""):
        n, _ = os.path.splitext(__file__)
        dir_ = n + ".d"
        return os.path.join(dir_, name)
        

    def setUp(self):
        self.maxDiff = None
        self.ifc = sirifc.sirifc(self.tmpdir('SIRIFC'))

    def test_wrong_file_header(self):
        with self.assertRaises(RuntimeError):
            wrong = sirifc.sirifc(name=self.tmpdir('AOONEINT'))

    def test_potnuc(self):
        self.assertAlmostEqual(self.ifc.potnuc, 31.249215315972)

    def test_emy(self):
        self.assertAlmostEqual(self.ifc.emy, -143.60291282551114)

    def test_eactive(self):
        self.assertAlmostEqual(self.ifc.eactive, 0.0)

    def test_emcscf(self):
        self.assertAlmostEqual(self.ifc.emcscf, -112.353697509539)

    def test_istate(self):
        self.assertEqual(self.ifc.istate, 1)

    def test_ispin(self):
        self.assertEqual(self.ifc.ispin, 1)

    def test_nactel(self):
        self.assertEqual(self.ifc.nactel, 0)

    def test_lsym(self):
        self.assertEqual(self.ifc.lsym, 1)

    def test_nisht(self):
        self.assertEqual(self.ifc.nisht, 8)

    def test_nasht(self):
        self.assertEqual(self.ifc.nasht, 0)

    def test_nocct(self):
        self.assertEqual(self.ifc.nocct, 8)

    def test_norbt(self):
        self.assertEqual(self.ifc.norbt, 12)

    def test_nbast(self):
        self.assertEqual(self.ifc.nbast, 12)

    def test_nsym(self):
        self.assertEqual(self.ifc.nsym, 1)

    def test_cmo(self):
        ref_cmo = [
        [-0.00052699, -0.99261439, 0.12383359, 0.18555802, 0.00057906, -0.03008591, 0.00000525, -0.00032083, -0.00001086, -0.20197798, 0.00462897, -0.10720540],
        [0.00737583, -0.03297262, -0.27793974, -0.57839124, -0.00189817, 0.09379878, -0.00002193, 0.00213570, 0.00006014, 1.26291782, -0.03157479, 0.72473780],
        [-0.00000006, 0.00000034, 0.00000174, 0.00001207, -0.00000021, 0.00001577, -0.61047733, 0.00000024, 0.82117352, -0.00007631, 0.00000107, -0.00000241],
        [-0.00001516, 0.00002433, 0.00014992, -0.00142334, 0.53199496, 0.00597361, -0.00000010, -0.18011818, 0.00000020, -0.01026909, -1.15947841, -0.03615204],
        [0.00636525, -0.00081783, -0.15880295, 0.22231084, -0.00480339, 0.44843744, 0.00001484, -0.00156991, -0.00002782, -0.49164118, -0.02356105, 1.14905324],
        [-0.99427109, -0.00011729, 0.21888547, -0.10086099, -0.00150002, 0.09267643, 0.00000036, 0.00014951, 0.00000066, 0.02177132, -0.00369526, 0.11807975],
        [-0.02609688, 0.00584164, -0.76504310, 0.43932688, 0.00767818, -0.49482810, -0.00000310, -0.00076894, -0.00000161, -0.11725264, 0.02605872, -0.88618237],
        [-0.00000004, -0.00000001, -0.00000050, 0.00000336, -0.00000016, 0.00001334, -0.67317247, -0.00000011, -0.77061491, 0.00003093, -0.00000010, -0.00001058],
        [-0.00000175, 0.00000508, 0.00003637, -0.00011893, 0.43867722, 0.00738524, 0.00000019, 0.87245053, -0.00000035, 0.00104585, 0.31891087, 0.00852617],
        [0.00572834, -0.00164157, 0.17319132, 0.17014988, 0.00631320, -0.67884912, -0.00002075, 0.00453149, 0.00000552, 0.19185230, -0.03015682, 0.93896261],
        [-0.00022781, 0.00650112, -0.03189527, -0.26702488, 0.29798906, -0.16111049, -0.00000255, -0.35516810, -0.00003335, -0.89167912, 0.84514752, 0.12270512],
        [-0.00026105, 0.00649966, -0.03167323, -0.26196797, -0.29964271, -0.16250671, -0.00000228, 0.35940112, -0.00003302, -0.89524480, -0.84083843, 0.06116855]
        ]
        
        np.testing.assert_allclose(self.ifc.cmo[0], ref_cmo, atol=1e-7)

    def test_pv(self):
        pv = self.ifc.pv
        self.assertTupleEqual(pv.shape, (0, 0))

    def test_fock(self):
        fock = self.ifc.fock.subblock[0]
        _ref = full.matrix.diag([-40.62325438, -22.25084656, -2.68385608, -1.60738397, -1.27752650, -1.08854783, -0.89243173, -0.70725144, 0.00000000, 0.00000000, 0.00000000, 0.00000000])
        print(fock)
        np.testing.assert_allclose(fock, _ref, atol=1e-8)

    def test_fc(self):
        fc = self.ifc.fc
        _ref = full.matrix.diag([
            -20.31162719, -11.12542328, -1.34192804, -0.80369198, -0.63876325, -0.54427391, -0.44621587, -0.35362572, 0.28583524, 0.62008686, 0.74574226, 0.92100240
            ]).pack()
        print(fc)
        np.testing.assert_allclose(fc.subblock[0], _ref, atol=1e-8)

    def test_fv(self):
        fv = self.ifc.fv
        _ref = full.triangular((12, 12))
        print(fv)
        np.testing.assert_allclose(fv.subblock[0], _ref, atol=1e-8)

    def test_str(self):
        print(self.ifc)
        self.assertEqual(str(self.ifc), """\
Nuclear Potential Energy:    31.249215
Electronic energy       :  -143.602913
Active energy           :     0.000000
MCSCF energy            :  -112.353698
State                   : 1
Spin                    : 1
Active electrons        : 0
Symmetry                : 1
NISHT                   : 8
NASHT                   : 0
NOCCT                   : 8
NORBT                   : 12
NBAST                   : 12
NCONF                   : 1
NWOPT                   : 32
NWOPH                   : 32
NCDETS                  : 1
NCMOT                   : 144
NNASHX                  : 0
NNASHY                  : 0
NNORBT                  : 78
N2ORBT                  : 144
NSYM                    : 1
MULD2H:
    1 2 3 4 5 6 7 8
    2 1 4 3 6 5 8 7
    3 4 1 2 7 8 5 6
    4 3 2 1 8 7 6 5
    5 6 7 8 1 2 3 4
    6 5 8 7 2 1 4 3
    7 8 5 6 3 4 1 2
    8 7 6 5 4 3 2 1
NRHF: 8 0 0 0 0 0 0 0
NFRO: 0 0 0 0 0 0 0 0
NISH: 8 0 0 0 0 0 0 0
NASH: 0 0 0 0 0 0 0 0
NORB: 12 0 0 0 0 0 0 0
NBAS: 12 0 0 0 0 0 0 0
NELMN1                  : 0
NELMX1                  : 0
NELMN3                  : 0
NELMX3                  : 0
MCTYPE                  : 0
NAS1: 0 0 0 0 0 0 0 0
NAS2: 0 0 0 0 0 0 0 0
NAS3: 0 0 0 0 0 0 0 0
CMO
Block 1

 (12, 12) 
              Column   1    Column   2    Column   3    Column   4    Column   5
       1     -0.00052699   -0.99261439    0.12383359    0.18555802    0.00057906
       2      0.00737583   -0.03297262   -0.27793974   -0.57839124   -0.00189817
       3     -0.00000006    0.00000034    0.00000174    0.00001207   -0.00000021
       4     -0.00001516    0.00002433    0.00014992   -0.00142334    0.53199496
       5      0.00636525   -0.00081783   -0.15880295    0.22231084   -0.00480339
       6     -0.99427109   -0.00011729    0.21888547   -0.10086099   -0.00150002
       7     -0.02609688    0.00584164   -0.76504310    0.43932688    0.00767818
       8     -0.00000004   -0.00000001   -0.00000050    0.00000336   -0.00000016
       9     -0.00000175    0.00000508    0.00003637   -0.00011893    0.43867722
      10      0.00572834   -0.00164157    0.17319132    0.17014988    0.00631320
      11     -0.00022781    0.00650112   -0.03189527   -0.26702488    0.29798906
      12     -0.00026105    0.00649966   -0.03167323   -0.26196797   -0.29964271

              Column   6    Column   7    Column   8    Column   9    Column  10
       1     -0.03008591    0.00000525   -0.00032083   -0.00001086   -0.20197798
       2      0.09379878   -0.00002193    0.00213570    0.00006014    1.26291782
       3      0.00001577   -0.61047733    0.00000024    0.82117352   -0.00007631
       4      0.00597361   -0.00000010   -0.18011818    0.00000020   -0.01026909
       5      0.44843744    0.00001484   -0.00156991   -0.00002782   -0.49164118
       6      0.09267643    0.00000036    0.00014951    0.00000066    0.02177132
       7     -0.49482810   -0.00000310   -0.00076894   -0.00000161   -0.11725264
       8      0.00001334   -0.67317247   -0.00000011   -0.77061491    0.00003093
       9      0.00738524    0.00000019    0.87245053   -0.00000035    0.00104585
      10     -0.67884912   -0.00002075    0.00453149    0.00000552    0.19185230
      11     -0.16111049   -0.00000255   -0.35516810   -0.00003335   -0.89167912
      12     -0.16250671   -0.00000228    0.35940112   -0.00003302   -0.89524480

              Column  11    Column  12
       1      0.00462897   -0.10720540
       2     -0.03157479    0.72473780
       3      0.00000107   -0.00000241
       4     -1.15947841   -0.03615204
       5     -0.02356105    1.14905324
       6     -0.00369526    0.11807975
       7      0.02605872   -0.88618237
       8     -0.00000010   -0.00001058
       9      0.31891087    0.00852617
      10     -0.03015682    0.93896261
      11      0.84514752    0.12270512
      12     -0.84083843    0.06116855
DV


FOCK
Block 1

 (12, 12) 
              Column   1    Column   2    Column   3    Column   4    Column   5
       1    -40.62325438    0.00000000   -0.00000000    0.00000000   -0.00000000
       2      0.00000000  -22.25084656   -0.00000000    0.00000000    0.00000000
       3     -0.00000000   -0.00000000   -2.68385608    0.00000000   -0.00000000
       4      0.00000000    0.00000000    0.00000000   -1.60738397   -0.00000000
       5     -0.00000000    0.00000000   -0.00000000   -0.00000000   -1.27752650

              Column   6    Column   7    Column   8    Column   9    Column  10
       6     -1.08854783    0.00000000   -0.00000000    0.00000000    0.00000000
       7      0.00000000   -0.89243173    0.00000000    0.00000000   -0.00000000
       8     -0.00000000    0.00000000   -0.70725144   -0.00000000   -0.00000000

              Column  11    Column  12
PV

 (0, 0) 

FC
Block 1

  -20.31162719
    0.00000000  -11.12542328
   -0.00000000   -0.00000000   -1.34192804
    0.00000000    0.00000000    0.00000000   -0.80369198
   -0.00000000    0.00000000   -0.00000000   -0.00000000   -0.63876325
    0.00000000    0.00000000   -0.00000000    0.00000000   -0.00000000   -0.54427391
    0.00000000    0.00000000    0.00000000    0.00000000   -0.00000000    0.00000000   -0.44621587
   -0.00000000    0.00000000   -0.00000000   -0.00000000   -0.00000000   -0.00000000    0.00000000   -0.35362572
   -0.00000000   -0.00000000   -0.00000000   -0.00000000   -0.00000000    0.00000000    0.00000000   -0.00000000    0.28583524
   -0.00000000   -0.00000000   -0.00000000    0.00000000   -0.00000000    0.00000000   -0.00000000   -0.00000000    0.00000000    0.62008686
   -0.00000000   -0.00000000   -0.00000000   -0.00000000   -0.00000000   -0.00000000    0.00000000   -0.00000000   -0.00000000   -0.00000000    0.74574226
    0.00000000    0.00000000   -0.00000000   -0.00000000    0.00000000    0.00000000   -0.00000000    0.00000000   -0.00000000    0.00000000    0.00000000    0.92100240
FV
Block 1

    0.00000000
    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000    0.00000000
"""
        )


if __name__ == "__main__":#pragma no cover
    unittest.main()

