import pandas as pd

def load_grade_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
    column_mapping = {
        'Աշակերտի անուն, ազգանուն, հայրանուն': 'name',
        'Հանրահաշվի քննության արդյունքներ (04.06.2025)': 'algebra',
        'Python-ի քննության արդյունքներ (11.06.2025)': 'python',
        'ԱԲ քննության արդյունքներ (18.06.2025)': 'ab'
    }
    
    df = df.rename(columns=column_mapping)
    
    df = df[['name', 'algebra', 'python', 'ab']]
    
    return df

def load_all_grades(file_path):
    grades = {}
    
    try:
        grades['11'] = load_grade_data(file_path, 'ԱԲ 11րդ դասարան_2024')
    except Exception as e:
        print(f"Could not load 11th grade: {e}")
        grades['11'] = None
    
    try:
        grades['12'] = load_grade_data(file_path, 'ԱԲ 12րդ դասարան_2023')
    except Exception as e:
        print(f"Could not load 12th grade: {e}")
        grades['12'] = None
    
    return grades
