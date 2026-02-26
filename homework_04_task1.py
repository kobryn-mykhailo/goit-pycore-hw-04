# hw.04 Task 1: Extract aggregated and average salary for the employees

def total_salary(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                parts = line.split(',')
                salary = int(parts[1])
                total = total + salary
                count = count + 1
            average = total / count
            return (total, average)
                

    except FileNotFoundError:
        print(f"File {path} not found.")
        return None
    

total, average = total_salary("data/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # verification of the function result