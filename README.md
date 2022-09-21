# projet_uber_bloc3

Etape 1 :
EDA et Data cleaning

Etape 2 :
Utilisation du modèle de machine learning Kmeans clustering.
Le principe est de laisser le modèle classer les données selon leurs ressemblences.
    ° La première étape est de déterminer le nombre de clusters, après avoir appliquer un standartscaller et un numerique encoder, la donnée est prépocessée.
    ° Nous allons déterminer le nombre de cluster en utilisant la méthode Elbow pour trouver le nombre optimal de clusters puis la silhouette_score pour déterminer le nombre optimal de clusters.
    ° et enfin, il faut entrainer Kmeans avec le nombre optimal de cluster.

Comment fonctionne KMEANS :
  Kmeans va placer des centroïd au hasard dans la donnée, ensuite on affecte chaques points du dataset au centroïde le plus proche, ce qui nous donne des clusters puis on déplace chaques centroïdes au milieu de son cluster et on recommence jusqu'à ce que les centroïdes convergent dans une position d'équilibre.
  

![](https://github.com/DATA-ICARD/projet_uber_bloc3/blob/main/kmeans.gif)
