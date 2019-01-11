mysql -u root <<EOF
CREATE DATABASE $1;
USE $1;
CREATE TABLE contig (ID varchar(255), Chromosome varchar(255), Start varchar(255), Stop varchar(255), Length varchar(255), Sequence text(105000), PRIMARY KEY (ID));
CREATE TABLE summaryGene (Locus varchar(255), Taille varchar(255), Start varchar(255), Stop varchar(255), Strand varchar(255), Name varchar(255), Chromosome varchar(255), PRIMARY KEY(Locus));
CREATE TABLE gene (ID varchar(255), Sequence varchar(21000), PRIMARY KEY (ID), CONSTRAINT seq_geneID FOREIGN KEY(ID) REFERENCES summaryGene(Locus));
CREATE TABLE pfam (PfamAcc varchar(255), Nom varchar(255), Description varchar(255), PRIMARY KEY (PfamAcc));
CREATE TABLE pfamToGene (NumHit varchar(255), GeneID varchar(255), PfamAcc varchar(255), Start varchar(255), Stop varchar(255), Taille varchar(255), Score varchar(255), Expected varchar(255), PRIMARY KEY(NumHit, GeneID), 
CONSTRAINT pfam_2_geneID FOREIGN KEY(GeneID) REFERENCES summaryGene(Locus), CONSTRAINT gene_2_pfamACC FOREIGN KEY(PfamAcc) REFERENCES pfam(PfamAcc));
CREATE TABLE transcript (ID varchar(255), gene_id varchar(255), length varchar(255), Sequence text(25000), PRIMARY KEY(ID), CONSTRAINT seq_tranID FOREIGN KEY(gene_id) REFERENCES summaryGene(Locus));
CREATE TABLE proteine (ID varchar(255), gene_id varchar(255), length varchar(255), Sequence varchar(10000), PRIMARY KEY(ID), CONSTRAINT seq_protID FOREIGN KEY(gene_id) REFERENCES summaryGene(Locus));
exit
EOF