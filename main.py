### Análise de dados
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

### Criação do modelo
from sklearn.tree import DecisionTreeClassifier
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
tree_predict = tree.predict(X_test)

tree_score = accuracy_score(y_test, tree_predict)
print(f"Pontuação Decision Tree:{tree_score}")


print("Entre com os dados para verificar a chace de recorrência da doença após o tratamento:")
age = int(input("Entre com a idade da paciente:\n"))
menopause = int(input("Com relação a menopausa da paciente, selecione uma das opções: 1 - Menopausa antes dos 40 2 - Menopausa depois dos 40 3 - Pré Menopausa\n"))
tumorSize = int(input("Indique a faixa do diâmetro do tumor em mm:\n"))
invNodes = int(input("Indique o número de linfonodos axilares:\n"))
nodeCaps = int(input("Informe se há penetração do tumor na cápsula do linfonodo: 1 - Não 2 - Sim\n"))
degMalig = int(input("Informe o grau de malignidade do tumor: 1 - Menor 2 - Médio 3 - Maior\n"))
breast = int(input("Informe a mama: 1 - Esquerda 2 - Direita\n"))
breastQuad = int(input("Informe o quadrante da mama afetado: 1 - esquerda-cima 2 - esquerda-baixo 3 - direita - cima 4 - direita - baixo 5 - centro\n"))
irradiat = int(input("Há histórico de radioterapia? 1 - Não 2 - Sim\n"))

ageValue = 0
if age >= 10 and age <= 19:
    ageValue = 1
elif age >= 20 and age <= 29:
    ageValue = 2
elif age >= 30 and age <= 39:
    ageValue = 3
elif age >= 40 and age <= 49:
    ageValue = 4
elif age >= 50 and age <= 59:
    ageValue = 5
elif age >= 60 and age <= 69:
    ageValue = 6
elif age >= 70 and age <= 79:
    ageValue = 7
elif age >= 80 and age <= 89:
    ageValue = 8
elif age >= 90 and age <= 99:
    ageValue = 9

tumorSizeValue = 0
if tumorSize <= 4:
    tumorSizeValue = 1
elif tumorSize >= 5 and age <= 9:
    ageValue = 2
elif tumorSize >= 10 and age <= 14:
    ageValue = 3
elif tumorSize >= 15 and age <= 19:
    ageValue = 4
elif tumorSize >= 20 and age <= 24:
    ageValue = 5
elif tumorSize >= 25 and age <= 29:
    ageValue = 6
elif tumorSize >= 30 and age <= 34:
    ageValue = 7
elif tumorSize >= 35 and age <= 39:
    ageValue = 8
elif tumorSize >= 40 and age <= 44:
    ageValue = 9
elif tumorSize >= 45 and age <= 49:
    ageValue = 10
elif tumorSize >= 50 and age <= 54:
    ageValue = 11
elif tumorSize >= 55 and age <= 59:
    ageValue = 12

invNodesValue = 0
if invNodes <= 2:
    invNodesValue = 1
elif invNodes >= 3 and invNodes <= 5:
    invNodesValue = 2
elif invNodes >= 6 and invNodes <= 8:
    invNodesValue = 3
elif invNodes >= 9 and invNodes <= 11:
    invNodesValue = 4
elif invNodes >= 12 and invNodes <= 14:
    invNodesValue = 5
elif invNodes >= 15 and invNodes <= 17:
    invNodesValue = 6
elif invNodes >= 18 and invNodes <= 20:
    invNodesValue = 7
elif invNodes >= 21 and invNodes <= 23:
    invNodesValue = 8
elif invNodes >= 24 and invNodes <= 26:
    invNodesValue = 9
elif invNodes >= 17 and invNodes <= 29:
    invNodesValue = 10
elif invNodes >= 30 and invNodes <= 32:
    invNodesValue = 11
elif invNodes >= 33 and invNodes <= 35:
    invNodesValue = 12
elif invNodes >= 36 and invNodes <= 39:
    invNodesValue = 13


dados = [[ageValue, menopause, tumorSizeValue, invNodesValue, nodeCaps, degMalig, breast, breastQuad, irradiat]]
resposta = tree.predict(dados)
if resposta == 1:
    print("Não há chances de recorrência da doença após o tratamento.")
elif resposta == 2:
    print("Há chances de recorrência da doença após o tratamento.")