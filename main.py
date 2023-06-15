### Análise de dados
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt

### Criação do modelo
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

### Avaliação de métricas
from sklearn.metrics import accuracy_score

engine = create_engine('mysql+mysqlconnector://root:inatel@localhost/ag002')

query = "SELECT * FROM `breast-cancer`"
df = pd.read_sql(query, engine)
engine.dispose()

# instanciando modelos
tree = DecisionTreeClassifier()

# Separando dados
## Variáveis preditoras
X = df.loc[:, ["age", "menopause", "tumor-size", "inv-nodes", "node-caps", "deg-malig", "breast", "breast-quad", "irradiat"]].values
X = np.array(X)
print(X)

## Variável alvo
y = df.loc[:, ["class"]].values
y = np.array(y)

## Separando treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
print(f"Tamanho X de treino: {X_train.shape}")
print(f"Tamanho X de teste: {X_test.shape}")
print(f"Tamanho y de treino: {y_train.shape}")
print(f"Tamanho y de teste: {y_test.shape}")

# Treinando modelos
tree.fit(X_train, y_train)
print(X_test)
tree_predict = tree.predict(X_test)

tree_score = accuracy_score(y_test, tree_predict)
print(f"Pontuação Decision Tree:{tree_score}")

teste = [[4, 1, 3, 4, 1, 1, 2, 2, 2]]
print(teste)
resposta = tree.predict(teste)
print(resposta)