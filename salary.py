salary = float(input("Enter salary: "))
experience = int(input("Enter experience (in years): "))

bonus = 0.20 * salary
da = 0.045 * salary
ta = 0.10 * salary
hra = 0.15 * salary
pf = 0.18 * salary

total_salary = salary + bonus + da + ta + hra - pf

print("Bonus:", bonus)
print("DA:", da)
print("TA:", ta)
print("HRA:", hra)
print("PF:", pf)
print("Total Salary:", total_salary)
