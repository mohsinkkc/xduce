import pandas as pd
import os

def process_payroll(payroll_file, employee_data):
    salaries = {}

    with open(payroll_file, 'r') as file:
        for line in file:
            emp_code, work_days = line.strip().split(',')
            work_days = int(work_days)
            if emp_code in employee_data:
                base_wage = employee_data[emp_code][base_wage]
                salary = base_wage * work_days
                salaries[emp_code] = salary
            else:
                print(f"Employee with code {emp_code} not found in the employee data.")

    return salaries

def save_salary_data(salaries, output_file):
    with open(output_file, 'w') as file:
        for emp_code, salary in salaries.items():
            file.write(f"{emp_code},{salary}\n")

def process_employee_data(employee_excel_file):
    
    employee_data = pd.read_excel(employee_excel_file)

   
    employee_base_wages = {
        'EMP001': 20,
        'EMP002': 25,
        'EMP003': 30
    }

    
    employee_data['base_wage'] = employee_data['emp_code'].map(employee_base_wages)
    employee_data['salary'] = employee_data['base_wage'] * employee_data['work_days']  

    return employee_data

        
def main():
    
    employee_data = {
        'EMP001': {'base_wage': 20},
        'EMP002': {'base_wage': 25},
        'EMP003': {'base_wage': 30}
    }
    payroll_file = "payroll.txt"
    salaries = process_payroll(payroll_file, employee_data)
    save_salary_data(salaries, "salaries.txt")
    
    employee_excel_file = "ActiveEmployeeData.xlsx"    
    processed_employee_data = process_employee_data(employee_excel_file)
    print(processed_employee_data)
    
if __name__ == "__main__":
    main()