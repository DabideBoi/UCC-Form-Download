import glob
import os.path

folder_path = 'Files/'
file_type = '/*txt'
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)
last_file = max_file.replace("Files\\", '')
last_file = last_file.replace('.txt', '')
print(last_file)