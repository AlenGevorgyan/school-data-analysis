from src.data_loader import load_all_data
from src.analysis import mean_array, min_max, clean_data, student_average, find_top_student

def analyze(df, grade_name):
    if df is None:
        print(f"No data for {grade_name}")
        return None
    
    print(f"\nAB {grade_name} dasaran")
    print("-" * 40)
    print(f"Columns: {df.columns.tolist()}")
    
    df = clean_data(df)
    if df.empty:
        print("No valid data after cleaning")
        return None
    
    df['avg'] = df.apply(student_average, axis=1)
    
    print(f"Ashakertner: {len(df)}")
    
    subjects = [('algebra', 'Hanrahashiv'), ('python', 'Python'), ('ab', 'AB')]
    
    for subj, name in subjects:
        if subj not in df.columns:
            continue
        col = df[subj]
        if col.dropna().empty:
            continue
        m = mean_array(col)
        mn, mx = min_max(col)
        print(f"{name}: mijin={m:.1f}, min={mn}, max={mx}")
    
    print("\nLavaguynner:")
    for subj, name in subjects:
        student, score = find_top_student(df, subj)
        if student:
            print(f"  {name}: {student} ({score})")
    
    if not df['avg'].dropna().empty:
        best = df.loc[df['avg'].idxmax()]
        print(f"\nLavaguyn ynterq: {best['name']} ({best['avg']:.1f})")
    
    return df

if __name__ == "__main__":
    data = load_all_data('data/raw/students.xlsx')
    if data.get('11') is not None:
        analyze(data['11'], "11-rd")
    if data.get('12') is not None:
        analyze(data['12'], "12-rd")