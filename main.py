
# Import des bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns

# Chargement des données
df = pd.read_csv('cumulative.csv')

# Affichage des informations de base sur les données
print("5 premières lignes du DataFrame :")
print(df.head())
print("\n5 dernières lignes du DataFrame :")
print(df.tail())
print("\nDimensions du DataFrame (lignes, colonnes) :")
print(df.shape)

# Liste des colonnes pour comprendre la structure des données
print("Colonnes disponibles dans le DataFrame :")
print(df.columns)

# Sélection de la colonne cible (y)
# Ici, on suppose que 'koi_disposition' est la colonne cible
y = df['koi_disposition']

# Sélection des features (X)
# Ici, nous prenons des colonnes numériques pertinentes, à ajuster si nécessaire
X = df[['koi_period', 'koi_depth', 'koi_prad', 'koi_teq', 'koi_insol']]

# Vérification des valeurs nulles dans X et y
print("Valeurs nulles dans X :", X.isnull().sum().sum())
print("Valeurs nulles dans y :", y.isnull().sum())

# Traitement des valeurs nulles si elles existent
# Suppression des lignes avec valeurs nulles
X = X.dropna()
y = y[X.index]  # Assure que X et y aient les mêmes indices après suppression


# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Affichage des dimensions des ensembles d'entraînement et de test
print("Dimensions de X_train :", X_train.shape)
print("Dimensions de X_test :", X_test.shape)
print("Dimensions de y_train :", y_train.shape)
print("Dimensions de y_test :", y_test.shape)

# Entraînement d'un modèle d'arbre de décision
clf = DecisionTreeClassifier(random_state=42, max_depth=3)  # Limiter la profondeur pour simplifier
clf.fit(X_train, y_train)

# Prédictions sur l'ensemble de test
y_pred = clf.predict(X_test)

# Calcul de l'exactitude
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitude du modèle : {accuracy:.4f}")

# Affichage de la matrice de confusion
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=clf.classes_, yticklabels=clf.classes_)
plt.title("Matrice de confusion")
plt.xlabel("Prédictions")
plt.ylabel("Vrais labels")
plt.show()

# Affichage de l'arbre de décision avec matplotlib
plt.figure(figsize=(20, 10))  # Ajuster la taille pour une meilleure lisibilité
plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True, rounded=True)
plt.title("Arbre de décision pour la classification de 'koi_disposition'")
plt.show()

# Visualisation des prédictions et des vrais labels (optionnel)
plt.figure(figsize=(10, 6))
plt.scatter(range(len(y_test)), y_test, color="blue", label="Vrais labels", alpha=0.6)
plt.scatter(range(len(y_pred)), y_pred, color="red", label="Prédictions", alpha=0.6)
plt.title("Comparaison entre les vrais labels et les prédictions")
plt.xlabel("Index")
plt.ylabel("Classe")
plt.legend()
plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Normalisation des données (standardisation)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Normalisation des features

# Test pour différentes valeurs de k
inertia = []  # Inertie (somme des distances au centre des clusters)
sil_scores = []  # Silhouette scores

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)  # Utilisation de X_scaled
    inertia.append(kmeans.inertia_)
    sil_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Affichage de la méthode du coude (inertie)
plt.plot(range(2, 11), inertia, marker='o')
plt.title("Méthode du coude pour choisir k")
plt.xlabel("Nombre de clusters")
plt.ylabel("Inertie")
plt.show()

# Affichage des Silhouette Scores
plt.plot(range(2, 11), sil_scores, marker='o')
plt.title("Silhouette Scores pour choisir k")
plt.xlabel("Nombre de clusters")
plt.ylabel("Silhouette Score")
plt.show()

# Affichage de la comparaison entre les vraies étiquettes et les prédictions
comparison = pd.DataFrame({'Vrai label': y_test, 'Prédiction': y_pred})
print(comparison.head())
