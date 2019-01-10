#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import operator

#~ os.chdir("/Users/karl-stephan.baczkowski/Documents/Prog_Web/Projet_Web")

#~ p2g_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_pfam_to_genes.txt", "r")

def pfamParser(infile):
    # 2 libraries that respectively collects pfam annotations and pfam hit details
    PFAM = set(); P2G = dict()
    
    # Lecture de l'input
    try:
        p2g_file = open(infile,'r')
    except IOError:
        print("L'ouverture du fichier "+infile+" a échoué")
        sys.exit(1)
    
    line = p2g_file.readline()
    line = p2g_file.readline()

    # Fill in PFAM and P2G libraries
    while line != "":
        LIST = line.rstrip("\n").split("\t")
        
        # Update PFAM library
        annot = ";".join(LIST[3:6])
        if annot not in PFAM:
            PFAM.update({annot})
        
        # Screen each hit for one gene, one pfam motif, one location (avoid duplicates)
        gene = LIST[1];     pfam = ";".join(LIST[3:4] + LIST[6:9])
        score = float(LIST[9]);     expected = float(LIST[10])
        
        if gene not in P2G:
            P2G[gene] = dict()
        
        if (pfam not in P2G[gene]) or (P2G[gene][pfam][0] < score):
            P2G[gene][pfam] = [score, expected]
        
        line = p2g_file.readline()

    p2g_file.close()
    
    # Chemin vers les outputs
    path_LIST = infile.split("/")[:-1]
    path_LIST[-2] = "Outputs"
    path_LIST += ["Tables_SQL"]
    pfam_file = "/".join(path_LIST + ["pfam.csv"])
    p2g_file = "/".join(path_LIST + ["pfam2gene.csv"])

    # Write PFAM and P2G tables
    try:
        pfam_table = open(pfam_file, "w")
    except IOError:
        print("L'ouverture du fichier "+pfam_file+" a échoué")
        sys.exit(1)
    pfam_table.write("pfam_acc;name;description\n")
    pfam_table.write("\n".join(sorted(PFAM)) + "\n")
    pfam_table.close()
    
    try:
        p2g_table = open(p2g_file, "w")
    except IOError:
        print("L'ouverture du fichier "+p2g_file+" a échoué")
        sys.exit(1)
    p2g_table.write("num_hit;gene_id;pfam_acc;start;stop;length;score;expected\n")
    for gene in sorted(P2G):
        num_hit = 1
        for pfam,score_exp in sorted(P2G[gene].items(), key=operator.itemgetter(1), reverse=True):
            p2g_table.write(str(num_hit) + ";" + gene + ";" + pfam + ";")
            p2g_table.write(str(round(score_exp[0],1)) + ";" + "{:0.1e}".format(score_exp[1]) + "\n")
            num_hit += 1
    p2g_table.close()
    
def main():
    infile = sys.argv[1]
    pfamParser(infile)
