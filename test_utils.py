import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(0) == 1
    assert utils.fact(4) == 24
    #assert utils.fact(-1) == None
    #est une fonction qui necessite un code test particulier voir lien suivant: https://docs.pytest.org/en/8.0.x/getting-started.html
    pass

def test_roots():
    # À compléter...
    assert utils.roots(1,2,3) == ()
    assert utils.roots(1,2,1) == (-1) 
    #assert utils.roots(1,3,1) == ((-3+5**1/2)/2,(-3-5**1/2)/2)
    pass

def test_integrate():
    # À compléter...
    result = utils.integrate('x ** 2 - 1', -1, 1)
    assert abs(result)<2 #car float !
    #pass
