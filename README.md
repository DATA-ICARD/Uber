# Projet_uber_bloc3  
Recommandation des zones chaudes dans les grandes villes à tout moment de la journée. (sujet détaillé : https://github.com/DATA-ICARD/projet_uber_bloc3/blob/main/sujet_uber_pickups.ipynb)

Etape 1 :  

EDA et Data cleaning (uber_data)

Etape 2 (Déterminer le modèle) :  

_Utilisation du modèle de machine learning Kmeans clustering._  

Le principe est de laisser le modèle classer les données selon leurs ressemblences.  
    ° La première étape est de déterminer le nombre de clusters, après avoir appliquer un standartscaller et un numerique encoder, la donnée est prépocessée.  
    ° Nous allons déterminer le nombre de cluster en utilisant la méthode Elbow pour trouver le nombre optimal de clusters puis la silhouette_score pour déterminer le nombre optimal de clusters.  
    ° et enfin, il faut entrainer Kmeans avec le nombre optimal de cluster.  

Comment fonctionne KMEANS :  
  Kmeans va placer des centroïd au hasard dans la donnée, ensuite on affecte chaques points du dataset au centroïde le plus proche, ce qui nous donne des clusters puis on déplace chaques centroïdes au milieu de son cluster et on recommence jusqu'à ce que les centroïdes convergent dans une position d'équilibre.


![](https://github.com/DATA-ICARD/projet_uber_bloc3/blob/main/kmeans.gif)

_MODELE NON RETENU : Les K-Means sont mal adaptés aux situations où les clusters que nous recherchons ne sont pas en forme de boule._  

_Utilisation du modèle de machine learning dbscan._  

DBSCAN (density-based spatial clustering of applications with noise) est un algorithme de partitionnement de données.  
Il s’agit d’un algorithme fondé sur la densité dans la mesure qui s’appuie sur la densité estimée des clusters pour effectuer le partitionnement.

_Fonctionnement_  
L’algorithme DBSCAN utilise 2 paramètres :  
La distance ε et le nombre minimum de points « MinPts » devant se trouver dans un rayon ε pour que ces points soient considérés comme un cluster.

DBSCAN fonction de la maniere suivante :

1 – DBSCAN commence par un point de données de départ arbitraire qui n’a pas été visité. Le voisinage de ce point est extrait en utilisant une distance epsilon ε.

2 – S’il y a un nombre suffisant de points (selon les minPoints) dans ce voisinage, le processus de mise en cluster démarre et le point de données actuel devient le premier point du nouveau cluster.  
Sinon, le point sera étiqueté comme bruit (plus tard, ce point bruyant pourrait devenir la partie du cluster). Dans les deux cas, ce point est marqué comme «visité».

3 – Pour ce premier point du nouveau cluster, les points situés dans son voisinage à distance se joignent également au même cluster.  
Cette procédure est ensuite répétée pour tous les nouveaux points qui viennent d’être ajoutés au groupe de cluster.

4 – Ce processus des étapes 2 et 3 est répété jusqu’à ce que tous les points du cluster soient déterminés, c’est-à-dire que tous les points à proximité du ε voisinage du cluster ont été visités et étiquetés.

5 – Une fois terminé avec le cluster actuel, un nouveau point non visité est récupéré et traité, ce qui permet de découvrir un nouveau cluster ou du bruit. Ce processus se répète jusqu’à ce que tous les points soient marqués comme étant visités. A la fin de tous les points visités, chaque points a été marqué comme appartenant à un cluster ou comme étant du bruit.  
_(Source : https://penseeartificielle.fr/clustering-avec-lalgorithme-dbscan/)_  

![](https://github.com/DATA-ICARD/projet_uber_bloc3/blob/main/dbscan.gif)  
  
_MODELE RETENU_
