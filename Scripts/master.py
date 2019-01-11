#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:52:11 2019

@author: karl-stephan.baczkowski
"""

import os, sys

species = sys.argv[1]

# Création de la base de données si nécessaire
if not os.path.isdir("../DSW/Outputs/"+species):
    os.system("./Scripts/CreateDB.sh "+species)

import arborescence
import updateCSV


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



# Enrichir la Database
os.system("./enrichDB.sh "+species)