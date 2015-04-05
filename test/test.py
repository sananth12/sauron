from sys import version_info
from time import sleep
import argparse
from sauron.main import *
from nose.tools import eq_, ok_
if version_info.major is 2:
    import pynotify
    notifyModule = "pynotify"
    if version_info.major is 3:
        try:
            from gi.Repository import Notify
            notifyModule = "Notify"
        except ImportError:
            import notify2
            notifyModule = "notify2"
    
def test_intern():
    eq_(pop("x","y",""), True)

