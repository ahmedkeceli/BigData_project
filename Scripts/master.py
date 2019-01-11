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

list_sql = list()

if os.path.isfile("../DSW/Outputs/"+species+"/gene.csv"):
    import geneCSVtoSQL
    list_sql.append("geneSQL.sql")
    
if os.path.isfile("../DSW/Outputs/"+species+"/contig.csv"):
    import contigCSVtoSQL
    list_sql.append("contigSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/gene_seq.csv"):
    import gene_seqCSVtoSQL
    list_sql.append("gene_seqSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/protein_seq.csv"):
    import proteinCSVtoSQL
    list_sql.append("proteinSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/transcript_seq.csv"): 
    import transcriptCSVtoSQL
    list_sql.append("transcriptSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/pfam.csv"):
    import pfamCSVtoSQL
    list_sql.append("pfamSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/pfam2gene.csv"):
    import p2gCSVtoSQL
    list_sql.append("p2gSQL.sql")

# Enrichir la Database
for sql_file in list_sql:
    os.system("./enrichDB.sh "+species+" "+sql_file)
os.system("rm ../DSW/Outputs/"+species+"/*.csv")
os.system("rm ../DSW/Outputs/"+species+"/*.sql")
