# AI-Assisted Test Failure Grouping

## Overview
This is a **student project** that shows how automated test failures can be collected,
stored, and grouped using simple AI techniques.

The project helps reduce the time spent manually reviewing test failures by grouping
similar errors together.

---

## Problem
When automated tests run, they can produce many failures.
Often, several failures are caused by the same issue, but they still need to be checked one by one.

This makes test analysis slow and repetitive.

---

## Solution
This project provides a simple solution by:

- running automated tests with `pytest`
- collecting failed test results
- storing failures in a SQLite database
- grouping similar error messages using basic machine learning

This allows similar failures to be reviewed together instead of individually.

---

## How It Works
1. Automated tests are executed using `pytest`
2. Test results are saved in JUnit XML format
3. Failed tests are extracted from the results
4. Failure data is stored in a SQLite database
5. Error messages are grouped based on text similarity
6. Grouping results are saved for further analysis

---

## Technologies Used
- Python
- pytest
- SQLite
- scikit-learn
- Git & GitHub

### How to Run the Project

1. install the required Python dependencies using the requirements file.  
2. run the automated tests to generate a test results XML file.  
3. execute the script that reads the test results and stores failed tests in a SQLite database.  
4. run the grouping script to analyze and group similar test failures.

```bash
pip install -r requirements.txt
pytest --junitxml=results.xml
python -m scripts.read_results
python -m scripts.group_failures
