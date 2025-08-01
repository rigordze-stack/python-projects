# Importamos panda para manipulacion de dataFrames
import pandas as pd
import numpy as np # numpy para operaciones numericas z-score

def fill_nulls(df, strategy='mean'):
    """
    Rellena valores nulos en cada columna numerica
    strategy: mean, median, zero 
    """
    # Copiamos el dataFrame para no mutar el original
    df_clean = df.copy()
    
    for col in df_clean.select_dtypes(include='number').columns:
        # Calcula valor de reemplazo según estrategia
        if strategy == 'mean':
            fill_val = df_clean[col].mean()
        elif strategy == 'median':
            fill_val = df_clean[col].median()
        else:
            fill_val = 0
        
        # Rellena nulos en la columna
        df_clean[col] = df_clean[col].fillna(fill_val)
    return df_clean

def detect_outliers_zscore(df, column, threshold = 3.0):
    """
    Devuelve un dataFrame con las filas que exceden el zscore dado
    threshold: numero de desviaciones estandar
    """
    # Calcula zscore de la columna
    col = df[column]
    z = np.abs((col - col.mean()) / col.std())
    # Filtra las filas con zscore al umbral
    return df[z > threshold]

def pivot_data(df, index, columns, values):
    """
    Realiza un pivot simple de un dataFrame
    """
    return df.pivot(index=index, columns=columns, values=values)

def melt_data(df, id_vars, value_vars, var_name='variable',value_name='value'):
    """
    Convierte de formato ancho a largo (melt)
    """
    return df.melt(id_vars=id_vars,value_vars=value_vars,
                    var_name=var_name,value_name=value_name)
    
def merge_data(df1,df2,on,how='inner'):
    """
    Une dos dataFrame por la clave 'on con el metodo 'how'
    """
    return pd.merge(df1,df2,on=on,how=how)

def normalize_column(df,column):
    """
    Normaliza los valores de una columna numerica a rango [0,1]
    """
    col = df[column].astype(float)
    norm=(col-col.min()) / (col.max() - col.min())
    df_norm = df.copy()
    df_norm[column] = norm
    return df_norm

