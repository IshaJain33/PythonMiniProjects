#importing necessary libraries

import os
import shutil

source_folder = "C:/Users/User/pythonprom"   #specify your own path
destinations = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
}
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in destinations.items():
            if file.endswith(tuple(extensions)):
                folder_path = os.path.join(source_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)

print("Files organized successfully!")
