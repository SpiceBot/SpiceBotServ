# coding=utf8
from __future__ import unicode_literals, absolute_import, division, print_function

# import time
import inspect


"""
Dynamic Classes
"""


def class_create(classname):
    compiletext = """
        def __init__(self):
            self.default = str(self.__class__.__name__)
        def __repr__(self):
            return repr(self.default)
        def __str__(self):
            return str(self.default)
        def __iter__(self):
            return str(self.default)
        def __unicode__(self):
            return str(u+self.default)
        def lower(self):
            return str(self.default).lower()
        pass
        """
    exec(compile("class class_" + str(classname) + ": " + compiletext, "", "exec"))
    newclass = eval('class_'+classname+"()")
    return newclass


"""
Other
"""


def lineno():
    """Returns the current line number in our program."""
    linenum = inspect.currentframe().f_back.f_lineno
    frameinfo = inspect.getframeinfo(inspect.currentframe())
    filename = frameinfo.filename
    return str("File:  " + str(filename) + "    Line:  " + str(linenum))
