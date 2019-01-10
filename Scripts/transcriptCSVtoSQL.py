import os, sys

#IN : transcript_seq.csv



infile = sys.argv[1]

gene_table = open("Results/transcriptSQL.sql", "w")
#gene_table.write("gene_id\tlength\tstart\tstop\tstrand\tname\tsupercontig\n")

with open(infile,'r') as gene_file:
    
	line = gene_file.readline()
	line = gene_file.readline()

	while line != "":

		LIST = line.split(";")
		for i in range(0,4):
			#if ( (i != 1) or (i !=2) or (i !=3) or (i !=6)) :
			LIST[i]="'" + LIST[i] + "'"
		gene_table.write("INSERT INTO seq_tran (tran_id, gene_id, length, sequence) VALUES (")
		gene_table.write(",".join(LIST[0:4]) + ");\n")
		#gene_table.write([LIST[0] + LIST[1] + [LIST[2] + LIST[3] + LIST[3] + LIST[3] + LIST[3] + LIST[3:9]) + ");\n")
		line = gene_file.readline()

	gene_file.close()
	gene_table.close()

