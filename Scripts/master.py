#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:52:11 2019

@author: karl-stephan.baczkowski
"""

import os, sys
import arborescence
arborescence.main()

os.chdir("DSW/Scripts")

import updateCSV
updateCSV.main()

os.chdir("../DSW/Out")