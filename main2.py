import csv
from collections import Counter
import dernier_tweet
from tqdm import tqdm
#travailler ligne(s) par ligne(s)
#colonnes 57 
#lignes 1531507
#collected via thread only : 43
    # collected_via_thread_only,0,1267726 --- OK 
    # collected_via_thread_only,1,263780 --- 


### FILTRAGE -- il faut recréer un fichier csv


def filtrage(fichier, fichier_filtre):
    # Definir un fichier csv et le créer ? 
    with open(fichier, 'r') as f:
        file_content = csv.reader(f)
        l = []
        for j,r in tqdm(enumerate(file_content)):
            if j==0:
                l.append(r)
            if r[43]=='0':
                l.append(r)
    f2 = open(fichier_filtre, 'w')
    with f2:
        writer = csv.writer(f2)
        writer.writerows(l)  
    
       
### tweets_filtres
filtrage('tweets_proj1.csv','tweets_filtres.csv')

def utilisateurs_tp50(fc):
    with open(fc, 'r') as f:
        file_content = csv.reader(f)
        utilisateurs = set()
        top50 = Counter()
        for j, r in tqdm(enumerate(file_content)):
            utilisateurs.add(r[3])
            top50[r[3]]+=1 # collections COUNTER
        top50 = top50.most_common(50)
        return (utilisateurs, top50)

(uti,top50) = utilisateurs_tp50('tweets_filtres.csv')
utilisateurs = (uti,top50)[0]
top50 = (uti,top50)[1]
print(len(utilisateurs))

######## ----- Application du deuxieme filtre pour ne récupèrer qu'un tweet par utilisateurs
with open('top50.csv','w') as top:
    writer = csv.writer(top)
    writer.writerow(['username','nb_tweets'])
    writer.writerows(top50) 
#dernier_tweet.dernier_tweet(utilisateurs,'tweets_filtres.csv','tweets_uniques.csv')
