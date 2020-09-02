import csv
from tqdm import tqdm
# 'from_user_id':24

def dernier_tweet(utilisateurs,fich_input,fich_output):
    uti_tweetsdate = {}
    uti_tweets = {}
    headers = []
    with open(fich_input, 'r') as f:
        file_content = csv.reader(f)
         #on ne peut pas utiliser un collections.counter() car le type comparé est problematique
        #initialisation du dictionnaire 
        for u in utilisateurs:
            uti_tweetsdate[u]= '1920-00-05T00:00:00'
            uti_tweets[u] = 0
        for j,r in enumerate(file_content):
            if j==0:
                headers.append(r)
            if uti_tweetsdate[r[3]] < r[2]: #problemes
                uti_tweetsdate[r[3]] = r[2]
                uti_tweets[r[3]] = r
    for nom,tweet in uti_tweets.items():
        headers.append(tweet) 
    with open(fich_output,'w') as f2:
        writer = csv.writer(f2)
        writer.writerows(headers) 
