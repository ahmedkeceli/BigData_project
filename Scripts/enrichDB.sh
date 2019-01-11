mysql -u root <<EOF
USE $1;
SOURCE ../DSW/Outputs/$1/contigSQL.sql;
SOURCE ../DSW/Outputs/$1/geneSQL.sql;
SOURCE ../DSW/Outputs/$1/gene_seqSQL.sql;
SOURCE ../DSW/Outputs/$1/proteinSQL.sql;
SOURCE ../DSW/Outputs/$1/transcriptSQL.sql;
SOURCE ../DSW/Outputs/$1/pfamSQL.sql;
SOURCE ../DSW/Outputs/$1/p2gSQL.sql;
exit
EOF