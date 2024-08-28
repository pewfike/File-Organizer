# Creating a File Organizer script
# In order to sort all the types of files that I have on my desktop
# So I don't need to manually sort them

import os
import shutil

# Define the path to your desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the file types and their corresponding folders
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    elif os.path.isfile(folder_path):
        print(f"Error: A file with the name '{folder}' exists on the desktop. Please remove or rename this file.")
        exit(1)

# Function to move the file, handling potential name conflicts
def move_file(file_path, destination_folder):
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)

    # If the file already exists in the destination folder, rename it
    if os.path.exists(destination_path):
        base, extension = os.path.splitext(filename)
        counter = 1
        new_filename = f"{base}_{counter}{extension}"
        new_destination_path = os.path.join(destination_folder, new_filename)

        while os.path.exists(new_destination_path):
            counter += 1
            new_filename = f"{base}_{counter}{extension}"
            new_destination_path = os.path.join(destination_folder, new_filename)

        destination_path = new_destination_path

    # Move the file
    shutil.move(file_path, destination_path)
    print(f"Moved: {filename} to {destination_folder}")

# Organize files
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    
    if os.path.isfile(file_path):  # Check if it's a file (not a folder)
        moved = False
        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                move_file(file_path, os.path.join(desktop_path, folder))
                moved = True
                break
        if not moved:
            move_file(file_path, os.path.join(desktop_path, "Others"))

print("Desktop files organized successfully!")
