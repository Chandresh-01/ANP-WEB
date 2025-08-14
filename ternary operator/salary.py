salary = float(input("Enter your salary: "))
experience = int(input("Enter years of experience: "))

bonus = salary * (0.10 if experience > 10 else 0.05)
total_salary = salary + bonus

print(f"Bonus: {bonus}, Total Salary: {total_salary}")
