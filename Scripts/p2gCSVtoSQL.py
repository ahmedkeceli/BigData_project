import os, sys
import operator


#IN : p2g.csv


espece = sys.argv[1]

gene_table = open("../DSW/Outputs/" + espece + "/p2gSQL.sql", "w")
#gene_table.write("gene_id\tlength\tstart\tstop\tstrand\tname\tsupercontig\n")

with open("../DSW/Outputs/" + espece + "/pfam2gene.csv",'r') as gene_file:
    
	line = gene_file.readline()
	line = gene_file.readline()

	while line != "":

		LIST = line.split(";")
		for i in range(0,8):
			#if ( (i != 1) or (i !=2) or (i !=3) or (i !=6)) :
			LIST[i]="'" + LIST[i] + "'"
		gene_table.write("INSERT INTO pfamToGene (NumHit, GeneID, PfamAcc, Start, Stop, Taille, Score, Expected) VALUES (")
		gene_table.write(",".join([LIST[0]] + LIST[1:8]) + ");\n")
		#gene_table.write([LIST[0] + LIST[1] + [LIST[2] + LIST[3] + LIST[3] + LIST[3] + LIST[3] + LIST[3:9]) + ");\n")
		line = gene_file.readline()

	gene_file.close()
	gene_table.close()

