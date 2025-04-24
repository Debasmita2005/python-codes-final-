# Create a dictionary with department number, employee roll number, and salary
employee_data = {
    101: {'dept': 'HR', 'salary': 45000},
    102: {'dept': 'IT', 'salary': 55000},
    103: {'dept': 'HR', 'salary': 48000},
    104: {'dept': 'IT', 'salary': 60000},
    105: {'dept': 'Finance', 'salary': 65000},
    106: {'dept': 'IT', 'salary': 48000},
    107: {'dept': 'Finance', 'salary': 70000},
    108: {'dept': 'HR', 'salary': 42000}
}

# Dictionary to store department-wise salary lists
dept_salaries = {}

# Group salaries by department
for emp_id, details in employee_data.items():
    dept = details['dept']
    salary = details['salary']
    
    # Add department to dict if not present
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    
    # Add salary to department's list
    dept_salaries[dept].append(salary)

# Find min and max salary for each department
print("Department-wise Salary Analysis:")
print("-" * 40)
print(f"{'Department':<10} {'Minimum Salary':<15} {'Maximum Salary':<15}")
print("-" * 40)

for dept, salaries in dept_salaries.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    print(f"{dept:<10} ${min_salary:<14} ${max_salary:<14}")
