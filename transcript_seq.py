#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

#~ os.chdir("/Users/karl-stephan.baczkowski/Documents/Prog_Web/Projet_Web")

#~ seq_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_transcripts.fasta", "r")


def transcriptseqParser(infile):
    # Créer le chemin vers la sortie
    path_LIST = infile.split("/")[:-1]
    path_LIST[-2] = "Outputs"
    path_LIST += ["Tables_SQL", "transcript_seq.csv"]
    outfile = "/".join(path_LIST)
    
    # Ecriture de l'output
    try:
        seq_table = open(outfile, "w")
    except IOError:
        print("L'ouverture du fichier "+outfile+" a échoué")
        sys.exit(1)
    seq_table.write("tran_id;gene_id;length;sequence\n")
    
    # Lecture de l'input
    try:
        seq_file = open(infile,'r')
    except IOError:
        print("L'ouverture du fichier "+infile+" a échoué")
        sys.exit(1)
    
        
    line = seq_file.readline().lstrip(">").split(" nt) ")[0]
    seq = line[:10] + ";BC1G" + line[4:10] + ";" + line.split("(")[-1] + ";"

    line = seq_file.readline()
    while line != "":
        if line[0] != ">":
            seq += line.rstrip("\n")
        else:
            seq_table.write(seq + "\n")
            line = line.lstrip(">").split(" nt) ")[0]
            seq = line[:10] + ";BC1G" + line[4:10] + ";" + line.split("(")[-1] + ";"
        line = seq_file.readline()
    seq_table.write(seq + "\n")

    seq_file.close()
    seq_table.close()

def main():
    infile = sys.argv[1]
    transcriptseqParser(infile)

