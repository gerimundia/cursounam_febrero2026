# -*- coding: utf-8 -*-
"""
Razones y proporciones
"""

# Paquetes
import os
import pandas as pd
from joblib import dump, load
"""
import numpy as np
import statistics as sta
import matplotlib.pyplot as plt
import seaborn as sns
"""


# Directorio de trabajo
os.chdir("C:/taller_demografia1/")
os.getcwd()


# Datos
df = pd.read_excel(
    "Semana2/cpv2020_b_ags_01_poblacion.xlsx",
    sheet_name="03",
    usecols="A:F",
    skiprows=9,
    nrows=102,
    header=None
)

df.info()
df.describe()
df.head(2)
df.tail(2)

df = df.drop(df.columns[1], axis=1)

df.columns = ["entidad", "edad_txt", "total", "hombres", "mujeres"]

df['edad'] = list(range(0, 101)) + [999]


# Razón de masculinidad
pobtotal = df["total"].sum()
hombrestotal = df["hombres"].sum()
mujerestotal = df["mujeres"].sum()

razonmasculinidad = hombrestotal / mujerestotal


# Proporción de personas de 65+ con respecto al total
pob65ymas = df.loc[65:100, "total"].sum()
prop_pob65ymas = pob65ymas / pobtotal


# Guardando objetos
dump({'df': df, 'pobtotal': pobtotal,
      'hombrestotal': hombrestotal, 'mujerestotal': mujerestotal},
     "datos_aguascalientes.joblib")
