#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,sys, csv

#~ os.chdir("/Users/karl-stephan.baczkowski/Documents/Prog_Web/Projet_Web")

#~ gene_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_genome_summary_per_gene.txt", "r")


def geneParser(infile):
    # Créer le chemin vers la sortie
    path_LIST = infile.split("/")[:-1]
    path_LIST[-2] = "Outputs"
    path_LIST += ["gene.csv"]
    outfile = "/".join(path_LIST)
    
    # Ecriture de l'output
    try:
        gene_table = open(outfile, "w")
    except IOError:
        print("L'ouverture du fichier "+outfile+" a échoué")
        sys.exit(1)
    gene_table.write("gene_id;length;start;stop;strand;name;supercontig\n")
    
    # Lecture de l'input
    try:
        gene_file = open(infile,'r')
    except IOError:
        print("L'ouverture du fichier "+infile+" a échoué")
        sys.exit(1)
    
    line = gene_file.readline()
    line = gene_file.readline()

    while line != "":
        LIST = line.split("\t")
        gene_table.write(";".join([LIST[0]] + LIST[3:9]) + "\n")
        line = gene_file.readline()
        
    gene_file.close()
    gene_table.close()
    
def main():
    infile = sys.argv[1]
    geneParser(infile)

