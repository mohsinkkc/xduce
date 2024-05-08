import pandas as pd
import os

def process_payroll(payroll_file, employee_data):
   salaries = {}
   pending_employees = {}
   with open(payroll_file, 'r') as file:
        for line in file:
            parts = line.strip().split(" ")
            if len(parts) >= 2:
                emp_code = parts[0]
                work_days = int(parts[1])
                employee = employee_data.get(emp_code)
                print(line,"10")
                if employee:
                    base_wage = employee['base_wage']
                    salary = work_days * base_wage
                    salaries.append({'emp_code': emp_code, 'salary': salary})
                else:
                    pending_employees.append(emp_code)
            else:
                print(f"lines are : {line}")

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
    employee_data['salary'] = employee_data['base_wage0'] * employee_data['work_days']  

    return employee_data

        
def main():
    
    employee_data = {
        'EMP001': {'base_wage': 20},
        'EMP002': {'base_wage': 25},
        'EMP003': {'base_wage': 30}
    }
    payroll_file ='payroll.txt'
    print(payroll_file, "payroll_file 49")
    salaries = process_payroll(payroll_file, employee_data)
    save_salary_data(salaries,"salaries.txt") 
    
    employee_excel_file = "ActiveEmployeeData.xlsx"    
    processed_employee_data = process_employee_data(employee_excel_file)
    print(processed_employee_data)
    
if __name__ == "__main__":
    main()