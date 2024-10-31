# Nexabet C. Tousssaint
# 10/29/2024
# P3HW2
# Program calculates paycheck based on over time or no over time

'''
Input: Get employee name from the user - string (name)
Input: Get hours worked from the user - int (hours)
Inpit: Get pay rate from user - float (pay_rate)

Output: print dotted line and employee name

If hours is greater than 40 (employee has OT)
  Variable for hours worked already exist
    (dont have to create pay rate, it already exist)
    create a variable (OT) that holds only the OT hours (hours - 40)
    create a variable for OT_pay_rate (pay_rate *1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay rate (pay_rate * 40)
    calculate gross pay (pay for OT + regular pay)
Else (NO OT - hours has to be 40 or less)
    create a variable(OT) that holds only the OT hours WHICH is ZERO
    calculate pay for OT hours WHICH IS 40
    calculate regular pay rate (pay_rate * 40)
     calculate gross pay (pay for OT + regular pay)

Display the line of strings with width specifiers
print(f"{'Hours worked':<20}{'Pay rate':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross pay':<20}")

'''

# Input
employee_name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("-" * 37)

# Display result aka pay

print(f"Employee name:    {employee_name}")
print()
print(f"{'Hours worked':<15}{'Pay rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross pay':<15}")
print("-" * 89)

# If
if hours > 40:
    OT_hours = hours - 40
    reg_pay = pay_rate * 40
    OT_pay_rate =  pay_rate * 1.5
    OT_pay = OT_pay_rate * OT_hours
    Gross_pay = reg_pay + OT_pay

else: 
    OT_hours = 0
    reg_pay = hours * pay_rate
    OT_pay_rate =  pay_rate * 1.5
    OT_pay = OT_pay_rate * OT_hours
    Gross_pay = reg_pay

# Display
print(f"{hours:<15.2f}${pay_rate:<15.2f}{OT_hours:<15.2f}${OT_pay:<15.2f}${reg_pay:<15.2f}${Gross_pay:<15.2f}")

