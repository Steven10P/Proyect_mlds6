### Librerías base

import pandas as pd

import numpy as np

import scipy

from scipy import stats

import statsmodels.api as sm

import statsmodels.formula.api as smf

import matplotlib.pyplot as plt

import matplotlib as mpl

%matplotlib inline

import seaborn as sns

import plotly



### Librerías para realizar Machine Learning en Python

# Actualizamos scikit-learn a la última versión

!pip install -U scikit-learn 



# Importamos scikit-learn y sus diferentes funcionalidades desde un principio

import sklearn

from sklearn import metrics, ensemble, model_selection



from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split



#Matplotlib y Seaborn - Librerías de visualización.

import matplotlib as mpl

import matplotlib.pyplot as plt

import seaborn as sns



# Visualización de grafos con graphviz.

import graphviz 





# Ignoramos las advertencias o warnings.

import warnings

warnings.simplefilter(action='ignore')



# Configuramos el formato por defecto de la 

# librería de visualización Matplotlib.

%matplotlib inline

%config InlineBackend.figure_format = 'retina'

mpl.rcParams['figure.dpi'] = 105

mpl.rcParams['figure.figsize'] = (9, 7)



# data preparation

from sklearn.preprocessing import *

from sklearn.decomposition import PCA

from sklearn.feature_selection import RFE, RFECV

from sklearn.utils import resample







# Función para visualizar un conjunto de datos de dos variables en un plano 2D.

def plot_data(X, y, model = None, ax = None, title=None):



    if ax is None:

      _, ax = plt.subplots(dpi = 110)



    if model is not None: 

      pred_fun = gen_pred_fun(model)

      plot_decision_region(X, pred_fun, ax)



    y_unique = np.unique(y)    

    df = pd.DataFrame({'x1': X[:,0], 'x2': X[:,1], 'Clases': y})

    sns.set_theme()

    sns.scatterplot(data = df, x = 'x1', y = 'x2', 

                    hue = 'Clases',style = 'Clases', ax = ax, palette = 'Set1').set_title(title)



# Función para visualizar la superficie de decisión de un clasificador.

def plot_decision_region(X, pred_fun, ax=None):

    min_x, max_x = np.min(X[:, 0]), np.max(X[:, 0])

    min_y, max_y = np.min(X[:, 1]), np.max(X[:, 1])

 

    min_x = min_x - (max_x - min_x) * 0.05

    max_x = max_x + (max_x - min_x) * 0.05

    min_y = min_y - (max_y - min_y) * 0.05

    max_y = max_y + (max_y - min_y) * 0.05



    x_vals = np.linspace(min_x, max_x, 100)

    y_vals = np.linspace(min_y, max_y, 100)



    XX, YY = np.meshgrid(x_vals, y_vals)

    grid_r, grid_c = XX.shape



    ZZ = np.zeros((grid_r, grid_c))



    for i in range(grid_r):

        for j in range(grid_c):

            ZZ[i, j] = pred_fun(XX[i, j], YY[i, j])    

    

    cs = ax.contourf(XX, YY, ZZ, 100, cmap = plt.cm.Pastel1, vmin = 0, vmax = np.max(ZZ)* 9. / (np.max(ZZ) + 1), alpha = 0.75)        

    ax.get_figure().colorbar(cs, ax=ax, )

    ax.set_xlabel("x")

    ax.set_ylabel("y")





# Función para visualizar la curva de aprendizaje a partir 

# del error de entrenamiento y de generalización.

def plot_learning_curve(train_error, generalization_error):

  n = len(train_error)

  if len(train_error) != len(generalization_error):

    print("Las secuencias de error de entrenamiento y generalización deben tener el mismo tamaño.")

    return



  balance_point = np.array(generalization_error).argmin() + 1

  plt.figure(figsize = (8, 5), dpi = 105)



  plt.plot(range(1, n + 1), train_error, label="Entrenamiento")

  plt.plot(range(1, n + 1), generalization_error, label="Generalización")

  plt.xticks(range(0, n + 1, 2))

  plt.xlabel("Profundidad máxima")

  plt.ylabel("Error")

  y_min, y_max = plt.gca().get_ylim() 

  plt.vlines(balance_point, y_min, y_max, colors = ['red'], linestyles = ['dashdot'])

  plt.ylim([y_min, y_max])

  plt.text(balance_point + 1, 0.165, 'Punto de balance')

  plt.legend();



#Función para generar la función de predicción de un clasificador entrenado previamente.

def gen_pred_fun(clf):

    def pred_fun(x1, x2):

        x = np.array([[x1, x2]])

        return clf.predict(x)[0]

    return pred_fun
