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




![image](https://github.com/user-attachments/assets/b1145101-cc6b-43e1-afb3-e18dfa00e88c)







Pour calculer la distance moyenne du Soleil à la Terre au cours de l'année, ainsi que la température moyenne de la Terre en fonction des mois de l'année, nous devons intégrer à la fois la variation de la distance (qui est fonction de la position de la Terre dans son orbite elliptique) et la température globale de la Terre qui en découle.

Calcul de la distance moyenne du Soleil à la Terre La distance moyenne de la Terre au Soleil varie au cours de l'année en raison de l'excentricité de l'orbite terrestre. Une approximation classique de la variation de cette distance, en fonction du temps, est donnée par l'excentricité de l'orbite terrestre et la loi des aires de Kepler.
Distance moyenne (en Astronomical Unit - AU) L'excentricité de l'orbite de la Terre est d'environ 𝑒 = 0.0167 e=0.0167, et la distance moyenne de la Terre au Soleil est de 1 AU (150 millions de km). La distance réelle varie autour de cette valeur tout au long de l'année.

On peut modéliser la distance 𝐷 D de la Terre au Soleil par une fonction qui dépend du temps, et qui prend en compte la variation de la distance au cours de l'année due à l'orbite elliptique.

𝐷 ( 𝑡 ) = 1   AU 1 + 𝑒 cos ⁡ ( 𝜃 ) D(t)= 1+ecos(θ) 1AU​

Où :

𝜃 θ est l'angle de la Terre par rapport au Soleil, qui change au cours de l'année.

𝑒 e est l'excentricité de l'orbite terrestre.

Calcul de la température en fonction de la distance La température de la Terre dépend de la quantité d'énergie reçue du Soleil, qui est inversement proportionnelle au carré de la distance au Soleil. Nous pouvons utiliser la loi de Stefan-Boltzmann pour ajuster la température :
𝑇 radiative = ( ( 1 − 𝐴 ) 𝑆 4 𝜎 𝐷 2 ) 1 / 4 T radiative​=( 4σD 2

(1−A)S​) 1/4

Où :

𝐴 A est l'albédo de la Terre (environ 0.3),

𝑆 S est la constante solaire ( 𝑆 = 1361   W/m 2 S=1361W/m 2 ),

𝜎 σ est la constante de Stefan-Boltzmann ( 𝜎 = 5.67 × 10 − 8   W/m 2 K 4 σ=5.67×10 −8 W/m 2 K 4 ),

𝐷 D est la distance de la Terre au Soleil (en AU, à convertir en mètres pour calculer la température),

𝑇 radiative T radiative​est la température de la Terre résultant de l'équilibre radiatif.



![image](https://github.com/user-attachments/assets/58149fb5-900b-4e3b-8bae-256cb16a1a1d)


....
