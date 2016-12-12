# -*- coding: utf-8 -*-
"""
    Some functions to handle data intended to be plotted through 
    matplotlib
"""

__title__ = "filefunctions"
__author__ = "Juliano Fischer Naves"
__license__ = "Apache License 2.0"
#date: Dec., 11, 2016

def extract_lines(myfile):
    """Returns the lines of a space separated file as a list
    let the file be:

    a b c
    d e f
    g h i

    function will return
   [[a,b,c],[d,e,f],[g,h,i]]
    """
    return [line.split() for line in myfile]

def extract_columns(myfile):
    """Returns the columns of a space separated file as a list
    let the file be:

    a b c
    d e f
    g h i

    the function will return:
    [(a,d,g), (b,e,h), (c,f,i)]
    """
    lines = extract_lines(myfile)
    zipped = zip(*lines)
    return list(zipped)
