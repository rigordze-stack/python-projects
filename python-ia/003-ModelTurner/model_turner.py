import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score

# Cargar dataset real
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Definir modelos
models = {
    "Logistic Regression": LogisticRegression(max_iter=10000),
    "KNN (k=5)": KNeighborsClassifier(n_neighbors=5)
}

# Definir métricas personalizadas
scorers = {
    "Accuracy": make_scorer(accuracy_score),
    "Precision": make_scorer(precision_score),
    "Recall": make_scorer(recall_score),
    "F1": make_scorer(f1_score)
}

# Evaluar cada modelo
results = {}
for name, model in models.items():
    print(f"\nEvaluando modelo: {name}")
    scores = []
    for metric_name, scorer in scorers.items():
        cv_score = cross_val_score(model, X, y, cv=5, scoring=scorer)
        mean_score = np.mean(cv_score)
        scores.append(mean_score)
        print(f"{metric_name}: {mean_score:.4f}")
    results[name] = scores

# Crear gráfico comparativo
metric_names = list(scorers.keys())
bar_width = 0.35
index = np.arange(len(metric_names))

plt.figure(figsize=(10, 6))
for i, (model_name, scores) in enumerate(results.items()):
    plt.bar(index + i * bar_width, scores, bar_width, label=model_name)
    for j, score in enumerate(scores):
        plt.text(index[j] + i * bar_width, score + 0.01, f"{score:.2f}", ha='center')

plt.xlabel("Métricas")
plt.ylabel("Score promedio")
plt.title("Comparación de modelos por métrica")
plt.xticks(index + bar_width / 2, metric_names)
plt.ylim(0, 1.1)
plt.legend()
plt.tight_layout()
plt.show()

input("Presiona ENTER para salir...")
