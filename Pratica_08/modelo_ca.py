# 1. Importação das bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    roc_auc_score, 
    confusion_matrix,
    roc_curve
)

# 2. Carregamento do Dataset
# A variável 'data' contém as características (features) e 'target' contém os rótulos (labels)
data = load_breast_cancer()
X = data.data
y = data.target

# Para referência, vamos ver os nomes das classes (0 = maligno, 1 = benigno)
# print(f"Nomes das classes: {data.target_names}")

# 3. Divisão dos dados em Treino e Teste
# 70% para treino e 30% para teste
# random_state garante que a divisão seja sempre a mesma (reprodutibilidade)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3, 
    random_state=42
)

# 4. Criação e Treinamento do Modelo
# Utilizando o algoritmo Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Realização das Previsões no Conjunto de Teste
y_pred = model.predict(X_test)
# Para a curva ROC, precisamos das probabilidades da classe positiva (1: benigno)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# 6. Cálculo das Métricas de Classificação
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc_roc = roc_auc_score(y_test, y_pred_proba)
conf_matrix = confusion_matrix(y_test, y_pred)

# 7. Apresentação dos Resultados
print("--- Métricas de Desempenho do Modelo Random Forest ---")
print(f"Acurácia: {accuracy:.4f}")
print(f"Precisão: {precision:.4f}")
print(f"Recall (Sensibilidadpythone): {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc_roc:.4f}")
print("\n--- Matriz de Confusão ---")
print("         Previsto Neg (0) | Previsto Pos (1)")
print(f"Real Neg (0) |     {conf_matrix[0][0]:<10} |     {conf_matrix[0][1]:<10}")
print(f"Real Pos (1) |     {conf_matrix[1][0]:<10} |     {conf_matrix[1][1]:<10}")
# TN, FP
# FN, TP

# 8. Visualização da Curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'Curva ROC (AUC = {auc_roc:.4f})')
plt.plot([0, 1], [0, 1], color='red', lw=2, linestyle='--', label='Classificador Aleatório')
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR) - Recall')
plt.title('Curva ROC para o Classificador de Câncer de Mama')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()