#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

#~ os.chdir("/Users/karl-stephan.baczkowski/Documents/Prog_Web/Projet_Web")

#~ seq_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_proteins.fasta", "r")


def proteinseqParser(infile):
    # Créer le chemin vers la sortie
    path_LIST = infile.split("/")[:-1]
    path_LIST[-2] = "Outputs"
    path_LIST += ["Tables_SQL", "protein_seq.csv"]
    outfile = "/".join(path_LIST)
    
    # Ecriture de l'output
    try:
        seq_table = open(outfile, "w")
    except IOError:
        print("L'ouverture du fichier "+outfile+" a échoué")
        sys.exit(1)
    seq_table.write("prot_id;gene_id;length;sequence\n")
    
    # Lecture de l'input
    try:
        seq_file = open(infile,'r')
    except IOError:
        print("L'ouverture du fichier "+infile+" a échoué")
        sys.exit(1)
    

    LIST = seq_file.readline().lstrip(">").rstrip(" aa)\n").split(" | ")
    seq = LIST[0] + ";" + LIST[1] + ";" + LIST[2].split(" (")[-1] + ";"

    line = seq_file.readline()
    while line != "":
        if line[0] != ">":
            seq += line.rstrip("\n")
        else:
            seq_table.write(seq + "\n")
            LIST = line.lstrip(">").rstrip(" aa)\n").split(" | ")
            seq = LIST[0] + ";" + LIST[1] + ";" + LIST[2].split(" (")[-1] + ";"
        line = seq_file.readline()
    seq_table.write(seq + "\n")

    seq_file.close()
    seq_table.close()

def main():
    infile = sys.argv[1]
    proteinseqParser(infile)
