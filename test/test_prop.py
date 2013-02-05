import numpy as np
from daltools import prop, sirifc

def setup():
    global propfile, nbast
    propfile = 'test/data/AOPROPER'
    ifcfile = 'test/data/SIRIFC'
    nbast = sirifc.sirifc(ifcfile).nbast

def teardown():
    pass

def assert_(this, ref):
    print this, ref
    assert np.allclose(this, ref)

def test_xdiplen():
    x = prop.read(nbast, 'XDIPLEN', propfile)
    xref = [0, 0, 0, 0.62318216, 2.00000000, 0.00000000]
    assert_(x, xref)

def test_ydiplen():
    y = prop.read(nbast, 'YDIPLEN', propfile)
    yref = [-0.22490589, 0.42047202, 2.63189861, 0.00000000, 0.00000000, 0.96659568]
    assert_(y, yref)

def test_zdiplen():
    z = prop.read(nbast, 'ZDIPLEN', propfile)
    zref = [0, 0, 0, 0, 0, 0]
    assert_(z, zref)

