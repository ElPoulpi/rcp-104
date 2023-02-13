# matrice et graph

## Devoir 1. Pour le graphe fourni

1. Calculer le plus court chemin d'un sommet à tous les autres avec l'algorithme Dijkstra.
2. Utiliser cet algorithme pour calculer la matrice D de distances entre chaque couple de sommets.
3. Utiliser cette matrice et les population de chaque sommet pour calculer un placement optimal d'un
"centre commercial" et d'un "caserne de pompiers.

## Devoir 2. Pour le graphe fourni

1. Calculer un arbre couvrant minimum avec l'algorithme de Kruskal.
2. En considérant les fréquentations des arêtes (en plus de leurs poids) fournir et calculer
une fonction bi-critère pour choisir un arbre couvrant optimal pour les deux critères.
Tester cette fonction pour des valeurs de alpha allant de 0 à 1 avec un pas de 0.01.

matrice:
```
0, 2, 4, 0, 0, 0, 0, 0
2, 0, 0, 5, 0, 0, 0, 0
4, 0, 0, 1, 0, 0, 4, 0
0, 5, 1, 0, 0, 6, 1, 0
0, 0, 0, 0, 0, 1, 2, 7
0, 0, 0, 6, 1, 0, 0, 0
0, 0, 4, 1, 2, 0, 0, 3
0, 0, 0, 0, 7, 0, 3, 0
```
