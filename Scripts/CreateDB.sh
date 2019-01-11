mysql -u root <<EOF
CREATE DATABASE $1;
USE $1;
## CREATE DATABASE //databasename//;

CREATE TABLE contig (ContigID varchar(255), Chromosome varchar(255), Start varchar(255), Stop varchar(255), Length varchar(255), Sequence text(105000), PRIMARY KEY (ContigID));

#gene 
CREATE TABLE summaryGene (Locus varchar(255), Taille varchar(255), Start varchar(255), Stop varchar(255), Strand varchar(255), Name varchar(255), Chromosome varchar(255), PRIMARY KEY(Locus));

#geneseq
CREATE TABLE gene (Nom varchar(255), Sequence varchar(21000), PRIMARY KEY (Nom), CONSTRAINT seq_geneID FOREIGN KEY(Nom) REFERENCES summaryGene(Locus));

CREATE TABLE pfam (PfamAcc varchar(255), Nom varchar(255), Description varchar(255), PRIMARY KEY (PfamAcc));

CREATE TABLE pfamToGene (NumHit varchar(255), GeneID varchar(255), PfamAcc varchar(255), Start varchar(255), Stop varchar(255), Taille varchar(255), Score varchar(255), Expected varchar(255), PRIMARY KEY(NumHit, GeneID), CONSTRAINT pfam_2_geneID FOREIGN KEY(GeneID) REFERENCES summaryGene(Locus),
CONSTRAINT gene_2_pfamACC FOREIGN KEY(PfamAcc) REFERENCES pfam(PfamAcc));

CREATE TABLE seq_tran (tran_id varchar(255), gene_id varchar(255), length varchar(255), sequence text(25000), PRIMARY KEY(tran_id), CONSTRAINT seq_tranID FOREIGN KEY(gene_id) REFERENCES summaryGene(Locus));

CREATE TABLE proteine (prot_id varchar(255), gene_id varchar(255), length varchar(255), sequence varchar(10000), PRIMARY KEY(prot_id), CONSTRAINT seq_protID FOREIGN KEY(gene_id) REFERENCES summaryGene(Locus));
exit
EOF