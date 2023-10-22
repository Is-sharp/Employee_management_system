num_of_employees = 0  #initializes the number of employees to 0
employees = dict()  #creates an empty dictionary that will be used to store employees later 

def new_employees():  #this method adds as many employees as the user needs, but wipes all previously added employees
    global num_of_employees, employees

    #resets the employee count and employees
    employees.clear()
    num_of_employees = 0

    num_of_employees = int(input("Please enter the number of employees you want to add: "))
    
    #iterates num_of_employees times and maps a unique employee id as a key to a list containing employee information
    for x in range(num_of_employees):
        employee_id = int(input("Enter the ID of employee: "))
        name = input("Enter the name of employee: ")
        hours_worked = int(input("Enter the hours worked for the employee: "))
        hourly_rate = float(input("Enter the hourly rate for the employee: "))

        employees[employee_id] = [name, hours_worked, hourly_rate]

def add_employee():
    global num_of_employees, employees

    employee_id = int(input("Enter the ID of employee: "))
    name = input("Enter the name of employee: ")
    hours_worked = int(input("Enter the hours worked for the employee: "))
    hourly_rate = float(input("Enter the hourly rate for the employee: "))

    employees[employee_id] = [name, hours_worked, hourly_rate]
    num_of_employees += 1

def view_employees(): 
    if num_of_employees == 0:
        print("No employee exists yet")
    else:
        for key, value in employees.items():  #loops over each key, value pair and prints the information
            print(f"Employee ID: {key} \nEmployee Name: {value[0]}")
            print(f"Employee Hours Worked: {value[1]} \nEmployee Hourly Rate: ${value[2]}", end = "\n")
    
def calculate_payroll(): #calculates payroll for employee with ID passed to the function
    if num_of_employees == 0:
        print("No Employee exists yet\n")
        return
    keep_calculating = 'y'

    while keep_calculating.lower() == 'y': #keeps calculating as many as the user wants
        employee_id = int(input("Enter ID of employee to calculate: "))

        if employee_id not in employees:
            print(f"The Employee with ID {employee_id} does not exist.")

        else:
            tax_rate = float(input(f"Enter the tax rate for {employees[employee_id][0]} as a number: "))
            while tax_rate < 0 or tax_rate > 100:
                tax_rate = float(input(f"Error. Enter the tax rate for {employees[employee_id][0]} as a positive number not greater than 100): "))
            
            benefit_amount = float(input(f"Enter benefits for {employees[employee_id][0]} as a number: "))
            while benefit_amount < 0:
                benefit_amount = float(input(f"Error. Enter benefits for {employees[employee_id][0]} as a positive number: \n"))
            
            gross_salary = employees[employee_id][1]*employees[employee_id][2]

            tax_deduction = gross_salary*(tax_rate/100)
            net_salary = gross_salary-tax_deduction+benefit_amount

            print(f"\nEmployee Name: {employees[employee_id][0]}\nEmployee ID: {employee_id}\nEmployee Gross Salary: ${gross_salary:.2f}\n" +
                    f"Employee Tax Deduction: ${tax_deduction:.2f}\nEmployee Benefit Amount: ${benefit_amount}\nEmployee Net Salary: ${net_salary:.2f}\n")
        
        keep_calculating = input("Would you like to calculate payroll for another Employee? (y/n)  ")
        
    
def delete_employee(): #deletes an employee with the id passed as an argument
    global employees
    
    keep_deleting = 'y'

    while keep_deleting.lower() == 'y':
        employee_id = int(input("Enter ID of Employee to delete: "))
        if employee_id not in employees:
            print("That Employee does not exist. ")
        else:
            del employees[employee_id]
            print(f"Employee with ID {employee_id} deleted successfully.")
        
        keep_deleting = input("Would you like to keep deleting? (y/n) ")

def adjust_salary(): #adjusts the hourly rate of as many employees as the user wants
    global employees
    
    keep_adjusting = 'y'

    while keep_adjusting.lower() == 'y':
        employee_id = int(input("Enter the ID of Employee to adjust: ")) 
        
        if employee_id not in employees:
            print(f"Employee with ID {employee_id} does not exist")
        else:
            new_hourly_wage = float(input("Enter the new hourly rate for Employee: "))
            employees[employee_id][2] = new_hourly_wage

        keep_adjusting = input("Would you like to keep adjusting salaries? (y/n)")

def search_employee():
    keep_searching = 'y'
    found = False

    while keep_searching.lower() == 'y':
        employee_name = input("Enter an Employee Name to search for: ")

        for key,value in employees.items():
            if(employees[key][0] == employee_name.lower()):
                print("Employee found.", end = "\n")
                print(f"Employee ID: {key} \nEmployee Name: {value[0]}")
                print(f"Employee Hours Worked: {value[1]} \nEmployee Hourly Rate: ${value[2]}", end = "\n")
                found = True
                break
        
        if not found:
            print(f"Employee with name {employee_name} does not exist")

        keep_searching = input("Would you like to keep searching? ")

def main():
    print("""\t\tEmployee Management System Menu:\n
    1. Add Employee
    2. View Employees
    3. Calculate Payroll (with Deductions and Benefits)
    4. Delete Employee
    5. Adjust Salary
    6. Search Employee
    7. Add new Employees (deletes all available employees before adding new ones)
    8. Quit """)

    while True: #creates an infinite loop
        choice = int(input("Enter your choice (1/2/3/4/5/6/7/8): "))

        #matches numbers to functions
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            calculate_payroll()
        elif choice == 4:
            delete_employee()
        elif choice == 5:
            adjust_salary()
        elif choice == 6:
            search_employee()
        elif choice == 7:
            new_employees()
        elif choice == 8: #if choice is 8, infinite loop is broken
            print("Thanks for using Employee Management System Menu. Goodbye....")
            break
        else:
            print("That is not a valid Choice.\n")
            
main()
