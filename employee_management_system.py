employee_1_id, employee_1_name, employee_1_hours_worked, employee_1_hourly_rate, employee_1 = 0, "", 0, 0, 0 #declares the variables to be used throughout the program
employee_2_id, employee_2_name, employee_2_hours_worked, employee_2_hourly_rate, employee_2 = 0, "", 0, 0, 0 #sets employee_1 and employee_2 to 0, meaning there is no employee data yet

def add_employee(): #enters data for a new employee
    global employee_1_id, employee_1_name, employee_1_hours_worked, employee_1_hourly_rate, employee_1
    global employee_2_id, employee_2_name, employee_2_hours_worked, employee_2_hourly_rate, employee_2
    
    if employee_1 == 0:
        employee_1_id = int(input("Enter Employee 1 ID: "))
        employee_1_name = input("Enter Employee 1 Name: ")
        employee_1_hours_worked = int(input("Enter hours worked for Employee 1: "))
        employee_1_hourly_rate = int(input("Enter hourly rate for Employee 1: "))
        print("Employee added successfully\n")
        employee_1 = 1 #after entering all employee data, employee_1 is set to 1 meaning there is an employee
        
    elif employee_2 == 0:
        employee_2_id = int(input("Enter Employee 2 ID: "))
        employee_2_name = input("Enter Employee 2 Name: ")
        employee_2_hours_worked = int(input("Enter hours worked for Employee 2: "))
        employee_2_hourly_rate = int(input("Enter hourly rate for Employee 2: "))
        print("Employee added successfully\n")
        employee_2 = 1 #after entering all employee data, employee_2 is set to 1 meaning there is an employee
        
    else:
        print("Maximum employee amount reached\n") #if neither employee_1 or employee_2 are 0 then there is no space for another employee

def view_employees(): #prints employee data if either employee_1 or employee_2 are '1'. Informs user if both are '0'
    if employee_1 == 1:
        print(f"Employee 1 ID: {employee_1_id}\nEmployee 1 Name: {employee_1_name}\nEmployee 1 Hours Worked: {employee_1_hours_worked}\n" +
              f"Employee 1 Hourly Rate: ${employee_1_hourly_rate}/hr\n")
        
    if employee_2 == 1:
        print(f"Employee 2 ID: {employee_2_id}\nEmployee 2 Name: {employee_2_name}\nEmployee 2 Hours Worked: {employee_2_hours_worked}\n" +
              f"Employee 2 Hourly Rate: ${employee_2_hourly_rate}/hr\n")

    if employee_1 == 0 and employee_2 == 0:
        print("No Employee exists yet\n")

def calculate_payroll(): #calculates the pay of employees available
    if employee_1 == 0 and employee_2 == 0: #if both are '0', informs the user
        print("No Employee exists yet\n")
        
    if employee_1 == 1: #calculates and prints employee net salary based off of inputs from the user if employee_1 is 1
        tax_rate = int(input("Enter the tax rate for Employee 1 as a number: "))
        while tax_rate < 0 or tax_rate > 100:
            tax_rate = int(input("Error. Enter the tax rate for Employee 1 as a positive number not greater than 100): "))
            
        benefit_amount = int(input("Enter benefits for Employee 1 as a number: "))
        while benefit_amount < 0:
            benefit_amount = int(input("Error. Enter benefits for Employee 1 as a positive number: \n"))
            
        gross_salary = employee_1_hours_worked*employee_1_hourly_rate
        tax_deduction = gross_salary*(tax_rate/100)
        net_salary = gross_salary-tax_deduction+benefit_amount
        print(f"Employee 1 Name: {employee_1_name}\nEmployee ID: {employee_1_id}\nEmployee 1 Gross Salary: ${gross_salary}\n" +
              f"Employee 1 Tax Deduction: ${tax_deduction}\nEmployee 1 Benefit Amount: ${benefit_amount}\nEmployee 1 Net Salary: ${net_salary}\n")
        
    if employee_2 == 1: #calculates and prints employee net salary based off of inputs from the user if employee_2 is 1
        tax_rate = int(input("Enter the tax rate for Employee 2 as a number: "))
        while tax_rate < 0 or tax_rate > 100:
            tax_rate = int(input("Error. Enter the tax rate for Employee 2 as a positive number not greater than 100): "))
            
        benefit_amount = int(input("Enter benefits for Employee 2 as a number: "))
        while benefit_amount < 0:
            benefit_amount = int(input("Error. Enter benefits for Employee 2 as a positive number: "))
            
        gross_salary = employee_2_hours_worked*employee_2_hourly_rate
        tax_deduction = gross_salary*(tax_rate/100)
        net_salary = gross_salary-tax_deduction+benefit_amount
        print(f"Employee 2 Name: {employee_2_name}\nEmployee ID: {employee_2_id}\nEmployee 2 Gross Salary: ${gross_salary}\n" +
              f"Employee 2 Tax Deduction: ${tax_deduction}\nEmployee 2 Benefit Amount: ${benefit_amount}\nEmployee 2 Net Salary: ${net_salary}\n")

def delete_employee(employee_id): #deletes an employee with the id passed as an argument
    global employee_1_id, employee_2_id, employee_1, employee_2
    
    if employee_1_id == employee_id: #if employee_id passed by the user equals employee of employee_1, employee_1 is set to 0. Treated as if it's data is deleted
        employee_1 = 0
        print(f"Employee with ID {employee_id} has been deleted successfully\n")
        
    if employee_2_id == employee_id: #if employee_id passed by the user equals employee of employee_1, employee_1 is set to 0. Treated as if it's data is deleted
        employee_2 = 0
        print(f"Employee with ID {employee_id} has been deleted successfully\n")

    if employee_1_id != employee_id and employee_2_id != employee_id: #if the id passed by the user equals neither of them, 0 is returned (this will make sense later)
        return 0

def adjust_salary(): #adjusts the hourly rate of available employees
    global employee_1_hourly_rate, employee_2_hourly_rate
    
    employee_id = int(input("Enter the ID of Employee: ")) #asks for id of employee to adjust

    while True: #creates an infinite loop
        if employee_1_id == employee_id: #if id provided by user equals id of first employee, hourly rate for the first employee is changed. the infinite loop is then broken
            employee_1_hourly_rate = int(input("Enter the new Houly Rate for Employee 1: "))
            print("Hourly Rate for Employee 1 changed successfully\n")
            break

        if employee_2_id == employee_id: #if id provided by user equals id of second employee, hourly rate for the second employee is changed. the infinite loop is then broken
            employee_2_hourly_rate = int(input("Enter the new Houly Rate for Employee 2: "))
            print("Hourly Rate for Employee 2 changed successfully\n")
            break
        
        employee_id = int(input("Employee with ID " + str(employee_id) + " does not exist.\nEnter a new ID. Enter 0 to stop: ")) #if id provided by user isn't valid, user is prompted to enter a new one
        if employee_id == 0: #if the user enters 0, the loop is broken
            break

def search_employee():
    employee_name = input("Enter an Employee Name to search for: ")

    while True: #creates an infinite loop
        if employee_1 == 1: #if employee_1 exists
            if employee_name.lower() == employee_1_name.lower(): #if name provided by user equals name of first employee, date of the first employee is printed. the infinite loop is then broken
                print(f"Employee 1 ID: {employee_1_id}\nEmployee 1 Name: {employee_1_name}\nEmployee 1 Hours Worked: {employee_1_hours_worked}\n" +
                       f"Employee 1 Hourly Rate: ${employee_1_hourly_rate}/hr\n")
                break
            
        if employee_2 == 1: #if employee_2 exists
            if employee_name.lower() == employee_2_name.lower(): #if name provided by user equals name of second employee, date of the second employee is printed. the infinite loop is then broken
                print(f"Employee 2 ID: {employee_2_id}\nEmployee 2 Name: {employee_2_name}\nEmployee 2 Hours Worked: {employee_2_hours_worked}\n" +
                      f"Employee 2 Hourly Rate: ${employee_2_hourly_rate}/hr\n")
                break
        
        employee_name = input("Employee with Name " + employee_name + " does not exist.\nEnter a new Name to search for. Type 'stop' to stop searching: ")
        if(employee_name == "stop"): #if the user enters stop, the loop is broken
            break

def main():
    print("""\t\tEmployee Management System Menu:\n
    1. Add Employee
    2. View Employees
    3. Calculate Payroll (with Deductions and Benefits)
    4. Delete Employee
    5. Adjust Salary
    6. Search Employee
    7. Quit """)

    while True: #creates an infinite loop
        choice = int(input("Enter your choice (1/2/3/4/5/6/7): "))

        #matches numbers to functions
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            calculate_payroll()
        elif choice == 4:
            employee_id = int(input("Enter Employee ID to delete: ")) #gets employee id to be deleted from the user
            result = delete_employee(employee_id) 
            while result == 0: #while the return value for delete_employee() is 0, user is prompted to enter a new id to delete
                employee_id = int(input("There is no employee with that ID. Please enter a valid ID: "))
                result = delete_employee(employee_id) #calls the delete_employee() method again with new argument
                if result != 0: #if delete_employee return value is not zero the while loop is broken
                    break
        elif choice == 5:
            adjust_salary()
        elif choice == 6:
            search_employee()
        elif choice == 7: #if choice is 7, infinite loop is broken
            print("Thanks for using Employee Management System Menu. Goodbye....")
            break
        else:
            print("That is not a valid Choice.\n")
        
main()
