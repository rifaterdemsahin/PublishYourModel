"""
ETL Transform Module
This module handles data transformation operations.
"""

import pandas as pd
from typing import List, Callable


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the data by removing duplicates and handling missing values.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    print(f"Cleaning data - initial rows: {len(df)}")
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna('')
    
    print(f"Cleaning data - final rows: {len(df)}")
    return df


def normalize_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Normalize specified columns to lowercase and strip whitespace.
    
    Args:
        df: Input DataFrame
        columns: List of column names to normalize
        
    Returns:
        DataFrame with normalized columns
    """
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    
    print(f"Normalized columns: {columns}")
    return df


def apply_transformation(df: pd.DataFrame, transform_func: Callable) -> pd.DataFrame:
    """
    Apply a custom transformation function to the DataFrame.
    
    Args:
        df: Input DataFrame
        transform_func: Transformation function to apply
        
    Returns:
        Transformed DataFrame
    """
    print("Applying custom transformation")
    return transform_func(df)


if __name__ == "__main__":
    print("Transform module - ready for data transformation")
