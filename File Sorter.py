import os, shutil

path = r"C:/Users/bowie/OneDrive/Masaüstü/Data analisti/"

file_name = os.listdir(path)
folder_names = ['EXCEL', 'SQL', 'POWERBI','CSV']

for i in range (0, len(folder_names)):
    if not os.path.exists(path + folder_names[i]):
        print("File crated")
        os.makedirs(path + folder_names[i])
    else:
        print("All Ready Exists")

for file in file_name:
    if ".csv" in file and not os.path.exists(path + "CSV/" + file):
        shutil.move(path + file, path + "CSV/" + file)
    elif ".xlsx" in file and not os.path.exists(path + "EXCEL/" + file):
        shutil.move(path + file, path + "EXCEL/" + file)
    elif ".pbix" in file and not os.path.exists(path + "POWERBI/" + file):
        shutil.move(path + file, path + "POWERBI/" + file)
    else: print("No file changed")