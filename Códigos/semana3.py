# -*- coding: utf-8 -*-
"""
Pirámides de población ∙ Declaración de edad ∙ Razones de sexo
"""

# Paquetes
import os
import pandas as pd
from joblib import dump, load
import numpy as np
import matplotlib.pyplot as plt

# Directorio de trabajo
os.chdir("C:/taller_demografia1/")
os.getcwd()


# Datos
globals().update(load("datos_aguascalientes.joblib"))


# Población por edades quinquenales

bins = list(np.arange(0, 85, 5)) + [101]

labels = ([f"{i}-{i+4}" for i in range(0, 80, 5)] + ["80+"])

df['edad_5y'] = pd.cut(
    df['edad'],
    bins=bins,
    right=False,
    labels=labels
)

poblacion_edad_5y = (
    df
    .groupby('edad_5y', observed=False)
    .agg(hombres_edad_5y=('hombres', 'sum'),
         mujeres_edad_5y=('mujeres', 'sum')))

poblacion_edad_5y.head(5)
poblacion_edad_5y.tail(5)

# Asignacion de edad NA

ne_hombres = 749
ne_mujeres = 759

poblacion_edad_5y['hombres_edad_5y_total'] = (
    poblacion_edad_5y['hombres_edad_5y'] +
    ne_hombres * (
        poblacion_edad_5y['hombres_edad_5y'] /
        (poblacion_edad_5y['hombres_edad_5y'].sum())
    )
)

poblacion_edad_5y['mujeres_edad_5y_total'] = (
    poblacion_edad_5y['mujeres_edad_5y'] +
    ne_mujeres * (
        poblacion_edad_5y['mujeres_edad_5y'] /
        (poblacion_edad_5y['mujeres_edad_5y'].sum())
    )
)

# Verificando:
pobtotal == (
    poblacion_edad_5y['hombres_edad_5y_total'].sum() +
    poblacion_edad_5y['mujeres_edad_5y_total'].sum())


# Razón de sexo por grupo de edad

poblacion_edad_5y['razonsexo'] = (
    poblacion_edad_5y['hombres_edad_5y_total'] / poblacion_edad_5y['mujeres_edad_5y_total'] * 100)

poblacion_edad_5y.plot(
    y="razonsexo",
    kind="line")

plt.xlabel("Grupo de edad")
plt.ylabel("Razón de sexo")
plt.legend().remove()

plt.show()


# Pirámide de población

poblacion_edad_5y['porc_hombres'] = (
    poblacion_edad_5y['hombres_edad_5y_total'] / -pobtotal)

poblacion_edad_5y['porc_mujeres'] = (
    poblacion_edad_5y['mujeres_edad_5y_total'] / pobtotal)

poblacion_edad_5y['edad'] = labels

plt.barh(poblacion_edad_5y["edad"], poblacion_edad_5y["porc_hombres"], label="Hombres")
plt.barh(poblacion_edad_5y["edad"], poblacion_edad_5y["porc_mujeres"], label="Mujeres")
plt.xlabel("Población")
plt.ylabel("Edad")
plt.title("Pirámide de población")
plt.legend()
plt.show()


# Pirámide de población por edades simples
df['hombres2'] = (df['hombres'] * -1)

plt.barh(
    df.loc[df["edad"] <= 100, "edad"], df.loc[df["edad"] <= 100, "hombres2"], label="Hombres")
plt.barh(
    df.loc[df["edad"] <= 100, "edad"], df.loc[df["edad"] <= 100, "mujeres"], label="Mujeres")
plt.xlabel("Población")
plt.ylabel("Edad")
plt.title("Pirámide de población")
plt.legend()
plt.show()
