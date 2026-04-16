import numpy as np
import pandas as pd

def mean_array(arr):
    if arr.dropna().empty:
        return 0
    return np.nanmean(arr)

def min_max(arr):
    if arr.dropna().empty:
        return 0, 0
    return np.nanmin(arr), np.nanmax(arr)

def clean_data(df):
    grade_cols = [c for c in ['algebra', 'python', 'ab'] if c in df.columns]
    if not grade_cols:
        return df
    return df.dropna(subset=grade_cols, how='all')

def student_average(row):
    grades = []
    for c in ['algebra', 'python', 'ab']:
        if c in row and pd.notna(row[c]):
            grades.append(row[c])
    return np.mean(grades) if grades else np.nan

def find_top_student(df, subject):
    if subject not in df.columns:
        return None, None
    valid = df.dropna(subset=[subject])
    if valid.empty:
        return None, None
    idx = valid[subject].idxmax()
    return valid.loc[idx, 'name'], valid.loc[idx, subject]