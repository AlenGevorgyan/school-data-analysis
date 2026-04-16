import matplotlib.pyplot as plt
import numpy as np
from src.data_loader import load_all_data
from src.analysis import mean_array

def compare_grades(data):
    subjects = ['algebra', 'python', 'ab']
    names = ['Հանրահաշիվ', 'Python', 'ԱԲ']
    
    g11 = [mean_array(data['11'][s]) if data['11'] is not None and s in data['11'].columns else 0 for s in subjects]
    g12 = [mean_array(data['12'][s]) if data['12'] is not None and s in data['12'].columns else 0 for s in subjects]
    
    x = np.arange(len(names))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, g11, width, label='11-rd', color='green')
    ax.bar(x + width/2, g12, width, label='12-rd', color='blue')
    
    ax.set_ylabel('Միջին միավոր')
    ax.set_title('Դասարանների համեմատում')
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.savefig('comparison.png')
    print("Grafiky pahpanvel e comparison.png")

if __name__ == "__main__":
    data = load_all_data('data/raw/students.xlsx')
    compare_grades(data)