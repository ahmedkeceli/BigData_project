#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

#~ os.chdir("/Users/karl-stephan.baczkowski/Documents/Prog_Web/Projet_Web")

#~ contig_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_contigs.fasta", "r")


def contigParser(infile):
    # Créer le chemin vers la sortie
    path_LIST = infile.split("/")[:-1]
    path_LIST[-2] = "Outputs"
    path_LIST += ["Tables_SQL", "contig.csv"]
    outfile = "/".join(path_LIST)
    
    # Ecriture de l'output
    try:
        contig_table = open(outfile, "w")
    except IOError:
        print("L'ouverture du fichier "+outfile+" a échoué")
        sys.exit(1)
    contig_table.write("contig_id;supercontig;start;stop;length;sequence\n")
    
    # Lecture de l'input
    try:
        contig_file = open(infile,'r')
    except IOError:
        print("L'ouverture du fichier "+infile+" a échoué")
        sys.exit(1)
    
    LIST = contig_file.readline().lstrip(">").rstrip(" nt \n").split(" | ")
    contig = LIST[0] + ";" + LIST[2].split(" ")[-1][2:] + ";" + LIST[3].split("-")[0][1:] \
            + ";" + LIST[3].split("-")[1][:-1] + ";" + LIST[4] + ";"

    line = contig_file.readline()

    while line != "":
        if line[0] != ">":
            contig += line.rstrip("\n")
        else:
            contig_table.write(contig + "\n")
            LIST = line.lstrip(">").rstrip(" nt \n").split(" | ")
            contig = LIST[0] + ";" + LIST[2].split(" ")[-1][2:] + ";" + LIST[3].split("-")[0][1:] \
                    + ";" + LIST[3].split("-")[1][:-1] + ";" + LIST[4] + ";"
        line = contig_file.readline()
    contig_table.write(contig + "\n")

    contig_file.close()
    contig_table.close()

def main():
    infile = sys.argv[1]
    contigParser(infile)
