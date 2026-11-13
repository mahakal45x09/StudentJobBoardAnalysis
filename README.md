# Student Job Board Analysis

## Project Overview
This project analyses student job applications from July to September 2026. The objective is to identify effective application sources, understand shortlist patterns, and compare employer response times for paid and unpaid jobs.

## Dataset
- Original applications: 1,206
- Cleaned applications: 1,200
- Duplicate application IDs removed: 6
- Total columns: 11

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib

## Analysis Performed
1. Data inspection and cleaning.
2. Overall hiring performance by application source.
3. Role-wise source performance.
4. Shortlist rate by application completion.
5. Paid versus unpaid employer response analysis.
6. Data visualization.

## Key Findings
- Referrals generated 10.74 hires per 100 applications overall.
- Applicants completing all four steps had a 48.39% shortlist rate.
- Applicants completing fewer than four steps had a 9.28% shortlist rate.
- Paid jobs had a median response time of 3 days.
- Unpaid jobs had a median response time of 7 days.

## Recommendations
- Use recruitment sources according to job role.
- Encourage applicants to complete all application steps.
- Encourage employers to respond to applications faster.
- Monitor employer response times.

## Project Files
- main.py
- data_inspection.py
- data_cleaning.py
- source_analysis.py
- role_source_analysis.py
- step_completion_analysis.py
- paid_unpaid_analysis.py
- create_chart.py
- job-board-applications.csv
- cleaned_applications.csv
- source_analysis.csv
- role_source_analysis.csv
- best_source_by_role.csv
- step_completion_analysis.csv
- paid_unpaid_analysis.csv
- shortlist_rate_by_steps.png
- manager_note.txt
- requirements.txt

## How to Run

### 1. Create virtual environment
python -m venv venv

### 2. Activate environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run analysis
python data_inspection.py
python data_cleaning.py
python source_analysis.py
python role_source_analysis.py
python step_completion_analysis.py
python paid_unpaid_analysis.py
python create_chart.py

## Conclusion
This project provides insights into recruitment source performance, application completion, and employer response behaviour. These findings can help improve the student job application experience.
