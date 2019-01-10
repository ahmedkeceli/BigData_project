import os,sys

#~ gene_file = open("Donnees_Botrytis_cinerea/botrytis_cinerea__b05.10__1_genome_summary_per_gene.txt", "r")

###### prends en entre un csv et le transforme en requetes SQL pour remplir la table summary per gene #######

infile = sys.argv[1]

gene_table = open("Results/geneSQL.sql", "w")
#gene_table.write("gene_id\tlength\tstart\tstop\tstrand\tname\tsupercontig\n")

with open(infile,'r') as gene_file:
    
	line = gene_file.readline()
	line = gene_file.readline()

	while line != "":
		line = line.replace("'","prime")

		LIST = line.split(";")
		for i in range(0,7):
			#if ( (i != 1) or (i !=2) or (i !=3) or (i !=6)) :
			LIST[i]="'" + LIST[i] + "'"
		gene_table.write("INSERT INTO summaryGene (Locus, Taille, Start, Stop, Strand, Name, Chromosome) VALUES (")
		gene_table.write(",".join([LIST[0]] + LIST[1:3] + LIST[3:8]) + ");\n")
		#gene_table.write([LIST[0] + LIST[1] + [LIST[2] + LIST[3] + LIST[3] + LIST[3] + LIST[3] + LIST[3:9]) + ");\n")
		line = gene_file.readline()

	gene_file.close()
	gene_table.close()









