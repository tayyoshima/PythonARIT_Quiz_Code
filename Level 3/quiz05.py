#Each salary in the list is updated based on increase. Employees making
#$150,000 or more will not get a raise.
#Salary list is populated from employee database, code not shown. Ex.salary_list = [10011,20005,24000,35000,50000]
#Your Answer
    if salary_list[index] >= 150000:
        #Your Answer
    salary_list[index]=(salary_list[index]*1.03)+500
    print(salary_list[index])