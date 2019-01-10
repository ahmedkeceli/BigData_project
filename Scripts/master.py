#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:52:11 2019

@author: karl-stephan.baczkowski
"""

import os, sys
import arborescence
import updateCSV

species = sys.argv[1]
if os.path.isfile("../DSW/Outputs/"+species+"/contig.csv"):
    import contigCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/gene_seq.csv"):
    import gene_seqCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/gene.csv"):
    import geneCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/pfam2gene.csv"):
    import p2gCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/pfam.csv"):
    import pfamCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/protein_seq.csv"):
    import proteinCSVtoSQL

if os.path.isfile("../DSW/Outputs/"+species+"/transcript_seq.csv"): 
    import transcriptCSVtoSQL
print(os.getcwd())


