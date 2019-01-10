#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:56:53 2019

@author: karl-stephan.baczkowski
"""

import os
import sys
from contig import contigParser
from gene_seq import geneseqParser
from gene import geneParser
from protein_seq import proteinseqParser
from transcript_seq import transcriptseqParser
from pfam_p2g import pfamParser

#os.chdir("Documents/BigData/DSW/Scripts")

def main():
    # Lister les répertoirs Inputs
    list_species = os.listdir("../DSW/Inputs")
    
    for species in list_species:
        if species != ".DS_Store":
            
            # Lister les fichiers présents dans le répertorie species
            files = os.listdir("../DSW/Inputs/"+species)
            
            for f_name in files:
                if f_name != ".DS_Store":
                    f_type = f_name.split(".")[-1]
                    
                    # Si le fichier est un .fasta ou un .fa -> Il contient des séquences
                    if f_type == "fasta" or f_type == "fa":
                        # Ouverture du fichier fasta
                        try:
                            f = open("../Inputs/"+species+"/"+f_name, "r")
                        except IOError:
                            print("L'ouverture du fichier "+f_name+"  a échoué.")
                            sys.exit(1)
                        
                        header = f.readline().rstrip("\n")
                        # Cas 1 : .fasta contient 4 pipe "|" min -> Contig
                        if header.count("|") > 3:
                            contigParser("../Inputs/"+species+"/"+f_name)
                        
                        # Sinon : correspond à un ORF
                        else:
                            seq = f.readline().rstrip("\n")
                            is_nucl = True
                            for letter in seq:
                                if letter not in set({'A', 'C', 'G', 'T'}):
                                    is_nucl = False
                            # Cas 2 : pas que des nucléotide -> protein
                            if not is_nucl:
                                proteinseqParser("../Inputs/"+species+"/"+f_name)
                            
                            # Sinon : correspond à un acide nucléique
                            else:
                                # Cas 3 : Un transcript commence par ">BC1T..."
                                if header[:5] == ">BC1T":
                                    transcriptseqParser("../Inputs/"+species+"/"+f_name)
                                # Cas 4 : Sinon, c'est un gène
                                else:
                                    geneseqParser("../Inputs/"+species+"/"+f_name)
                        
                    # Si le fichier est un .txt -> Il contient des infos sur gènes, contigs ou pfam
                    elif f_type == "txt":
                        # Ouverture du fichier text
                        try:
                            f = open("../Inputs/"+species+"/"+f_name, "r")
                        except IOError:
                            print("L'ouverture du fichier a échoué.")
                            sys.exit(1)
                        
                        header = f.readline().rstrip("\n")
                        # Cas 1 : summary_per_gene
                        if header == "LOCUS	SYMBOL	SYNOYM	LENGTH	START	STOP	STRAND	NAME	CHROMOSOME	GENOME ONTOLOGY	ENZYME CODE	KEGG	PATHWAY	REACTION	COG	PFAM	OPERON":
                            geneParser("../Inputs/"+species+"/"+f_name)
                        # Cas 2 : pfam2gene
                        elif header == "PROTEIN_NAME	LOCUS	GENE_CONTIG	PFAM_ACC	PFAM_NAME	PFAM_DESCRIPTION	PFAM_START	PFAM_STOP	LENGTH	PFAM_SCORE	PFAM_EXPECTED":
                            pfamParser("../Inputs/"+species+"/"+f_name)
                        # Sinon : on s'en fout
                    
                    # Fermeture du fichier
                    f.close()
                    
                    # Supression du fichier une fois processed en .csv
                    os.remove("../Inputs/"+species+"/"+f_name)
                        