import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(0) == 1
    assert utils.fact(4) == 24
    assert utils.fact(-1) == None
    pass

def test_roots():
    # À compléter...
    assert utils.roots(1,2,3) == ()
    assert utils.roots(1,2,1) == (-1/2) 
    assert utils.roots(1,3,1) == ((-3+5**1/2)/2,(-3-5**1/2)/2)
    pass

def test_integrate():
    # À compléter...
    assert utils. integrate( x**2 ,1,2) == 10/3
    assert utils.integrate(x,5,1) == None
    pass
