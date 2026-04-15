import numpy as np
import pandas as pd

def mean_array(arr):
    """Calculate mean ignoring NaN values"""
    return np.nanmean(arr)

def min_max(arr):
    """Return min and max ignoring NaN values"""
    return np.nanmin(arr), np.nanmax(arr)

def get_column(df, column_name):
    """Extract specific column from DataFrame"""
    return df[column_name]

def clean_data(df):
    """Remove students with all missing grades"""
    grade_cols = ['algebra', 'python', 'ab']
    return df.dropna(subset=grade_cols, how='all')

def calculate_average(row):
    """Calculate average of available subjects for a student"""
    grades = [row['algebra'], row['python'], row['ab']]
    valid_grades = [g for g in grades if pd.notna(g)]
    return np.mean(valid_grades) if valid_grades else np.nan

def find_best_student(df, subject):
    """Find best student in specific subject"""
    valid_data = df.dropna(subset=[subject])
    if valid_data.empty:
        return None, None
    best_idx = valid_data[subject].idxmax()
    return valid_data.loc[best_idx, 'name'], valid_data.loc[best_idx, subject]
