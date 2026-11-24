# University-scholarship
# University Scholarship Allocation System

## Project Overview

The **University Scholarship Allocation System** is a Python-based application designed to evaluate university students for scholarship eligibility.

The system checks students' aggregate marks, subject-wise minimum scores, attendance percentage, and annual family income. It identifies eligible students, ranks them according to their academic performance, and resolves ties using predefined rules.

## Objectives

- To evaluate students based on academic performance.
- To check minimum subject-wise marks.
- To verify attendance eligibility.
- To check annual family income criteria.
- To identify eligible and rejected applicants.
- To rank eligible students based on aggregate marks.
- To resolve ranking ties using predefined conditions.

## Eligibility Criteria

| Criteria | Requirement |
|---|---|
| Number of subjects | 5 |
| Minimum subject marks | 40 |
| Minimum attendance | 75% |
| Maximum annual family income | ₹2,50,000 |

## Ranking Rules

Eligible students are ranked using the following rules:

1. Higher aggregate percentage receives a higher rank.
2. If aggregate percentages are equal, higher attendance receives priority.
3. If attendance is also equal, lower annual family income receives priority.
4. If all the above criteria are equal, alphabetical order of names determines the rank.

## Technologies Used

- Programming Language: Python
- Platform: Visual Studio Code
- Version Control: Git
- Repository Hosting: GitHub

## Python Concepts Used

- Variables and data types
- Input and output statements
- Lists and dictionaries
- For loops
- If-else statements
- Functions
- Sorting
- Conditional checking

## Algorithm

1. Start the program.
2. Read the number of scholarship applicants.
3. Collect each applicant's name.
4. Enter marks for five subjects.
5. Enter attendance percentage and annual family income.
6. Calculate total marks and aggregate percentage.
7. Check subject-wise minimum marks.
8. Check attendance and income eligibility.
9. Separate eligible and rejected applicants.
10. Sort eligible applicants according to aggregate marks.
11. Apply tie-breaking rules wherever necessary.
12. Display the scholarship ranking list.
13. Display rejected applicants with their rejection reasons.
14. Display the total number of eligible and rejected applicants.
15. Stop the program.

## Pseudocode

```text
START

INPUT number of applicants

FOR each applicant:
    INPUT name
    INPUT marks of five subjects
    INPUT attendance
    INPUT annual family income

    CALCULATE total marks
    CALCULATE aggregate percentage

    IF every subject mark >= 40
       AND attendance >= 75
       AND income <= 250000:

        ADD applicant to eligible list

    ELSE:
        ADD applicant to rejected list
        STORE rejection reasons

SORT eligible applicants BY:
    Aggregate percentage (descending)
    Attendance (descending)
    Income (ascending)
    Name (alphabetical)

DISPLAY eligible applicants with ranks
DISPLAY rejected applicants and reasons
DISPLAY summary

STOP
```

## Test Cases

| Test Case | Aggregate | Attendance | Income | Expected Result |
|---|---:|---:|---:|---|
| 1 | 90% | 90% | ₹1,50,000 | Eligible |
| 2 | 90% | 95% | ₹1,80,000 | Eligible |
| 3 | 85% | 80% | ₹2,00,000 | Eligible |
| 4 | 92% | 85% | ₹3,00,000 | Rejected |
| 5 | 80% | 70% | ₹1,00,000 | Rejected |

## Sample Output

```text
========== SCHOLARSHIP RANK LIST ==========

Rank: 1
Name: Banu
Total Marks: 450.0 / 500
Aggregate: 90.0 %
Attendance: 95.0 %
Annual Income: Rs. 180000

Rank: 2
Name: Arun
Total Marks: 450.0 / 500
Aggregate: 90.0 %
Attendance: 90.0 %
Annual Income: Rs. 150000

Rank: 3
Name: Charan
Total Marks: 425.0 / 500
Aggregate: 85.0 %
Attendance: 80.0 %
Annual Income: Rs. 200000

========== SUMMARY ==========

Total Applicants: 5
Eligible Applicants: 3
Rejected Applicants: 2
```

## Conclusion

The University Scholarship Allocation System provides a simple and efficient way to evaluate scholarship applicants using Python.

It reduces manual work by automatically checking eligibility conditions, calculating aggregate percentages, ranking eligible students, and identifying rejected applicants with their reasons.

This project demonstrates the practical application of Python programming concepts to solve a real-world university scholarship allocation problem.

## Project Structure

```text
University-Scholarship-Allocation/
│
├── scholarship_allocation.py
├── README.md
└── screenshots/
    └── output.png
```

## Author Details

- **Name:** Your Name
- **Roll Number:** Your Roll Number
- **Branch:** Your Branch
- **Section:** Your Section
- **Project:** Python Activity-Based Learning
