import pandas as pd
import numpy as np
from utils.generic import mean_array, min_max, get_column, clean_data, calculate_average, find_best_student
from utils.data_loader import load_all_grades

def analyze_grade(df, grade_name):
    print(f"\n{'='*50}")
    print(f"AB {grade_name} dasarani verlutsutyun")
    print(f"{'='*50}")
    
    df_clean = clean_data(df)
    df_clean['average'] = df_clean.apply(calculate_average, axis=1)
    
    print(f"Ashakertneri qanak: {len(df_clean)}")
    
    subjects = {
        'algebra': 'Hanrahashiv',
        'python': 'Python', 
        'ab': 'AB'
    }
    
    print(f"\nMijin baler yst ararkaneri:")
    for subj, name in subjects.items():
        col = get_column(df_clean, subj)
        if not col.dropna().empty:
            mean_val = mean_array(col)
            min_val, max_val = min_max(col)
            print(f"  {name:12} | Mijin: {mean_val:5.1f} | Min: {min_val:5.1f} | Max: {max_val:5.1f}")
    
    print(f"\nLavaguyn ashakertner yst ararkaneri:")
    for subj, name in subjects.items():
        student, score = find_best_student(df_clean, subj)
        if student:
            print(f"  {name:12} | {student:25} | {score:5.1f}")
    
    valid_avg = df_clean.dropna(subset=['average'])
    if not valid_avg.empty:
        best_idx = valid_avg['average'].idxmax()
        best_student = valid_avg.loc[best_idx]
        print(f"\nLavaguyn ashakert ynterq mijinov:")
        print(f"   {best_student['name']} | Mijin: {best_student['average']:.2f}")
    
    return df_clean

def main():
    print("Vanadzori Eureka dprots - AB Serundi Verlutsutyun")
    
    try:
        grades = load_all_grades('data/students.xlsx')
        
        if grades.get('11') is not None:
            analyze_grade(grades['11'], "11-rd")
        
        if grades.get('12') is not None:
            analyze_grade(grades['12'], "12-rd")
            
    except FileNotFoundError:
        print("Error: Excel file not found in data/ folder")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()