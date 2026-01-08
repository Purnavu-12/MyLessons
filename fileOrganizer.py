import os
import shutil

directory = os.path.join(os.path.expanduser("~"), " HERE ") #-> write the foldername of which you want to organize 

extentions = {
    ".pdf": "documents",
    ".docx": "documents",
    ".xlsx": "documents",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "TextFiles",
    ".mp4": "Videos",       
    ".mp3": "Audio"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        if extension in extentions:
            folder_name = extentions[extension]
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            destination = os.path.join(folder_path, filename)
            shutil.move(file_path, destination)

            print(f"Moved: {filename} to {folder_name}")
        else:
            print(f"Skipped: {filename}")
    else:
        print(f"Not a file: {filename}")

print("File organization complete.")
