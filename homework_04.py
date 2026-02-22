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
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") # verification of the function result


# hw.04 Task 2: Extract informatin about cats from the external file and present it in dictionary

def get_cats_info(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            cats = []
            for line in file:
                cat = line.strip()
                cat_parameters = cat.split(',')
                cat_dictionary = ({
                    "id": cat_parameters[0],
                    "name": cat_parameters[1],
                    "age": cat_parameters[2]
                })
                cats.append(cat_dictionary)
            return cats
        
    except FileNotFoundError:
        print(f"File {path} not found.")
        return None

# print(get_cats_info("data/cats.txt")) # verification of the function result
