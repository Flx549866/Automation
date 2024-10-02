#!/usr/bin/env python3

import csv

# Register the dialect
csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

def read_employees(csv_file_location):
    employee_list = []
    with open(csv_file_location, mode='r') as file:
        employee_file = csv.DictReader(file, dialect='empDialect')
        for data in employee_file:
            employee_list.append(dict(data))
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    
    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()

# Test the functions
if __name__ == "__main__":
    csv_file_location = '/home/student/data/employees.csv'  # Replace with the actual path to your employees.csv file
    employee_list = read_employees(csv_file_location)
    dictionary = process_data(employee_list)
    print("Department Data:")
    print(dictionary)
    report_file = '/home/student/data/report.txt'  # Replace with the desired path for the report file
    write_report(dictionary, report_file)
    print("\nReport has been written to", report_file)
