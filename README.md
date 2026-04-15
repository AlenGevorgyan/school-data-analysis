# School Data Analysis

Vanadzori Eureka dprots AB serundi ashakertneri tvayleri verlutsutyun.

## Team Members

| Anun | Patkerastvacutyun | Nakhagic
|------|-------------------|----------
| Argam | Data infrastructure, Excel loading, NumPy utilities | src/data_loader.py, src/analysis.py
| Alen | Core analysis logic, main program | main.py
| Samo | Data visualization, documentation | visualize.py, README.md

## Project Structure

```
school-data-analysis/
├── data/
│   └── raw/                  # Excel files (do not commit)
│       └── students.xlsx
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # Excel sheet reading
│   └── analysis.py           # NumPy statistical functions
├── main.py                   # Main analysis script
├── visualize.py              # Matplotlib charts
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md                 # This file
```

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the Excel file in `data/raw/students.xlsx`.

## Usage

Run analysis:

```bash
python main.py
```

Generate charts:

```bash
python visualize.py
```

## Features

- Load 11th and 12th grade data from Excel sheets
- Calculate mean, min, max for Algebra, Python, AB subjects
- Identify top performing students per subject
- Handle missing data (NaN values)
- Generate comparison bar charts between grades

## Data Description

- **11th grade**: 23 students, complete records
- **12th grade**: 23 students, partial missing values
- **Subjects**: Hanrahashiv (Algebra), Python, AB (Algorithms)

## Git Workflow

Branches:
- `main` - Stable code
- `argam/data-infrastructure` - Data loading infrastructure
- `alen/analysis-engine` - Analysis engine
- `samo/visualization` - Visualization and docs
