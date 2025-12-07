import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib



# 2. CHARGEMENT DU DATASET

print("=== Chargement du dataset ===")
df = pd.read_csv("Crop_recommendation.csv")

print("\nAperçu des données :")
print(df.head())

print("\nRépartition des cultures :")
print(df["label"].value_counts())

# Séparation X/y
X = df.drop("label", axis=1)
y = df["label"]


# 3. NORMALISATION

print("\n=== Normalisation des données ===")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# 4. TRAIN / TEST SPLIT

print("\n=== Séparation Train/Test ===")
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
print("Taille du train :", X_train.shape)
print("Taille du test :", X_test.shape)


# 5. ENTRAÎNEMENT DU RANDOM FOREST

print("\n=== Entraînement du modèle Random Forest ===")

model = RandomForestClassifier(
    n_estimators=200,       # 200 arbres = très bon résultat
    max_depth=None,         # profondeur libre 
    random_state=42,
    n_jobs=-1              
)

model.fit(X_train, y_train)

# 6. ÉVALUATION DU MODÈLE

print("\n=== Évaluation ===")

y_pred = model.predict(X_test)

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("\nMatrice de confusion :")
print(confusion_matrix(y_test, y_pred))


# 7. SAUVEGARDE DU MODELE
print("\n=== Sauvegarde ===")
joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("Modèle RandomForest sauvegardé : model.joblib")
print("Scaler sauvegardé : scaler.joblib")
