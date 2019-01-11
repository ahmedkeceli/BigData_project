# BigData_project
TOOL TO CREATE DYNAMIC DATABASES FROM FASTA FILES FOR WEB INTERFACE

PRÉ-REQUIS                       


    - MYSQL doit être installé et peut être lancé dans le Terminal
    - Votre session MYSQL est de la forme : mysql -u root (le mot de passe est vide)

LANCEMENT                      


Dans un premier temps ouvrir votre Terminal et placez vous dans le répertoire que vous souhaitez.
Lancer la commande suivante:

    git clone https://github.com/ahmedkeceli/BigData_project.git

Cette commande vous permettra de récupérer l'ensemble du workflow avec tous les scripts permettant de structurer vos données.

Une fois que le téléchargement est terminé, lancer la commande suivante vous permettant de vous rendre dans le répertoire BigData_project:

    cd BigData_project

Vous êtes maintenant prêt à créer votre Base de données.

Création de la BD                      


  - PRÉ-REQUIS
    - Avoir tous vos fichiers .fasta et .txt
  
 Pour créer votre BD, il vous faut entrer la commande suivante
  
  python Scripts/master.py <nom_espèce_à_ajouter> <path/to/file1.FASTA> <path/to/file2.FASTA> ... <path/to/fileN.FASTA>

Par exemple:
  Créer une Base de donnée spécifique à l'éspèce Botrytis Cinerea
  
      python Scripts/master.py Botrytis keceli/Desktop/Botrytis/gene.fasta keceli/Desktop/Botrytis/prot.fasta keceli/Desktop/Botrytis/contig.fasta keceli/Desktop/Botrytis/trans.fasta keceli/Desktop/Botrytis/summary_gene.fasta

Visualiser de la BD                      


Maintenant que vous avez créé votre Base de donnée vous pouvez vous connecter à mysql est observer votre Base de donnée liée à l'espèce.
  
  
