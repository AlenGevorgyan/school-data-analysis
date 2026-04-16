import pandas as pd

def load_grade_data(file_path, sheet_name):
    # Read without header first
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    print(f"Raw shape: {df.shape}")
    print(f"First 5 rows:\n{df.head()}")
    
    # Find the row with 'Աշակերտի անուն' (header row)
    header_row = None
    for idx, row in df.iterrows():
        for cell in row:
            if isinstance(cell, str) and 'անուն' in cell:
                header_row = idx
                break
        if header_row is not None:
            break
    
    if header_row is None:
        raise ValueError("Could not find header row")
    
    print(f"Header found at row {header_row}")
    
    # Re-read with correct header
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row)
    df.columns = df.columns.str.strip()
    
    # Map columns
    mapping = {}
    for col in df.columns:
        s = str(col)
        if 'անուն' in s:
            mapping[col] = 'name'
        elif 'Հանրահաշվի' in s:
            mapping[col] = 'algebra'
        elif 'Python' in s:
            mapping[col] = 'python'
        elif 'ԱԲ' in s and 'քննության' in s:
            mapping[col] = 'ab'
    
    df = df.rename(columns=mapping)
    
    # Remove header duplicates and empty rows
    df = df[df['name'].notna()]
    df = df[df['name'] != 'Աշակերտի անուն, ազգանուն, հայրանուն']
    
    return df[['name', 'algebra', 'python', 'ab']]

def load_all_data(file_path):
    return {
        '11': load_grade_data(file_path, 'ԱԲ 11րդ դասարան_2024'),
        '12': load_grade_data(file_path, 'ԱԲ 12րդ դասարան_2023')
    }