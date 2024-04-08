import pandas as pd

# Step 1: Read employee data from Excel
def read_employee_data(filename):
    return pd.read_excel(filename)


def parse_payroll_file(filename):
    payroll_data = {}
    with open(filename, 'r') as file:
        for line in file:
            emp_code, work_days = line.strip().split(',')
            payroll_data[emp_code] = int(work_days)
    return payroll_data

# Step 3: Calculate salary
def calculate_salary(employee_data, payroll_data):
    for index, row in employee_data.iterrows():
        emp_code = row['emp_code']
        if emp_code in payroll_data:
            working_days = payroll_data[emp_code]
            base_wage = row['base_wage']  # Assuming 'base_wage' column exists
            salary = base_wage * working_days
            employee_data.at[index, 'salary'] = salary

# Step 4: Write back to Excel
def write_to_excel(employee_data, filename):
    employee_data.to_excel(filename, index=False)

def main():
    # Input filenames
    employee_filename = 'ActiveEmployeeData.xlsx'
    payroll_filename = 'payroll.txt'

    # Read employee data from Excel
    employee_data = read_employee_data(employee_filename)

    # Parse payroll file
    payroll_data = parse_payroll_file(payroll_filename)

    # Calculate salary
    calculate_salary(employee_data, payroll_data)

    # Write back to Excel
    write_to_excel(employee_data, employee_filename)

if __name__ == "__main__":
    main()