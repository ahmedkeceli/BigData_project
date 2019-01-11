#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:52:11 2019

@author: karl-stephan.baczkowski
"""

import os, sys

species = sys.argv[1]
print("#############################################")
print("#             Projet BigData                #")
print("#############################################\n\n")

# Création de la base de données si nécessaire
if not os.path.isdir("../DSW/Outputs/"+species):
    os.system("./Scripts/CreateDB.sh "+species)
    print("    > Création de la base de données "+species)

print("    > Création de l'arborescence et déplacement des données")
import arborescence
print("    > Parsing des fichiers input")
import updateCSV


list_sql = list()

if os.path.isfile("../DSW/Outputs/"+species+"/gene.csv"):
    print("    > Ajout de nouveaux gènes")
    import geneCSVtoSQL
    list_sql.append("geneSQL.sql")
    
if os.path.isfile("../DSW/Outputs/"+species+"/contig.csv"):
    print("    > Ajout de nouveaux contigs")
    import contigCSVtoSQL
    list_sql.append("contigSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/gene_seq.csv"):
    print("    > Ajout de nouvelles séquences de gènes")
    import gene_seqCSVtoSQL
    list_sql.append("gene_seqSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/protein_seq.csv"):
    print("    > Ajout de nouvelles séquences de protéines")
    import proteinCSVtoSQL
    list_sql.append("proteinSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/transcript_seq.csv"): 
    print("    > Ajout de nouvelles séquences de transcripts")
    import transcriptCSVtoSQL
    list_sql.append("transcriptSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/pfam.csv"):
    print("    > Ajout de nouveaux domaines pfam")
    import pfamCSVtoSQL
    list_sql.append("pfamSQL.sql")

if os.path.isfile("../DSW/Outputs/"+species+"/pfam2gene.csv"):
    print("    > Ajout de nouvelles associations pfam <-> gènes")
    import p2gCSVtoSQL
    list_sql.append("p2gSQL.sql")

# Enrichir la Database
    print("    > Enrichissement de la base de données "+species)
for sql_file in list_sql:
    print("         - Traitement du fichier "+sql_file)
    os.system("./enrichDB.sh "+species+" "+sql_file)
#os.system("rm ../DSW/Outputs/"+species+"/*.csv")
#os.system("rm ../DSW/Outputs/"+species+"/*.sql")
