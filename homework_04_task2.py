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

print(get_cats_info("data/cats.txt")) # verification of the function result
