from sauron.main import *
from nose.tools import eq_, ok_

def test_intern():
    eq_(pop("x","y"), True)

