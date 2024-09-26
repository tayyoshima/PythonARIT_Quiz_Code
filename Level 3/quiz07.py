#The following variables have been declared:
employee_pay =[15000,120000,35000,45000]
count = 0
sum = 0

#There are two errors in the following code:
for index in range(0,len(employee_pay)-1):
    count += 1
    sum += employee_pay[index]
    average = sum//count
print("The total payroll is:", sum)
print("The average salary is:", average)



