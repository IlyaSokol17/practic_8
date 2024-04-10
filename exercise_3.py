salary = int(input('введите зарпплату житеоя города'))
sum_salary = 0
i = 0
while salary != 0:
    sum_salary += salary
    i += 1
    salary = int(input('введите зарпплату житеоя города'))
average_salary = sum_salary / i
print(average_salary)
