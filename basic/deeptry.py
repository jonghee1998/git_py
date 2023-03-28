import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 데이터 로드
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 트레이닝, 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN 모델 생성 및 학습
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 예측 및 평가
y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 데이터 시각화
features = iris.feature_names
target_names = iris.target_names

for feature_idx in range(X.shape[1]):
    for target_idx in range(len(target_names)):
        plt.scatter(X[y == target_idx, feature_idx], y[y == target_idx], label=target_names[target_idx])

    plt.xlabel(features[feature_idx])
    plt.ylabel('Target')
    plt.legend()
    plt.title(f"{features[feature_idx]} vs. Target")
    plt.show()
