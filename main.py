from src.data_loader import load_all_data
from src.analysis import mean_array, min_max, clean_data, student_average, find_top_student

def analyze(df, grade_name):
    print(f"\nAB {grade_name} dasaran")
    print("-" * 40)
    
    df = clean_data(df)
    df['avg'] = df.apply(student_average, axis=1)
    
    print(f"Ashakertner: {len(df)}")
    
    for subj, name in [('algebra', 'Hanrahashiv'), ('python', 'Python'), ('ab', 'AB')]:
        col = df[subj]
        if not col.dropna().empty:
            m = mean_array(col)
            mn, mx = min_max(col)
            print(f"{name}: mijin={m:.1f}, min={mn}, max={mx}")
    
    print("\nLavaguynner:")
    for subj, name in [('algebra', 'Hanrahashiv'), ('python', 'Python'), ('ab', 'AB')]:
        student, score = find_top_student(df, subj)
        if student:
            print(f"  {name}: {student} ({score})")
    
    best = df.loc[df['avg'].idxmax()]
    print(f"\nLavaguyn ynterq: {best['name']} ({best['avg']:.1f})")
    
    return df

if __name__ == "__main__":
    data = load_all_data('data/data.xlsx')
    if data['11'] is not None:
        analyze(data['11'], "11-rd")
    if data['12'] is not None:
        analyze(data['12'], "12-rd")