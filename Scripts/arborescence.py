# -*- coding: utf-8 -*-

import os
import sys
import subprocess

#Usage : python version1.py <nom_espece> <fichier 1> <fichier 2> ... <fichier n>

def Get_Path():
    path = os.getcwd()
    return path

def Get_arg(argu):
    liste_arg = []
    for arg in sys.argv:
        liste_arg.append(arg)
    return liste_arg
           

def Create_Arborescence(path):
    
    #Création du Répertoire Web_Master
    
        #Crée le nouveau chemin
    mypath = os.path.join("DSW")
        #Crée le répertoire
    os.makedirs(mypath)
    
    #Création des sous-répertoires
    
    DWM_path = path + "/DSW"
        #On change de répertoire de travail, on se place dans DSW
    os.chdir(DWM_path)
    
    #new_path = os.getcwd()
    #print("Vous êtes maintenant dans %s " % new_path)
    
    dossier_in = os.path.join("Inputs")
    dossier_out = os.path.join("Outputs")
    os.makedirs(dossier_in)
    os.makedirs(dossier_out)
    
def Create_Species_Dir(path):
    
    liste_arg = Get_arg(sys.argv)
    print(liste_arg)
    #~ print(Get_Path())
    if len(liste_arg) > 2:
        specie_name = liste_arg[1]
        os.chdir(path+"/Outputs")
        dossier_espece = os.path.join(specie_name)
        os.makedirs(dossier_espece)
        #Nous sommes dans SCRIPTS et souhaitons nous rendre dans les INPUTS
        os.chdir(path+"/Inputs")
        #~ print(Get_Path())
        #Crée un répertoire pour l'espèce voulue
        #Le nom est donné lors de l'execution
        dossier_espece = os.path.join(specie_name)
        os.makedirs(dossier_espece)
        
        #On récupère l'ensemble des fichiers
    
        liste_fic = []
        i = 2 #On commence à deux car argv[2] repésente un fichier
        while i < len(liste_arg):
            liste_fic.append(liste_arg[i])
            #~ print(liste_arg[i])
            i = i+1
            
        os.chdir("./"+specie_name)
        Move_file(liste_fic)

        #On déplace les fichiers dans le dossier input
        
        #~ print(len(liste_fic))
        #~ for fic in liste_fic:
            #~ print("esaai fic")
            #~ print(fic)
            #~ subprocess.call(["cp",fic,"."])
    else:
        print("Impossible de créer le repertoire sans vos fichiers")


def Move_file(liste_file):
    for fic in liste_file:
        subprocess.call(["cp",fic,"."])
    return
    
def Liste_File(path):
    fic = os.listdir(path)
    return fic

def Move_Py(path):
    for fic in os.listdir(path):
        if fic.split(".")[-1] == "py":
            subprocess.call(["cp",path+"/"+fic,path+"/DSW/Scripts/"+fic])
    return
    

def main():
    a = Get_Path()
    if os.path.isdir(a+"/DSW"):
        os.chdir(a+"/DSW/Inputs/")
        if os.path.isdir(a+"/DSW/Inputs/"+sys.argv[1]):
            os.chdir(a+"/DSW/Inputs/"+sys.argv[1])
            liste_arg = Get_arg(sys.argv)
            liste_fic = []
            i = 2 
            while i < len(liste_arg):
                liste_fic.append(liste_arg[i])
                i = i+1
            Move_file(liste_fic)
        else:
            #os.chdir("../Scripts")
            Create_Species_Dir(a+"/DSW")
    else:
        Create_Arborescence(a)
        #os.chdir(a+"/DSW/Scripts")
        Create_Species_Dir(a+"/DSW")
    os.chdir("../../../Scripts")
    #Move_Py(a)


main()
