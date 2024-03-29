import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script
os.chdir("csvs")
# Importez csv
import csv

 

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
# 
#          Aucune instruction détaillée n'est donnée plus bas
with open("Ex7 Lan Party.csv" , encoding='utf-8') as csv_file :
    csv_reader = csv.reader(csv_file , delimiter=';')
    with open("Ex7 Lan Party Valorant" , "w" , encoding='utf-8') as csv_file_writer :
        csv_writer = csv.writer(csv_file_writer , delimiter=';' , lineterminator='\n')
        csv_writer.writerow(["Lan Party" , "Top 1" , "Top 2" , "Top 3"])
        next(csv_reader)
        for line in csv_reader :
            if "Valorant" in line:
                csv_writer.writerow(line)
        




