# planet-classification





I

main.py

L'objectif de cette analyse est de prédire la disposition des exoplanètes (par exemple, si elles sont candidates ou confirmées) '
à partir de leurs caractéristiques physiques (comme la période orbitale,
la température, etc.) 
en utilisant un modèle de classification basé sur un arbre
de décision. On évalue ensuite la performance du modèle avec l'exactitude et la
matrice de confusion.
En parallèle, une analyse de clustering non supervisée avec
l'algorithme K-means est réalisée pour découvrir des groupes d'exoplanètes similaires en fonction de leurs caractéristiques,
afin de mieux comprendre la structure des données.

En résumé, cette analyse combine des méthodes de
classification supervisée et de clustering non supervisé pour prédire des catégories
et explorer des patterns cachés dans les données des exoplanètes.


Modèle d'arbre de décision:
![image](https://github.com/user-attachments/assets/e81f4637-d865-480b-bad6-52c6fc62da60)

Affichage de la matrice de confusion:
![image](https://github.com/user-attachments/assets/d5e0422d-9b02-484c-8788-bd2f9ff9a449)

Affichage de la méthode du coude (inertie):
![image](https://github.com/user-attachments/assets/2f8bdc91-acd1-4f35-9323-f73261117cf7)

Affichage des Silhouette Scores:
![image](https://github.com/user-attachments/assets/65c90914-7d7d-4f82-9111-c5e04707bd09)



_________________________________________________________________________________________________________________________________________________________

II

terre_soleil.ipynb



🌡️ Température moyenne estimée (modèle en équilibre radiatif) La température moyenne de la Terre 𝑇 T (en Kelvin) peut être estimée par :

𝑇
( ( 1 − 𝐴 ) ⋅ 𝑆 4 ⋅ 𝜎 ⋅ 𝐷 2 ) 1 / 4 T=( 4⋅σ⋅D 2

(1−A)⋅S​) 1/4

Où :

𝐴 A = albédo terrestre moyen ≈ 0.3

𝑆 S = constante solaire ≈ 1361 W/m² (puissance reçue à 1 UA)

𝜎 σ = constante de Stefan-Boltzmann ≈ 5.67 × 10⁻⁸ W·m⁻²·K⁻⁴

𝐷 D = distance Terre-Soleil en UA

Cette formule suppose que la Terre est une sphère noire recevant le rayonnement solaire, sans atmosphère (≈ 255 K). Avec l’effet de serre, la température réelle moyenne est ≈ 288 K.
