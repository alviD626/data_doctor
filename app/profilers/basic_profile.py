import pandas as pd


def get_numeric_columns(df:pd.DataFrame) -> list[str]:
    numeric_df =  df.select_dtypes(
        include="number"
    )

    if numeric_df.empty:
        return {}
    return numeric_df.describe().to_dict()

def get_categorical_columns(df:pd.DataFrame) -> list[str]:
    categorical_df = df.select_dtypes(
        include=["object", "category"]
    )
    if categorical_df.empty:
        return {}
    
    return categorical_df.columns.tolist()

def get_basic_profile(df:pd.DataFrame) -> dict:
    profile = {
        "rows": len(df),

        "columns": len(df.columns),

        "cells": df.size,
        
        "column_names": df.columns.tolist(),
        
        "data_types":{
            column : str(dtype)
            for column, dtype in df.dtypes.items()
        },
        
        "unique_columns": {
            column: df[column].nunique()
            for column in df.columns
        },
        
        "numeric_columns": get_numeric_columns(df),
        
        "categorical_columns": get_categorical_columns(df),
        
        "memory_usage": int(
            df.memory_usage(deep=True).sum()
        )
    }

    return profile
